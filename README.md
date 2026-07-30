# ProBCR-Project

# ProBCR Project

## Deep learning analysis of prostate cancer histopathology images

This repository contains code developed during my Master’s research project on the application of deep learning to digital pathology images of prostate cancer.

The project explored computational methods for analysing whole-slide histopathology images and investigating image-based prediction tasks related to prostate cancer, including biochemical recurrence (BCR).

## Project overview

Digital pathology produces very large whole-slide images that cannot be processed directly by most conventional machine learning workflows. This project therefore used a pipeline in which slides were divided into smaller image patches, filtered and organised before being used for model development and evaluation.

The repository includes scripts for:

* generating image tiles from whole-slide images;
* filtering low-information image patches;
* organising images and associated labels;
* creating patient-level training, validation, and test partitions;
* preparing five-fold cross-validation datasets;
* running and processing model inference;
* comparing normalised and non-normalised images;
* calculating classification performance metrics;
* generating confusion matrices and visualising training results.

## Research workflow

The general workflow followed in the project was:

1. **Whole-slide image preparation**
   Histopathology slides were processed and divided into smaller image patches.

2. **Patch selection and preprocessing**
   Low-information patches were removed using image entropy, and image-normalisation approaches were investigated.

3. **Dataset organisation**
   Images and labels were organised at patient level to reduce the risk of information leakage between training and evaluation datasets.

4. **Model development**
   Deep learning experiments were performed using the NiftyNet framework.

5. **Cross-validation and inference**
   Patient-level data partitions and five-fold cross-validation were used to evaluate model performance.

6. **Performance evaluation**
   Predictions were evaluated using confusion matrices and classification metrics including accuracy, precision, recall, F1 score, balanced accuracy, and Cohen’s kappa.

## Repository structure

```text
ProBCR-Project/
├── BCR/                       # Configuration and files related to BCR experiments
├── WSI_PACK/                  # Whole-slide image processing utilities
├── niftynet/                  # NiftyNet framework files
├── py-wsi/                    # Whole-slide image processing dependency
├── CROSS_VAL.py               # Patient-level data splitting and cross-validation
├── FUNCTIONS_images.py        # Image organisation and filtering functions
├── tilemaker.py               # Generation of patches from large images
├── run_all_tilemaker.py       # Batch execution of the tiling workflow
├── inference_files.py         # Processing of inference output
├── confusion_matrix.py        # Classification metrics and confusion matrices
├── results_calculations.py    # Calculation and comparison of model results
├── plot_accuracy_loss.py      # Training-curve visualisation
├── plots_tensorboard.py       # TensorBoard result processing
└── additional utility scripts
```

## Main technologies

The project was developed primarily in Python and used tools and libraries including:

* Python
* NumPy
* pandas
* OpenCV
* scikit-image
* scikit-learn
* Matplotlib
* NiftyNet
* TensorFlow
* `py-wsi`

## Data availability

The medical imaging data used in this project are not included in this repository because they contain sensitive clinical information and are subject to institutional data-governance requirements.

The file paths in some scripts refer to the original local research environment and must be updated before the code can be run on another system.

## Reproducibility note

This repository is an archive of research code developed during a Master’s project. It documents the main preprocessing, modelling, and evaluation steps used in the study, but it is not currently distributed as a fully packaged or independently reproducible software application.

Reproducing the original experiments would require:

* access to the original histopathology dataset;
* the corresponding clinical labels;
* compatible versions of the original dependencies;
* adjustment of local file paths and configuration files;
* appropriate computational resources for deep learning.

## Skills demonstrated

This project involved:

* scientific programming in Python;
* digital pathology and medical image processing;
* machine learning and deep learning;
* patient-level dataset preparation;
* cross-validation;
* statistical model evaluation;
* processing of large image datasets;
* research workflow development;
* interpretation and visualisation of classification results.

## Author

**Carolina Carrapiço Seabra**

Biomedical Engineer with experience in medical imaging, clinical research, quantitative analysis, and data-driven healthcare applications.

## Disclaimer

This repository is provided for research purposes. It is not intended for clinical use, medical diagnosis, or treatment decision-making.
