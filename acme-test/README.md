# acme-test

This project represents a architecture library (dependency) related with **testing** to develop the different parts in a homogeneus way

This library stands out for:

* Provides utility classes to facilitaty testing with certain elements : exceptions, constant classes, etc.
* Provides tools to control the quality of the projects
* Define unit testing framework and their versioning
* Define mocking testing framework and their versioning
* Define matcher testing framework and their versioning
* Define tools to control the quality of the projects
* Provides utilities for ink and formatting management




## Technological Stack

* [Python](https://www.python.org/)

Dependencies with architecture projects

* N/A

Third Party

* **pipdeptree** [2.1.0] : Command line utility to show dependency tree of packages -> [Pypi](https://pypi.org/project/pipdeptree/) [Documentation](https://github.com/naiquevin/pipdeptree)

  * Includes :
    * pip

* **graphviz** [0.17] : Simple Python interface for Graphviz -> [Pypi](https://pypi.org/search/?q=graphviz) [Documentation](https://github.com/xflr6/graphviz)

* **pytest** [6.2.4] : Framework for use unit testing (with over 850+ external plugins ) -> [Pypi](https://pypi.org/project/pytest/) [Documentation](https://docs.pytest.org/en/latest/)

  * Includes :
    * iniconfig
    * attrs
    * toml
    * pyparsing
    * packaging
    * py

* **pytest-xdist** [2.3.0] : pytest plugin for execution modes : parallelization, multi-platform, etc. -> [Pypi](https://pypi.org/project/pytest-cov/) [Documentation](https://github.com/pytest-dev/pytest-cov)

  * Includes :
    * execnet
    * pytest
    * pytest-forked

* **pytest-cov** [2.12.1] : pytest plugin for create reports -> [Pypi](https://pypi.org/project/pytest-cov/) [Documentation](https://github.com/pytest-dev/pytest-cov)

  * Includes :
    * coverage
    * pytest
    * toml

* **pytest-flake8** [1.0.7] : Framework that is a plugin to check FLAKE8 requirements -> [Pypi](https://pypi.org/project/pytest-flake8/) [Documentation](https://flake8.pycqa.org/en/latest/index.html#quickstart)
  
  * Includes :
    * **flake8** [3.9.2] : Framework that is a wrapper of differentes tools -> [Pypi](https://pypi.org/project/flake8/) [Documentation](https://flake8.pycqa.org/en/latest/index.html#quickstart)
    * **pycodestyle** [2.7.0] : Framework for checking Python style guide -> [Pypi](https://pypi.org/project/pycodestyle/) [Documentation](https://www.python.org/dev/peps/pep-0008/)
    * **pyflakes** [2.3.1] : Framework for checking Python error about source files -> [Pypi](https://pypi.org/project/pyflakes/) [Documentation](https://github.com/PyCQA/pyflakes)
    * **mccabe** [0.6.1] : Framework for checking Python with McCabe complexity -> [Pypi](https://pypi.org/project/mccabe/) [Documentation](https://github.com/pycqa/mccabe)
    * Supports storing its configuration in the following places :setup.cfg, tox.ini, or .flake8 (Flake8 looks for ~\.flake8 on Windows and ~/.config/flake8 on Linux and other Unix systems)

* **pytest-mock** [3.6.1] : Thin-wrapper around the mock package for easier use with pytest -> [Pypi](https://pypi.org/project/pytest-mock/) [Documentation](https://github.com/pytest-dev/pytest-mock/)

  * Includes :
    * pytest

* **pytest-cases** [3.6.3] : Separate test code from test cases in pytest -> [Pypi](https://pypi.org/project/pytest-cases/) [Documentation](https://github.com/smarie/python-pytest-cases/)

  * Includes :
    * decopatch
    * makefun

* **pytest-asyncio** [0.15.1] : Pytest support for asyncio -> [Pypi](https://pypi.org/project/pytest-asyncio/) [Documentation](https://github.com/pytest-dev/pytest-asyncio)

  * Includes :
    * pytest

* **pylint** [2.10.2] : Framework checking programming errors, coding starndar, code smells, etc. -> [Pypi](https://pypi.org/project/pylint/) [Documentation](https://github.com/PyCQA/pylint) [Documentation2](http://pylint.pycqa.org/en/latest/)

  * Includes :
    * astroid
    * isort
    * mccabe
    * platformdirs
    * toml

* **black** [21.8b0] : Framework for code formatter -> [Pypi](https://pypi.org/project/black/) [Documentation](https://github.com/psf/black)

  * Includes :
    * click
    * mypy-extensions
    * pathspec
    * platformdirs
    * regex
    * tomli
    * typing-extensions

* **Sphinx** [4.1.2] : Framework checking programming errors, coding starndar, code smells, etc. -> [Pypi](https://pypi.org/project/pylint/) [Documentation](https://github.com/PyCQA/pylint) [Documentation2](http://pylint.pycqa.org/en/latest/)

  * Includes :
    * alabaster
    * babel
    * docutils
    * imagesize
    * Jinja2
    * packaging
    * Pygments
    * requests
    * setuptools
    * snowballstemmer
    * sphinxcontrib-applehelp
    * sphinxcontrib-devhelp
    * sphinxcontrib-htmlhelp
    * sphinxcontrib-jsmath
    * sphinxcontrib-qthelp
    * sphinxcontrib-serializinghtml

* **pre-commit** [2.14.0] : Framework for managing and maintaining multi-language pre-commit hooks -> [Pypi](https://pypi.org/project/pre-commit/) [Documentation](https://pre-commit.com/)


