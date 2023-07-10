from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="AutoML_DSNA",
    author="Vestech",
    description="Automate machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enisbaskapan/AutoML_DSNA/edit/main/setup.py",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",)
