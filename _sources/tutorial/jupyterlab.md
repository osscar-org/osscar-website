# JupyterLab

## 1. Introduction

JupyterLab is the next-generation GUI for the Jupyter project, taking over from the standard Jupyter notebook. We use JupyterLab as the OSSCAR development
environment. 

### a. Installation

JupyterLab can be easily installed via pip:

```bash
pip install --upgrade jupyterlab
```

Otherwise, you can alternatively use the
EPFL <a href="https://noto.epfl.ch">NOTO platform</a>, which offers JupyterLab
as a cloud webpage.

## 2. JupyterLab extensions

JupyterLab allows for the development and installation of extensions. For the development of the
notebooks, we need to install two JupyterLab extensions.

### a. JupyterLab hide code extension

We developed the "jupyterlab-hide-code" extension, which runs all code cells of the current notebook and hides their output. It is useful to quickly check the layout of the notebook's output. Install it with pip:

```bash
pip install --upgrade jupyterlab-hide-code
```

Once installed it shall show up as a button with an eye icon in the toolbar of the current notebook. One can
toggle to hide or show the source codes by clicking the button.

![Jupyterlab hide code](./images/hide-input.gif)

### b. Voila extension

The Voila package provides a JupyterLab extension. After installing Voila with
pip, one will have the Voila extension available in JupyterLab.

```bash
pip install --upgrade voila 
```

![Jupyterlab Voila](./images/jupyterlab_voila.gif)
