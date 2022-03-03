#!/usr/bin/env python
# coding: utf-8

# # `widget-periodictable`: A Jupyter Widget to Create Interactive Periodic Table
# 
# **Introduction**: The periodic table is an important tool for chemistry and physics 
# education and research. This is a Jupyter widget to create an interactive periodic 
# table. Users can customize the colors of the elements and group elements by assigning them colors. 
# The elements are also clickable and trigger custom events.
# 
# ```{image} ./images/widget_periodictable.png
# :alt: image periodictable
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```
# 
# ````{admonition} Installation
# ```bash
# pip install --upgrade widget-periodictable
# ```
# ````
# 
# ## Try it with Binder
# 
# You can try the interactive periodic table and check the usage through the Binder link:
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/widget-periodictable/develop?urlpath=%2Fvoila%2Frender%2Fexamples%2Fintroduction.ipynb)

# ## Tutorial
# 
# <hr style="border:1px solid gray"> </hr>
# 
# ### **Import the widget**

# In[1]:


import ipywidgets as widgets
from widget_periodictable import PTableWidget
from ipywidgets import Layout


# ### **Initialize and visualize the element grid**
# 
# Here, we initialize the periodic table with three states, which have red, green
# and blue color respectively. The selected elements are C, Si and Ge. The carbon
# is in the 1st state, which has red color. The elements B, Al and Ga are disabled,
# which means they are not clickable. The remaining unselected elements are in pink. The border color of each element is black. The width option is set for
# each element.

# In[4]:


widget = PTableWidget(states = 3, selected_elements = {"C": 0, "Si": 1, "Ge": 2}, 
                      selected_colors = ['red', 'green', 'blue'], 
                      disabled_elements = ['B', 'Al', 'Ga'],
                      unselected_color='pink', border_color = 'black', width = '20px')

display(widget)


# ### **Set the states of the elements**
# 
# The periodic table allows users to customize the states of the selected elements. 
# If one does not specify the selected element's state, it shall default to zero.
# One can initialize the selected elements by using a dictionary.

# In[5]:


widget.selected_elements = {"La": 0, "Ce": 1, "Pr": 2}


# Change or reset the element's state via the `set_element_state` method.
# Note, however, that you cannot use widget.selected_elements["Nd"] = 1 to set the states of the elements for instance.

# In[6]:


widget.set_element_state("Nd",0)


# Get the elements which are in the same state:

# In[7]:


widget.get_elements_by_state(0)


# ### **Get the selected values in python**

# Check which elements are currently selected

# In[8]:


output = widgets.Output()

def on_get_in_python(event):
    output.clear_output()
    with output:
        print(
            "Currently selected values:",  
            widget.selected_elements)

button2 = widgets.Button(
    description="Get the currently selected values", 
    button_style='success',
    layout={'width': '300px'}
)
button2.on_click(on_get_in_python)
vbox = widgets.VBox([button2, output])
vbox


# ### **Play with enabling/disabling some elements**

# In[9]:


toggle_disabled = widgets.Checkbox(
    value="O" in widget.disabled_elements,
    description='Disable oxygen',
    disabled=False
)

def on_change_disabled(event):
    if toggle_disabled.value:
        # It's set, meaning we want to disable oxygen
        widget.disabled_elements = ["O"]
    else:
        widget.disabled_elements = []
toggle_disabled.observe(on_change_disabled, names='value')

def on_change(event):
    """
    Update the toggle value if manually changing the disabled_elements list.
    """
    toggle_disabled.value = "O" in widget.disabled_elements
widget.observe(on_change, names='disabled_elements', type='change')        
        
toggle_disabled


# ### **Freeze (disable clicking events) the whole periodic table**

# In[10]:


toggle_freeze = widgets.Checkbox(
    value= False,
    description='Freeze periodic table:',
    disabled=False
)

def on_freeze_change(event):
    widget.disabled = toggle_freeze.value
    
toggle_freeze.observe(on_freeze_change, names='value')

toggle_freeze


# ### **Set the selected values from python**
# 
# Choose the selected values from python

# In[11]:


def on_set_from_python(event):
    # NOTE! If you put an element which does not exist, it will stay forever in the list, but it's ignored
    widget.selected_elements = {"Li":0, "H":0}

button = widgets.Button(
    description="Select only Li and H (from python)", 
    button_style='success',
    layout={'width': '300px'}
)
button.on_click(on_set_from_python)
button


# ### **Change the displayed string for some elements**
# 
# Note that you should pass valid HTML strings, as they will not be escaped. On the other hand this allows one to use HTML to change the class, color, ...

# In[12]:


def get_noble_gases_state():
    label_deactivate = "Make noble gases bold"
    label_activate = "Make noble gases not bold"
    def deactivate_noble_gases(event):
        widget.display_names_replacements = {}
    def activate_noble_gases(event):
        widget.display_names_replacements = {
            elem_name: "<b>{}</b>".format(elem_name)
            for elem_name in ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']
        }

    if 'He' in widget.display_names_replacements:
        return {
            'is_active': True,
            'toggler_function': deactivate_noble_gases,
            'toggled_label': label_deactivate,
            'current_label': label_activate
        }
    else:
        return {
            'is_active': True,
            'toggler_function': activate_noble_gases,
            'toggled_label': label_activate,
            'current_label': label_deactivate
        }

button_noble = widgets.Button(
    description=get_noble_gases_state()['current_label'], 
    button_style='success',
    layout={'width': '300px'}
)
                
def on_toggle_noble_gases(event):
    """Toggle the state of the button and of the ."""
    state = get_noble_gases_state() 
    # Change the table
    state['toggler_function'](event)
    # Change the button description
    button_noble.description = state['toggled_label']
    
button_noble.on_click(on_toggle_noble_gases)
button_noble

