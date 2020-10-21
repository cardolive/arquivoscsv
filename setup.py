from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="arquivoscsv",
    version="0.1.0",
    description="read csv files and populate a db",
    packages=find_packages(),
    include_packages_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
