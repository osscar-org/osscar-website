#!/usr/bin/env python
# coding: utf-8

# # `widget-bzvisualizer`: A Jupyter widget to visualize the 1st Brillouin zone and band paths
# 
# **Introduction**: A Jupyter widget to plot the 1st Brillouin zone and band paths. 
# It uses the Javascript package [tools-seekpath](https://seekpath.readthedocs.io) developed 
# by Materials Cloud.

# ## 1. Import the widget from the package

# In[1]:


from widget_bzvisualizer import BZVisualizer
import numpy as np
from ase.dft.kpoints import *


# ## 2. Initialize the parameters for the widget
# 
# * cell: the cell vectors a, b, c
# * positions: the coordinates of the atoms
# * elements: the elements of the atoms in an array

# In[ ]:


lattice = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

w = BZVisualizer(lattice, [[0.0, 0.0, 0.0]], [1], True)
display(w)


# ```{image} ./images/widget_bzvisualizer.png
# :alt: image periodictable
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```

# ### One can also change the kpoints coordinates in the widget

# In[ ]:


w.kpts = (monkhorst_pack((8, 8, 8))*2*np.pi).tolist()


# In[ ]:




