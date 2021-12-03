# Use Widgets

Widgets is the core of our interactive web applications. We mainly use the
`ipywidgets` package. 

The ipywidgets can be installed with pip:

```bash
pip install --upgrade ipywidgets
```

Ipywidgets offer a large number of widgets as interactive components.

## Example: create a slider with integer number

```python
import ipywidgets as widgets

w = widgets.IntSlider(value=0, min=-10, max=10, description='A slider:')
display(w)
```

The `display` function will show the widget in the notebook.

## Example: Textarea to show some text
```python
import ipywidgets as widgets

w = widgets.Textarea(
    value='Hello the world!',
    placeholder='Type something',
    description='String:',
    disabled=False
)

display(w)
```

For more widgets, please read the <a
href="https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html">ipywidgets
document</a>.

## Use matplotlib figure as widget

Leveraging the Jupyter interactive widgets framework, `ipympl` enables the
interactive features of matplotlib in the Jupyter notebook and in JupyterLab.
To enable the ipympl backend, simply use the matplotlib Jupyter magic:

```python
%matplotlib widget
```

## Use OSSCAR widgets

In the OSSCAR project, we have developed a few custom widgets related to
computational chemistry and physics. For example, we developed a interactive
periodic table.

![widget periodic table](images/widget_periodictable.gif)

For more information, please check the "Tools" section.
