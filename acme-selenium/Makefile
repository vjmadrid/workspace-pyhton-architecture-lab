.DEFAULT_GOAL := help

# *** GENERAL ***

upgrade: ## Upgrade Python modules : pip and setuptools
	pip install -U pip setuptools wheel



# *** DEPENDENCIES ***

deps-install-dev: ## Install dependencies 'dev-requirements.txt' file (No versions)
	pip install -Ur dev-requirements.txt
	make deps-generate-requirements

deps-generate-requirements: ## Generate 'requirements-version.txt' file (With versions)
	pip freeze | grep -v -- '^-e' > requirements.txt

deps-install: ## Install dependencies 'requirements.txt' file (With versions)
	pip install -Ur requirements.txt

deps-reset: ## Reset all requirements
	pip freeze | xargs pip uninstall -y



# *** TEST ***

test: ## Run all the tests with all the supported python interpreters 
	python3 -m pytest -ra
	make clean

coverage: ## Run tests with coverage
	python3 -m coverage erase
	python3 -m coverage run --include=src/* -m pytest -ra
	python3 -m coverage report -m

lint: ## Lint and static-check
	flake8 --version
	flake8 .
	pylint --version
	pylint acmeselenium
	pylint tests



# *** DISTRIBUTE ***

distribute-package-install: ## Distribute package install
	pip install -Ue .

distribute-install-develop: distribute-uninstall-develop ## Distribute package install mode develop
	python3 setup.py develop

distribute-uninstall-develop: ## Distribute package uninstall mode develop
	python3 setup.py develop --uninstall

distribute-install: ## Distribute package install by setup.py
	python3 setup.py install

distribute-local: ## Distribute package mode local (folder : sdist)
	python3 setup.py sdist

show-content:
	cp ./dist/acme-common-0.0.1.tar.gz ../


# *** CLEAN ***

clean-build: ## Remove elements for build
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '.pytest_cache' -type d | xargs rm -fr
	find . -name '*.pytest_cache' -type d | xargs rm -fr
	find . -name '*.pyc' -type d | xargs rm -fr

clean-distribute: clean-build ## Remove *.egg-info files and *.egg, build and dist directories
	rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./*.egg
	find . -name '*.egg-info/' -type d | xargs rm -fr

clean : clean-distribute ## Remove *.pyc files and __pycache__ directory


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