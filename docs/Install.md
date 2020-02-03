##  Prerequisites

Commonly, you do not have to care about prerequisites because the package manager pip automatically install anything you need.

**BUT:** MIScnn does NOT use Tensorflow 2.0 (right now)!  
Therefore, if you have a higher Tensorflow or Keras version, please install the two modules manually with the correct version or in a separate package environment (e.g. with [Conda](https://docs.conda.io/en/latest/)).  

MIScnn currently only supports Tensorflow 1.13 and Keras 2.2.4.  
Keras install instructions: https://keras.io/#installation

## MIScnn Installation

There are two ways to install MIScnn:

- **Install MIScnn from PyPI (recommended):**

Note: These installation steps assume that you are on a Linux or Mac environment. If you are on Windows or in a virtual environment without root, you will need to remove sudo to run the commands below.

```sh
sudo pip install miscnn
```

- **Alternatively: install MIScnn from the GitHub source:**

First, clone MIScnn using git:

```sh
git clone https://github.com/frankkramer-lab/MIScnn
```

Then, cd to the MIScnn folder and run the install command:

```sh
cd MIScnn
sudo python setup.py install
```
