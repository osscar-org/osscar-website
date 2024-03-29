# `widget-code-input`: A widget to allow input of a python function, with syntax highlighting.

**Source code:** [https://github.com/osscar-org/widget-code-input](https://github.com/osscar-org/widget-code-input) 

**Introduction**: This is a widget which allows users to implement small python functions dynamically and interactively. It uses the codemirror library to create the input area. The goal of this widget is to let students implement functions that can be given by tutors as assignments. The function becomes an actual python function that can be immediately run (and that it is run in a sandboxed environment, without access to the jupyter notebook global variables). It is also possible to select a custom code theme. This widget is particularly useful in combination with AppMode and/or voila.


## Try it with Binder !

* Simple usage of the widget code input

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/widget-code-input/master?urlpath=%2Ftree%2Fexamples%2Fintroduction.ipynb)

* Impact distance of a projectile ( a exmaple for using the widget-code-input for a educational notebook )

- Text for the exercise: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/widget-code-input/develop?urlpath=%2Fvoila%2Frender%2Fdemos%2Fprojectile-notebook.ipynb)

- The interactive exercise: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/widget-code-input/develop?urlpath=%2Fvoila%2Frender%2Fdemos%2Fprojectile-inline.ipynb)

## Installation

You can install using `pip`:

```bash
pip install widget_code_input
```

Or if you use jupyterlab:

```bash
pip install widget_code_input
jupyter lab build
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] widget_code_input
```
There are seven different code themes can be chosen. They are "eclipse",
"idea", "material", "midnight", "monokai", "nord" and "solarized".
You can check the appearance of the code themes at:

[https://codemirror.net/demo/theme.html](https://codemirror.net/demo/theme.html)


