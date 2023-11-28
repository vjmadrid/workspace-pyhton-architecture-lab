import io
import os
# import sys

# from shutil import rmtree
# from setuptools import setup, find_packages, Command
from setuptools import setup, find_packages

from configs.default import BASE_DIR


print("BASE_DIR: "+str(BASE_DIR))


# Package meta-data default values
NAME = "architecture-test"
DESCRIPTION = "Architecture library (dependency) related with testing to develop the different parts in \
    a homogeneus way"
URL = "https://github.com/vjmadrid/workspace-python-architecture-lab/tree/main/" + str(NAME)
EMAIL = "vjmadrid"
AUTHOR = "Víctor Madrid"
REQUIRES_PYTHON = ">=3.11.0"
VERSION = "0.0.1"
PACKAGES_EXCLUDE = ["tests", "*.tests", "*.tests.*", "tests.*", "docs", "examples"]
REQUIREMENTS_FILE = "dev-requirements.txt"


# Prepare info dictionary
info_dict = {}

# Load version -> the package's __version__.py module as a info dictionary
# project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
# with open(os.path.join(path, project_slug, "__version__.py")) as f:
with open(os.path.join(BASE_DIR, '__version__.py')) as f:
    exec(f.read(), info_dict)

print("VERSION: "+str(info_dict['__version__']))



# Load README.md
try:
    with io.open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8") as f:
        info_dict["long_description"] = "\n" + f.read()
except FileNotFoundError:
    info_dict["long_description"] = DESCRIPTION


# Load LICENSE
with open("LICENSE") as f:
    info_dict["license"] = f.read()


# Load Packages required
REQUIRED_DEFAULT = [
    # N/A
]

# Load Package optional
EXTRAS_DEFAULT = {
    # N/A
}


# class UploadCommand(Command):
#     """Support setup.py upload"""

#     description = "Build and publish the package"
#     user_options = []

#     @staticmethod
#     def status(s):
#         """Prints things in bold"""
#         print("\033[1m{0}\033[0m".format(s))

#     def initialize_options(self):
#         pass

#     def finalize_options(self):
#         pass

#     def run(self):
#         try:
#             self.status("Removing previous builds ...")
#             rmtree(os.path.join(path, "dist"))
#         except OSError:
#             pass

#         self.status("Building Source and Wheel (universal) distribution…")
#         os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

#         # self.status('Uploading the package to PyPI via Twine…')
#         # os.system('twine upload dist/*')

#         self.status("Pushing git tags…")
#         os.system("git tag v{0}".format(info_dict['__version__']))
#         os.system("git push --tags")

#         sys.exit()


setup(
    python_requires=REQUIRES_PYTHON,
    name=NAME,
    version=info_dict['__version__'],
    description=DESCRIPTION,
    long_description=info_dict['long_description'],
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    license=info_dict["license"],
    url=URL,
    package_dir={'': 'src'},
    packages=find_packages("src", exclude=PACKAGES_EXCLUDE),
    install_requires=[i.strip() for i in open(REQUIREMENTS_FILE).readlines()],
    extras_require=EXTRAS_DEFAULT,
    include_package_data=True,
    scripts=[],
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: Python",
    ]
    # $ setup.py publish support
    # cmdclass={
    #    'upload': UploadCommand,
    # },
)
