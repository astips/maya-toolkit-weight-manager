# maya-toolkit-weight-manager

---
![Example UI](docs/images/gui.png)

Maya toolkit used to export / import skin weights.  

---

#### SUPPORT

* Poly Mesh  
* Nurbs Surface
* Nurbs Curve
* Lattice


#### INSTALLATION

* Most of the development we are currently doing is in Windows, so all instructions will be given assuming that platform.

1. Download the latest release and unzip the folder where you want to live.
2. Copy folder "tk_weight_manager" to `%USERPROFILE%\Documents\maya\2016\scripts` (or the 2017 folder if you're using 2017)
3. Run these two commands in Python to start the tool.

```python
from tk_weight_manager import startup
startup.show_manager()  
```

```python
from tk_weight_manager import startup
startup.show_toolkits() 
```