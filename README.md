# CareerAI
CareerAI's repositiory for the job parsing daemon, model calling, and application submission

## Getting Started
### Setting up a virtual environment
The first thing to do with Python projects is to establish a venv for CareerAI to install dependencies. This has numerous benefits that can be explored, but we will just move onto setting up and working in a venv. Navigating to the terminal and running the following command activates the venv:

mac/Linux:
```bash
source env/bin/activate
```
Windows:
```bash
env\Scripts\activate
```

### Installing Depdendencies
We now need to install the libraries that will be used by CareerAI. These are open-source projects that perform specific functions, and they will be installed in the venv using the following command:
```bash
pip install -r requirements.txt
```


### Contributing (for devs)
## Initializing dependencies in requirements.txt
To store all the dependencies in one file for an easy user download, we use the pipreqs library.

Firstly install the pipreqs library:
```bash
pip install pipreqs
```
Then utilize the following command after writing a contribution that imports a new dependency:
```bash
python -m pipreqs.pipreqs [folder to be added, use '.' for all] --force
```
