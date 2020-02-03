The examples for MIScnn are implemented in Jupyter Notebooks. Jupyter Notebooks offer reproducibility by including the output of each coding block, but can also integrate commentary blocks with Markdown. Also, Jupyter Notebooks can be directly displayed in GitHub without any additional software.

## Overview

| Data Set | Task | Jupyter Notebook  |
|-------------|:--------------------:|:------:|
| [KiTS19](#KiTS19) | 3-fold cross-validation | [KiTS19.ipynb](https://github.com/frankkramer-lab/MIScnn/blob/master/examples/KiTS19.ipynb) |

## <a name="KiTS19"></a>Kidney Tumor Segmentation Challenge 2019 (KiTS19)

With more than 400 000 kidney cancer diagnoses worldwide in 2018, kidney cancer is under the top 10 most common cancer types in men and under the top 15 in woman.

The goal of the KiTS19 challenge is the development of reliable and unbiased kidney and kidney tumor semantic segmentation methods. Therefore, the challenge built a data set for arterial phase abdominal CT scan of 300 kidney cancer patients. The original scans have an image resolution of 512x512 and on average 216 slices (highest slice number is 1059).

For all CT scans, a ground truth semantic segmentation was created by experts. This semantic segmentation labeled each pixel with one of three classes: Background, kidney or tumor. 210 of these CT scans with the ground truth segmentation were published during the training phase of the challenge, whereas 90 CT scans without published ground truth were released afterwards in the submission phase.

The CT scans were provided in NIfTI format in original resolution and also in interpolated resolution with slice thickness normalization.

The data for the KITS19 challenge can be found here: [https://github.com/neheller/kits19](https://github.com/neheller/kits19)
