NOTE: It's not a huge deal if you can't get this to work, you don't actually need either library for the lecture breakouts or assignment. Just don't run any code in the notebook.

### Step 1:  
Install networkx version 2.3 (nxpd doesn't work with 2.4) in conda.  
`$ conda install networkx=2.3 -c https://conda.anaconda.org/conda-forge/`  

If that worked, great and move on to step 2. If it gets stuck trying to solve the environment, instead try:  

`$ pip uninstall networkx`  
`$ pip install networkx==2.3`  

(or just that second line if the first lines like "You didn't have networkx")

### Step 2:
Install the graph visualization library used in this notebook:  

`$ pip install nxpd`  

NEW: And its dependencies:  
  
Mac OS: `brew install graphviz`  
Linux: `sudo apt-get install graphviz`  

### Step 3:
To confirm your installation, run:  

`$ python nxpd_test.py`  

This should output a simple graph if successful (or at least not throw an error)
