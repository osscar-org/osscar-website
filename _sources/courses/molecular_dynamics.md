# **Molecular Dynamics**

## 1. [Verlet Integration](https://github.com/osscar-org/quantum-mechanics/blob/develop/notebook/molecular-dynamics/verlet_integration.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/quantum-mechanics/develop?urlpath=%2Fvoila%2Frender%2Fnotebook%2Fmolecular_dynamics%2Fverlet_integration.ipynb)
[![Materials Cloud Tool osscar-qmcourse](https://raw.githubusercontent.com/materialscloud-org/mcloud-badge/main/badges/img/mcloud_badge_tools.svg)](https://osscar-quantum-mechanics.matcloud.xyz/voila/render/molecular-dynamics/verlet_integration.ipynb)

In the classic molecular dynamics simulations, the molecular motions are
computed by solving the Newton equation. The numerical approximation is
employed, which treats the velocities of the atoms as constant during a tiny
period Δt. A numerical aglorithm called verlet integration is employed to update
the positions, velocities and accelerations of the simulated systems. Here, we
used a two-body system (sun and earth) to demonstrate this numerical method.

```{image} ./images/verlet_integration.png
:alt: verlet integration
:class: bg-primary mb-1
:width: 500px
:align: center
```
