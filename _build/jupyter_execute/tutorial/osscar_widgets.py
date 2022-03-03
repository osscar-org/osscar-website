#!/usr/bin/env python
# coding: utf-8

# # **A simple web application with nglview and periodic table widget**
# 
# In this notebook, we give a more complex example, which is more directly related to computational chemistry and physics.
# We are going to use the atomic simulation environment (ASE) package to build molecular structure. Then the 
# three-dimensional geometrical structure of the selected molecule will be shown in the NGL visualizer.
# The elements of the molecule will be highlighted in the interactive periodic table.

# ## 1. Import pacakges
# 
# * We import the `Textarea` widget from "ipywidgets". We use it enable users to input the name of the molecule they wish to visualize.
# * Atomic simulation environment (ASE) is a python package, which contains a variety of functions and tools for computational chemistry and physics. Here, we import the molecule function, which has the geometry data for some popular molecules.
# * NGLview is a powerful molecular visualizer. Here we are using it to visualize the molecular structure.
# * We are using the interactive periodic table to highlight the elements of the molecules. This widget is developed under the OSSCAR project.

# In[1]:


from ipywidgets import HBox, VBox, Textarea, Button, Layout
from ase.build import molecule
import nglview as nv
from widget_periodictable import PTableWidget


# ## 2. Initialize a default molecule
# 
# Initialize the Fullerene (C60) as the default molecule and show it in the visualizer.

# In[ ]:


#Initialize the fullerene molecule 
aa = molecule("C60")

#Set the cell parameters and periodic boundary condition
aa.set_cell([[15, 0, 0], [0, 15, 0], [0, 0, 15]])
aa.center()
aa.pbc=True

#Show the fullerene in the NGL visualizer
view = nv.show_ase(aa)
view.add_unitcell()
view.control.zoom(0.2)
view.add_ball_and_stick(aspectRatio=4)
view.camera='perspective'


# ## 3. Deploy a textarea for the input of the molecule name
# 
# Use the `Textarea` widget from the "ipywidgets" package.

# In[ ]:


w = Textarea(
    value='C60',
    placeholder='Type your molecule',
    description='Molecule:',
    disabled=False,
    layout=Layout(width='28%', height='27px')
)


# ## 4. Deploy the interactive periodic table

# In[ ]:


PTable = PTableWidget(states=1, selected_colors = ['red'], selected_elements = {'C':0})


# ## 5. Define the callback function for the button click event
# 
# Here, we deploy an "Update" button, which reads the name of the molecule from the textarea and updates the
# structure in the visualizer and highlighted elements in the periodic table.

# In[ ]:


def on_button_click(b):
    global view
    aa = molecule(w.value)
    aa.set_cell([[15, 0, 0], [0, 15, 0], [0, 0, 15]])
    aa.center()
    aa.pbc=True
    for comp_id in view._ngl_component_ids:
        view.remove_component(comp_id)
    view.add_component(nv.ASEStructure(aa))
    view.clear()
    view.add_ball_and_stick(aspectRatio=4)
    view.add_unitcell()
    view.control.zoom(0.2)
    PTable.selected_elements = {key: 0 for key in list(dict.fromkeys(aa.get_chemical_symbols()))}
    
b = Button(description = 'Update')
b.on_click(on_button_click)


# ## 6. Display the widgets
# 
# Display all the widgets and arrange them in a nice layout.

# In[ ]:


display(HBox([w, b]), VBox([view, PTable]))


# In[ ]:




