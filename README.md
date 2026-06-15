# Awesome Few-Shot Anomaly Detection

> A curated collection of papers, code repositories, datasets, and resources for **Few-Shot Anomaly Detection (FSAD)**.

This repository accompanies our survey paper:

**[Survey Paper Title]**  
[Author 1], [Author 2], [Author 3]  
[Journal / Conference / arXiv], [Year]

[![Paper](https://img.shields.io/badge/Paper-PDF-red)](<PAPER_URL>)
[![arXiv](https://img.shields.io/badge/arXiv-xxxx.xxxxx-b31b1b.svg)](<ARXIV_URL>)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Overview

Few-shot anomaly detection focuses on identifying anomalous samples when only a small number of training examples are available.

This repository aims to provide:

- A structured list of representative papers
- Links to official and third-party implementations
- Download links for commonly used datasets
- A simple taxonomy of existing methods
- Benchmark and evaluation references
- Updates, corrections, and newly published work

> This repository only provides links to external resources. Please follow the original licenses and terms of use for all papers, codebases, datasets, and pretrained models.

---

## Contents

- [Survey Paper](#survey-paper)
- [Scope](#scope)
- [Taxonomy](#taxonomy)
- [Papers and Code](#papers-and-code)
- [Datasets](#datasets)
- [Evaluation](#evaluation)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Survey Paper

### Abstract

[Add a short version of the survey abstract here.]

### Main Contributions

- A unified definition of few-shot anomaly detection
- A taxonomy of major research directions
- A summary of representative methods and applications
- A comparison of datasets and evaluation protocols
- A discussion of open challenges and future directions

### Links

- Paper: [PDF](<PAPER_URL>)
- arXiv: [Link](<ARXIV_URL>)
- Project page: [Link](<PROJECT_PAGE_URL>)
- Supplementary material: [Link](<SUPPLEMENTARY_URL>)

---

## Scope

This repository mainly covers the following settings:

- Few-shot normal-only anomaly detection
- Few-shot supervised anomaly detection
- Few-shot anomaly segmentation
- Few-shot domain adaptation
- Few-shot anomaly classification
- Meta-learning for anomaly detection
- Foundation-model-based anomaly detection
- Zero-shot and training-free anomaly detection as related topics

Supported data modalities may include:

- Images
- Videos
- Time series
- Graphs
- Medical data
- Multimodal data

---

## Taxonomy

The literature can be broadly grouped into:

- **Metric-based methods**
  - Nearest-neighbor matching
  - Prototype learning
  - Feature distance modeling

- **Transfer-learning methods**
  - Fine-tuning
  - Domain adaptation
  - Parameter-efficient adaptation

- **Meta-learning methods**
  - Episodic training
  - Task-level adaptation
  - Meta-optimization

- **Generative methods**
  - Autoencoders
  - GANs
  - Normalizing flows
  - Diffusion models

- **Data synthesis methods**
  - Synthetic anomalies
  - Feature perturbation
  - Defect generation

- **Foundation-model-based methods**
  - Vision-language models
  - Prompt learning
  - In-context learning
  - Training-free methods

---

## Papers and Code

### Legend

- ✅ Official implementation
- 🧩 Third-party implementation
- 📦 Pretrained model available
- 🚫 No public code

### Representative Methods

| Year | Method | Paper | Venue | Setting | Code |
|---:|---|---|---|---|---|
| 20XX | Method A | [Paper](<PAPER_URL>) | CVPR | 1-shot image AD | [✅ Code](<CODE_URL>) |
| 20XX | Method B | [Paper](<PAPER_URL>) | NeurIPS | 5-shot image AD | [✅ Code](<CODE_URL>) |
| 20XX | Method C | [Paper](<PAPER_URL>) | ICCV | Few-shot adaptation | [🧩 Code](<CODE_URL>) |
| 20XX | Method D | [Paper](<PAPER_URL>) | KDD | Time-series AD | 🚫 |
| 20XX | Method E | [Paper](<PAPER_URL>) | AAAI | Meta-learning | [✅ Code](<CODE_URL>) |

### Metric-Based Methods

- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — No public code

### Transfer and Adaptation Methods

- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — No public code

### Meta-Learning Methods

- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)

### Generative Methods

- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)

### Foundation-Model-Based Methods

- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — [Code](<CODE_URL>)
- [Method Name](<PAPER_URL>) — No public code

### By Application

- **Industrial inspection**
  - [Method Name](<PAPER_URL>)
  - [Method Name](<PAPER_URL>)

- **Medical anomaly detection**
  - [Method Name](<PAPER_URL>)
  - [Method Name](<PAPER_URL>)

- **Video anomaly detection**
  - [Method Name](<PAPER_URL>)

- **Time-series anomaly detection**
  - [Method Name](<PAPER_URL>)

- **Graph anomaly detection**
  - [Method Name](<PAPER_URL>)

> For a large collection, consider moving the full paper list to `resources/papers.md` or `resources/papers.csv`.

---

## Datasets

### Dataset List

| Dataset | Modality | Domain | Annotation | Download |
|---|---|---|---|---|
| Dataset A | Image | Industrial | Image / pixel level | [Download](<DATASET_URL>) |
| Dataset B | Image | Medical | Image level | [Download](<DATASET_URL>) |
| Dataset C | Video | Surveillance | Frame level | [Download](<DATASET_URL>) |
| Dataset D | Time series | Sensor | Point / interval level | [Download](<DATASET_URL>) |
| Dataset E | Graph | Network | Node / edge level | [Download](<DATASET_URL>) |

### Recommended Dataset Information

For each dataset, record:

- Official homepage
- Download link
- Reference paper
- Data modality
- Number of classes
- Annotation type
- Few-shot split protocol
- License or access requirements
- Known issues

### Suggested Few-Shot Split Format

```text
Dataset: <DATASET_NAME>
Shots: 1, 2, 4, 8
Random seeds: 0, 1, 2, 3, 4
Number of repeated runs: 5
Split files: splits/<dataset_name>/
```

---

## Evaluation

Common evaluation metrics include:

- AUROC
- AUPR / Average Precision
- F1-score
- Accuracy
- AUPRO / PRO
- IoU
- Dice score
- Recall@K
- Inference time
- Memory usage
- Number of parameters

Recommended reporting practices:

- Report mean and standard deviation over multiple runs
- Clearly specify the number of shots
- Report random seeds
- Distinguish image-level and pixel-level results
- Describe threshold selection
- Avoid tuning on the test set
- Report the backbone and pretrained data
- Use consistent data splits for comparison

---

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── CHANGELOG.md
├── assets/
│   ├── taxonomy.png
│   └── overview.png
├── resources/
│   ├── papers.md
│   ├── papers.csv
│   ├── datasets.md
│   ├── datasets.csv
│   └── benchmarks.md
└── scripts/
    ├── check_links.py
    └── build_tables.py
```

Optional resource files:

- `resources/papers.csv`: structured paper metadata
- `resources/datasets.csv`: dataset metadata
- `resources/benchmarks.md`: benchmark results
- `assets/taxonomy.png`: survey taxonomy figure
- `assets/overview.png`: repository overview figure

---

## Updates

- **[YYYY-MM-DD]** Initial release
- **[YYYY-MM-DD]** Added new papers and code repositories
- **[YYYY-MM-DD]** Added dataset download links
- **[YYYY-MM-DD]** Updated broken links

See [CHANGELOG.md](CHANGELOG.md) for details.

---

## Contributing

Contributions are welcome.

You may contribute:

- New papers
- Official code repositories
- Third-party implementations
- Dataset links
- Pretrained models
- Reproduction results
- Corrections
- Broken-link reports

### How to Contribute

1. Fork this repository
2. Create a new branch
3. Add or update the relevant entry
4. Verify the links
5. Submit a pull request

### Submission Checklist

- [ ] The paper link is publicly accessible
- [ ] The code is marked as official or third-party
- [ ] The dataset link points to an official or authorized source
- [ ] The entry is not duplicated
- [ ] The format is consistent
- [ ] License restrictions are respected

---

## Citation

If this survey or repository is useful for your research, please cite:

```bibtex
@article{<citation_key>,
  title   = {<Paper Title>},
  author  = {<Author 1> and <Author 2> and <Author 3>},
  journal = {<Journal or Conference>},
  year    = {<Year>},
  volume  = {<Volume>},
  number  = {<Number>},
  pages   = {<Pages>},
  doi     = {<DOI>}
}
```

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
