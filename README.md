# Awesome Few-Shot Anomaly Detection

> A curated collection of papers, code repositories, datasets, and resources for **Few-Shot Anomaly Detection (FSAD)**.

This repository accompanies our survey paper:

**When Data Is Scarce: A Systematic Survey of Few-Shot Learning for Visual Anomaly Detection** 


---

## Overview

Few-shot anomaly detection focuses on identifying anomalous samples when only a small number of training examples are available.

This repository aims to provide:

- A structured list of representative papers
- Links to official implementations
- Download links for commonly used datasets
- A simple taxonomy of existing methods
- Benchmark and evaluation references

> This repository only provides links to external resources. Please follow the original licenses and terms of use for all papers, codebases, datasets, and pretrained models.

---

## Contents

- [Taxonomy](#taxonomy)
- [Papers and Code](#papers-and-code)
- [Datasets](#datasets)
- [Evaluation](#evaluation)
- [License](#license)

---

## Taxonomy

The literature can be broadly grouped into:

- **Distribution-based methods**

- **Reconstruction--based methods**

- **Distance--based methods**

- **VLM-based methods**

- **Residual-based methods**


---

## Papers and Code

### Legend

- ✅ Official implementation
- 🧩 Third-party implementation
- 🚫 No public code


### Distribution-based methods

- [DifferNet](https://arxiv.org/abs/2008.12577) — ✅[Code](https://github.com/marco-rudolph/differnet)
- [TDG](https://openaccess.thecvf.com/content/ICCV2021/html/Sheynin_A_Hierarchical_Transformation-Discriminating_Generative_Model_for_Few_Shot_Anomaly_Detection_ICCV_2021_paper.html) — 🚫
- [RegAD](https://arxiv.org/abs/2207.07361) — ✅[Code](https://github.com/MediaBrain-SJTU/RegAD)
- [PDD](https://link.springer.com/chapter/10.1007/978-3-031-26387-3_17) — ✅[Code](https://github.com/ProtoDD/pdd)
- [COFT-AD](https://ieeexplore.ieee.org/abstract/document/10471293) — 🚫

### Reconstruction--based methods

- [Metaformer](https://openaccess.thecvf.com/content/ICCV2021/html/Wu_Learning_Unsupervised_Metaformer_for_Anomaly_Detection_ICCV_2021_paper.html) — 🚫
- [Wang et al.](https://proceedings.neurips.cc/paper_files/paper/2022/hash/1fe6f635fe265292aba3987b5123ae3d-Abstract-Conference.html) — 🚫
- [FastRecon](https://paperswithcode.com/paper/fastrecon-few-shot-industrial-anomaly) — ✅[Code](https://github.com/FzJun26th/FastRecon)
- [MAEDAY](https://www.sciencedirect.com/science/article/abs/pii/S1077314224000390) — 🚫
- [Li et al.](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8f4477b086a9c97e30d1a0621ea6b2f5-Abstract-Conference.html) — 🚫
- [INP-Former](https://paperswithcode.com/paper/fastrecon-few-shot-industrial-anomaly) — ✅[Code](https://github.com/luow23/INP-Former)
- [INP-Former++](https://arxiv.org/pdf/2506.03660) — 🚫
- [DictAS](https://www.arxiv.org/abs/2508.13560) — ✅[Code](https://github.com/xiaozhen228/DictAS)

### Distance--based methods

- [SPADE](https://arxiv.org/abs/2005.02357) — 🚫
- [PaDiM](https://link.springer.com/chapter/10.1007/978-3-030-68799-1_35) — 🚫
- [PatchCore](https://arxiv.org/abs/2106.08265) — ✅[Code](https://github.com/amazon-science/patchcore-inspection)
- [FewSOME](https://arxiv.org/pdf/2301.06957.pdf) — ✅[Code](https://github.com/niamhbelton/FewSOME)
- [GraphCore](https://arxiv.org/abs/2301.12082) — 🚫
- [PCSNet](https://ieeexplore.ieee.org/abstract/document/10702559) — ✅[Code](https://github.com/yuxin-jiang/PCSNet)
- [AnomalyDINO](https://arxiv.org/abs/2405.14529) — ✅[Code](https://github.com/dammsi/AnomalyDINO)
- [CIF](https://arxiv.org/abs/2511.05966) — ✅[Code](https://github.com/Sunny5250/CIF)

### VLM-based methods

- [GraphCore]() — ✅[Code]()
- [WinCLIP](https://openaccess.thecvf.com/content/CVPR2023/papers/Jeong_WinCLIP_Zero-Few-Shot_Anomaly_Classification_and_Segmentation_CVPR_2023_paper.pdf) — 🧩[Code](https://github.com/mala-lab/WinCLIP)
- [PromptAD](http://arxiv.org/abs/2404.05231) — ✅[Code](https://github.com/FuNz-0/PromptAD)
- [AnomalyGPT](https://ojs.aaai.org/index.php/AAAI/article/view/27963)  — 🚫
- [IIPAD](https://openreview.net/forum?id=Zzs3JwknAY) — ✅[Code](https://github.com/Vanssssry/One-For-All-Few-Shot-Anomaly-Detection)
- [KAG-prompt](https://ojs.aaai.org/index.php/AAAI/article/view/32790) — ✅[Code](https://github.com/CVL-hub/KAG-prompt)
- [AdaptCLIP](https://www.arxiv.org/pdf/2505.09926) — ✅[Code](https://github.com/gaobb/AdaptCLIP)

### Residual-based methods

- [InCTRL](https://arxiv.org/pdf/2403.06495.pdf) — ✅[Code](https://github.com/mala-lab/InCTRL)
- [ResAD](https://arxiv.org/abs/2410.20047) — ✅[Code](https://github.com/xcyao00/ResAD)
- [ResAD++](https://link.springer.com/article/10.1007/s11263-026-02885-1) — ✅[Code](https://github.com/xcyao00/ResAD)
- [NAGL](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a437d77270d5588a84d63a851a3fdeb-Abstract-Conference.html) — ✅[Code](https://github.com/JasonKyng/NAGL)


---

## Datasets

### Dataset List

| Dataset | Modality | Domain | Annotation | Download |
|---|---|---|---|---|
| MVTec AD | Image | Industrial | Image / pixel level | [Download](https://www.mvtec.com/company/research/datasets/mvtec-ad) |
| VisA | Image | Industrial | Image / pixel level | [Download](https://github.com/amazon-science/spot-diff) |
| BTAD | Image | Industrial | Image / pixel level | [Download](http://avires.dimi.uniud.it/papers/btad/btad.zip) |
| MVTec 3D  | Image | Industrial | Image / pixel level | [Download](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) |
| MPDD | Image | Industrial | Image / pixel level | [Download](https://github.com/stepanje/MPDD) |
| BraTS | MRI | Medical | Image level | [Download](https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1) |


---

## Evaluation

Common evaluation metrics include:

- AUROC
- AUPR / Average Precision
- F1-score
- AUPRO / PRO



---

## License

The original content and scripts in this repository are released under the [MIT License](LICENSE), unless otherwise stated.

External papers, code repositories, datasets, pretrained models, and figures remain subject to their original licenses and terms of use.

---

## Acknowledgements

We thank the authors and maintainers who make their papers, code, datasets, and pretrained models publicly available.

For missing resources, corrections, or broken links, please open an [Issue](<ISSUES_URL>) or submit a [Pull Request](<PULL_REQUEST_URL>).

---

## Star

If you find this repository useful, please consider giving it a star.
