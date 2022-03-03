# `jupyterlab-hide-code`: A JupyterLab Extension to Run and Hide Source Code

This extension adds a button in JupyterLab which enables one to run the code cells of a notebook and have them subsequently be hidden from view.
This JupyterLab extension was inspired by the 
[`jlab-hide-code`](https://github.com/AixViPMaP/jlab-hide-code) JupyterLab
extension from Aachen (Aix) Virtual Platform for Materials Processing.

Clicking the button for a first time will run all code cells before hiding their contents (displaying only the output of the cells). It allows
users to check the layout of the output cells in an efficient way. One call toggle
back the content of the code cells by clicking the button again.

````{admonition} Installation
```bash
pip install jupyterlab-hide-code
```
````

![image hide code](./images/hide-input.gif)