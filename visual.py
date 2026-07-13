import glob
import shutil
import cv2
import os
import numpy as np
import tifffile as tiff
import random
from matplotlib import cm


def visualize_anomaly_map(
    score_path,
    image_path,
    save_path,
    alpha=0.5,
    cmap="jet",
    percentile=99,
):
    """
    Generate and save an anomaly heatmap overlaid on the original image.

    Args:
        score_path (str): Path to an anomaly score map in TIFF or NumPy format.
        image_path (str): Path to the corresponding original image.
        save_path (str): Path used to save the resulting visualization.
        alpha (float): Opacity of the heatmap overlay.
        cmap (str): Name of the Matplotlib colormap.
        percentile (float): Upper percentile used to suppress noisy scores.
    """
    if score_path.endswith((".tiff", ".tif")):
        score_map = tiff.imread(score_path).astype(np.float32)
    elif score_path.endswith(".npy"):
        score_map = np.load(score_path).astype(np.float32)
    else:
        raise ValueError(
            "Unsupported score file format. Use .tiff/.tif or .npy."
        )

    if score_map.ndim == 3 and score_map.shape[0] == 1:
        score_map = score_map.squeeze(0)

    if score_map.ndim != 2:
        raise ValueError(
            f"Expected a 2D anomaly map, but received {score_map.shape}."
        )

    original = cv2.imread(image_path)
    if original is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    if score_map.shape != original.shape[:2]:
        score_map = cv2.resize(
            score_map,
            (original.shape[1], original.shape[0]),
            interpolation=cv2.INTER_LINEAR,
        )

    minimum_score = score_map.min()
    maximum_score = np.percentile(score_map, percentile)

    if maximum_score <= minimum_score:
        maximum_score = minimum_score + 1e-6

    normalized_score = np.clip(
        (score_map - minimum_score) / (maximum_score - minimum_score),
        0,
        1,
    )

    colormap = cm.get_cmap(cmap)
    heatmap = colormap(normalized_score)[:, :, :3]
    heatmap = (heatmap * 255).astype(np.uint8)

    overlay = cv2.addWeighted(
        original,
        1 - alpha,
        heatmap,
        alpha,
        0,
    )

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cv2.imwrite(
        save_path,
        cv2.cvtColor(overlay, cv2.COLOR_RGB2BGR),
    )

    print(f"Saved visualization to {save_path}")


def select_files(root_dir, k=None):
    """
    Select files from every leaf directory under a root directory.

    Args:
        root_dir (str): Root directory to search recursively.
        k (int, optional): Number of files randomly selected from each leaf
            directory. If None, all files are selected.

    Returns:
        list[str]: Paths to the selected files.
    """
    selected_files = []

    for directory_path, directory_names, file_names in os.walk(root_dir):
        if directory_names:
            continue

        if k is None:
            selected_names = file_names
        else:
            sample_size = min(k, len(file_names))
            selected_names = random.sample(file_names, sample_size)

        for file_name in selected_names:
            selected_files.append(
                os.path.join(directory_path, file_name)
            )

    return selected_files


if __name__ == "__main__":
    map_path = "Directory containing the generated anomaly score maps."

    data_path = "Root directory of the dataset"

    output_path = "Directory used to save heatmaps, original images, and masks."

    map_files = select_files(map_path)

    for map_file in map_files:
        file_name = os.path.basename(map_file).split(".")[0]
        relative_directory = os.path.dirname(
            map_file[len(map_path) + 1:]
        )

        image_file = glob.glob(
            os.path.join(data_path, relative_directory, file_name) + ".*"
        )[0]

        sample_output_path = os.path.join(
            output_path,
            relative_directory,
            file_name,
        )
        os.makedirs(sample_output_path, exist_ok=True)

        visualize_anomaly_map(
            map_file,
            image_file,
            os.path.join(
                sample_output_path,
                os.path.basename(image_file),
            ),
        )

        shutil.copy2(
            image_file,
            os.path.join(
                sample_output_path,
                "o" + os.path.basename(image_file),
            ),
        )

        mask_files = glob.glob(
            os.path.join(
                data_path,
                relative_directory,
                file_name,
            ).replace("test", "ground_truth")
            + ".*"
        )

        if mask_files:
            mask_file = mask_files[0]
            shutil.copy2(
                mask_file,
                os.path.join(
                    sample_output_path,
                    "m" + os.path.basename(mask_file),
                ),
            )