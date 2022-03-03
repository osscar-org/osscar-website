#!/usr/bin/env python
# coding: utf-8

# # **Using Voila to convert Jupyter notebooks into web application**

# ## 1. Introduction to Voila
# 
# Volia is a program used to convert Jupyter notebooks into standalone web applications which can be shared with others. Voila supports interactive widgets provided by the ipywidgets package, which
# is largely used in the OSSCAR project.
# 
# 
# The purpose of the Voila program is to render the selected notebook and enable real-time interaction with the included widgets.

# ## 2. Run Voila and Deploy a Web Application
# 
# ### **a. Run Voila locally**
# 
# Voila can be deployed via a variety of platforms. Primarily, one can access the web pages locally by connecting to a "port" provided by all computers which allows such local hosting of web pages. 
# The default port number is 8866. One can specify the port number with "--port". There are two ways
# to use Voila locally.
# 
# - Run Voila as a Jupyter server extension:
# 
#     One can access the web apps through the Jupyter server extension by inserting
#     "/voila/render/" after the Jupyter base URL and before the notebook path:
# 
# ```bash
# localhost:8888/voila/render/your_notebook.ipynb
# ```
# 
# - Run Voila as standalone application:
# 
#     One can also run Voila as a standalone application through the terminal: 
# 
# ```bash
# voila --template=osscar --enable_nbextensions=True your_notebook.ipynb
# ```

# ### **b. Deploying with Binder (mybinder.org)**
# 
# Binder (mybinder.org) offers free cloud computing services to deploy Jupyter applications.
# We can deploy the web applications with Voila by calling the Voila server extension. 
# One can follow the steps as listed below:
# 
# - In order to use Voila, one needs to first install the Voila python package. For the binder cloud deployment path, 
# put the package name "voila" in the requirements.txt file. 
# - The voila Jupyter server extension is specified by prepending "<strong>voila/render</strong>" to the path of your Jupyter notebook.
# 
# Provide the URL to mybinder.org as shown below:
# 
# ![voila](./images/fig_binderVoila.png)

# ### **c. Deploying on a dokku server**
# 
# The disadvantage of using Binder is that the allocated cloud computing power is very limited and
# loading can take long time. Alternatively, we can deploy the apps on dokku servers.
# Dokku is a open source platform as a service, which supports voila deployment as
# web applications. One can set up their own dokku servers. Otherwise, there is a 
# dokku server maintained by the Materials Cloud team. Here is the link for instructions on how to deploy 
# a new tool at Materials Cloud.
# 
# https://github.com/materialscloud-org/issues/wiki/Contributing-a-new-tool
# 
# For deploying apps with Voila for a single notebook, we need set the Procfile file as:
# 
# ```bash
# web: voila —-port=$PORT —-no-browser your_notebook.ipynb
# ```
# 
# For multiple notebooks, one can put them in a folder and use Voila to host the 
# whole folder as:
# 
# ```bash
# web: voila —-port=$PORT —-no-browser your_folder/
# ```
# 
# In order to save the computing resources and prevent idling kernels, one
# can set the timeout to kill idle kernels as:
# 
# ```bash
# web: voila —-port=$PORT —-no-browser your_notebook.ipynb --MappingKernelManager.cull_interval=60 --MappingKernelManager.cull_idle_timeout=120
# ```

# ## 3. Use the OSSCAR Voila template

# We developed a Voila template (<strong>voila-osscar-template</strong>) 
# for the OSSCAR project. The template has been released with PyPi. 
# One can install it locally with pip:
# 
# ```python
# pip install voila-osscar-template
# ```
# For delopying with Binder and Dokku platforms,
# One needs to put the "voila-osscar-template" into the <strong>requriments.txt</strong> file. 
# For Binder, one also needs to specify the <strong>jupyter_config.json</strong> file in the GitHub 
# repository. The content of this file is shown below:
# 
# ```bash
# {
#   "VoilaConfiguration": {
#     "enable_nbextensions": true,  
#     "theme": "light",
#     "template": "osscar"
#   }
# }
# ```
# 
# Normally, we need to set the <strong>enable_nbextenions: true</strong> for 
# using custom widgets like the "widget-periodictable". The <strong>theme</strong> 
# has two options, <strong>light</strong> and <strong>dark</strong>.
# 
# For dokku, we can modify the Procfile file as:
# 
# ```bash
# web: voila --template=osscar --VoilaConfiguration.enable_nbextensions=True --port=$PORT --no-browser your_notebook.ipynb
# ```
# 
# For multiple notebooks, this template (special feature) will redirect the starting page
# from "index.ipynb". One can create the "index.ipynb" file to link all
# other notebooks. The relevant input to the dokku Procfile is shown below:
# 
# ```bash
# web: voila --template=osscar --VoilaConfiguration.enable_nbextensions=True --port=$PORT --no-browser your_folder/
# ```

# In[ ]:




