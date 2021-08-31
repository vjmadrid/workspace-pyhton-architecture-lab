mkdir amce-project
$ cd amce-project
$ python3 -m venv env
$ . env/bin/activate

Generate .gitignore

.
├── .gitignore
└── podsearch
    └── __init__.py

"""Let's find some podcasts!"""

 __version__ = "0.1.0"


 def search(name, count=5):
     """Search podcast by name."""
     raise NotImplementedError()

# flit

pip install flit

pip install flit

pyproject.toml

Flit has created pyproject.toml - the project metadata file. It already has everything you need to publish the package to the public repository - PyPI.

Sign up for TestPyPi (test repository) and PyPI (the main one). They are completely independent, so you will need two accounts.

Setup access to repositories in the ~/.pypirc:

[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username: nalgeon  # replace with your PyPI username

[pypitest]
repository: https://test.pypi.org/legacy/
username: nalgeon  # replace with your TestPyPI username



