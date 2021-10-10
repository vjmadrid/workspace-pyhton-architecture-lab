#
# Makefile for Project Management
#  

SHELL = /bin/bash
.DEFAULT_GOAL := help
VIRTUAL_ENV_NAME := venv-local



# *** GENERAL ***

upgrade: ## Upgrade Python modules : pip and setuptools
	@pip install -U pip setuptools wheel



# *** Virtual Environment ***

venv-local-init: ## Init virtual environment
	@python3 -m venv $(VIRTUAL_ENV_NAME)
	@echo -e "Execute to activate : source $(VIRTUAL_ENV_NAME)/bin/activate"
	@echo -e "Execute to deactivate : source deactivate"


venv-local-del: ## Delete virtual environment
	@rm -rf ./$(VIRTUAL_ENV_NAME)


venv-local-prepare: ## Prepare virtual environment
	@make upgrade
	@make deps-install-dev



# *** DEPENDENCIES ***

deps-install-dev: ## Install dependencies 'dev-requirements.txt' file (No versions)
	@pip install -Ur dev-requirements.txt
	@make deps-generate-requirements

deps-generate-requirements: ## Generate 'requirements-version.txt' file (With versions)
	@pip freeze | grep -v -- '^-e' > requirements.txt

deps-install: ## Install dependencies 'requirements.txt' file (With versions)
	@pip install -Ur requirements.txt

deps-tree: ## Show dependency tree of packages
	pipdeptree

deps-tree-json: ## Show dependency tree of packages json
	pipdeptree --json-tree

deps-tree-graph: ## Show dependency tree of packages graph
	pipdeptree --graph-output png > dependencies.png

deps-reset: ## Reset all requirements
	pip freeze | xargs pip uninstall -y



# *** QA ****

check-lint: ## Check lint and static code
	flake8 --version
	flake8 .
	pylint --version
	pylint src
	pylint tests

check-format: ## Check format code
	black . --check --color --diff

check-format-apply: ## Apply format code
	black .

check-security: ## Check security code
	bandit -r .



# *** TEST ***

test: clean ## Run all the tests with all the supported python interpreters 
	pytest -ra

test-lint: ## Lint and static-check code
	pytest --cache-clear --flake8

test-coverage: ## Run tests with coverage
	coverage erase
	coverage run --include=src/* -m pytest -ra
	coverage report -m
	coverage html


# *** DOCS ***

docu: ## Documentation
	@echo "Build Doc"
	cd ./docs/sphinx && make html

docs: ## Create the documentation
	echo "Build completed"
	



# *** ALLURE ***
allure-reports: ## Create Allure reports
	pytest --alluredir=reports
	



# *** INSTALL / UNINSTALL ***

install: clean uninstall ## Install package local
	python3 setup.py develop

uninstall: ## Uninstall package local
	python3 setup.py develop --uninstall

install-site: clean ## Install the package to the active Python's site-packages
	python3 setup.py install



# *** DISTRIBUTE ***

dist-package-install: ## Distribute package install
	pip install -Ue .

dist-install: ## Distribute package install by setup.py
	python3 setup.py install

dist-sdist: ## Distribute package mode local (folder : sdist)
	python3 setup.py sdist

dist-wheel: ## Distribute package mode local (folder : sdist)
	python3 setup.py bdist_wheel
	
dist: clean dist-sdist dist-wheel ## Distribute source and wheel package



# *** CLEAN ***

clean-build: ## Remove elements for build
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pyc' -type d | xargs rm -fr

clean-test: ## Remove test and coverage artifacts
	@rm -fr .tox/
	@rm -fr .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

clean-pyc: ## Remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-distribute: ## Remove *.egg-info files and *.egg, build and dist directories
	@rm -vrf build/ 
	@rm -vrf dist/ 
	@rm -vrf ./*.tgz 
	@rm -vrf .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +


clean : clean-build clean-pyc clean-test clean-distribute  ## Remove all build, test, coverage and distribute Python artifacts



# *** BUILD ***

build: ## Build
	make clean
	make deps-install-
	make lint
	make test
	make docs
	make install-develop
	@echo "Build completed"



# *** RUN ***

run: ## Run
	N/A



# *** UPLOAD ****
upload: ## Upload
	python3 setup.py 
	@echo "Upload completed"


# *** HELP ***

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [target]"; \
	printf "%-40s %s\n" "target" "help" ; \
	printf "%-40s %s\n" "----------------------------------" "----------------------------------" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-40s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
	@echo "Check the Makefile to know exactly what each target is doing"


.PHONY: init test