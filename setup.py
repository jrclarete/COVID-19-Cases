from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


def install_requires():
    with open('requirements.txt') as f:
        INSTALL_REQ = f.read().splitlines()
    return INSTALL_REQ


setup(
    name="COVID-19-Cases",
    version="0.0.1",
    description="A python script that generates latest data set of COVID-19 cases around the globe.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/jrclarete/COVID-19-Cases",
    author="Jhon Rommel Clarete",
    author_email="rommel.clarete18@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["covid19cases"],
    include_package_data=True,
    install_requires=install_requires(),
)
