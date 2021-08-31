from setuptools import setup, find_packages

setup(
    name="acme-core",
    version="0.1",
    description="xxx",
    author="xxx",
    author_email="xxx",
    url="xxx",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    scripts=[],
    test_suite="tests"
)
