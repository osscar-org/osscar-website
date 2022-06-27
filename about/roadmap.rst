###################################
Roadmap
###################################

Goals 
-------

In the OSSCAR (Open Software Services for Classrooms and Research) project, we
developed tools and materials for computational chemistry and computational
physics research and education. We are mainly focusing on four different
sections.

1. Develop custom advanced visualizations web applications for education.
2. Jupyter custom widgets for computational chemistry and computational physics.
3. JupyterLab extensions and tools for research and development.
4. Offer documents and tutorials to developers to use the OSSCAR technologies.

Timeline
---------

.. image:: images/osscar-timeline.png
  :width: 600
  :alt: osscar timeline
  :align: center

OSSCAR project started from October, 2019. During the 1st year (2019-2020), we
were focusing on developing components for the framework of the OSSCAR web
applications. We were trying several different tools such as appmode_ for
rendering the notebooks and Jmol_ for the molecular visualization. However, we
chose the Voila_ program to render the interactive notebooks into web apps. We
developed OSSCAR style template (`voila-osscar-template`_)for the Voila web
apps. 

In the 2nd year (2020-2021), we were starting developing interactive notebooks
for computational chemistry and computational physics education. We developed
several interactive notebooks for quantum mechanics education. We were using the
free cloud server `mybinder.org`_ to deliver the notebooks as web apps. The
proof of concept of web apps turn to work well. However, we also found there
were some major drawback using the mybinder server, which the loading process
was very slow. We were also starting to develop custom Jupyter widgets for 
computational chemistry and computational physics, like the
`widget-periodictable`_ (a interactive periodic table as Jupyter widget).

In the 3rd year (2021-2022), we were developing several custom Jupyter widgets
for computational chemistry and physics, like `widget-bzvisualizer`_ (a Jupyter
widget to visualize the 1st Brillouin zone and band path), `widget-bandsplot`_
(a widget to plot bandstructure and density of states), `widget-code-input`_ (a
widget to allow users to define Python function interactively). We created a
collection of interactive and educational web apps for quantum mechanics and
computational materials science, which contains sections such as "quantum
mechanics", "band theory", "statistical mechanics" and "molecular dynamics".  We
set up two dokku_ servers under Materials Cloud project at Swiss supercomputing
infrastructure at CSCS_. Our web apps have been deployed on dokku servers with 
lower latency.

In the 4th year (2022-2023), we are planning to make more high quality
interactive web apps and introduce new technologies for interaction. We are
going to present and promote OSSCAR project in conferences and workshops.  We
will encourage more people both from EPFL and outside to contribute and use
OSSCAR web apps and technologies. We are aiming to introduce OSSCAR project to
world's top universities' classrooms (such Harvard and MIT). 

Milestone
----------

.. _appmode: https://github.com/oschuett/appmode
.. _Jmol: http://jmol.sourceforge.net
.. _Voila: https://github.com/voila-dashboards/voila
.. _voila-osscar-template: https://github.com/osscar-org/voila-osscar-template
.. _mybinder.org: https://mybinder.org
.. _widget-periodictable: https://github.com/osscar-org/widget-periodictable
.. _widget-bzvisualizer: https://github.com/osscar-org/widget-bzvisualizer
.. _widget-bandsplot: https://github.com/osscar-org/widget-bandsplot
.. _widget-code-input: https://github.com/osscar-org/widget-code-input
.. _dokku: https://dokku.com
.. _CSCS: https://www.cscs.ch






