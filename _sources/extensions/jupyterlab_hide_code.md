# `jupyterlab-hide-code`: A JupyterLab Extension to Run and Hide Source Code

A button in JupyterLab to run the code cells and then to hide the code cells.
This JupyterLab extension was inspired by the 
[`jlab-hide-code`](https://github.com/AixViPMaP/jlab-hide-code) JupyterLab
extension from Aachen (Aix) Virtual Platform for Materials Processing.

This extension creates a button on the toolbar of each opened notebook.
Clicking it first time will run all code cells and hide the codecells. It allows
users to check the layout of the output cells in a fast way. One call toggle
back the code cells by clicking the button again.

````{admonition} Installation
```bash
pip install jupyterlab-hide-code
```
````

![image hide code](./images/hide-input.gif)