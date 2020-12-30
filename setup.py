from setuptools import find_packages, setup

PROJECT_NAME = 'MY_PROJECT'

with open("README.md", "r") as fh:
  long_description = fh.read()

packages = find_packages()
packages.remove('mmmm_cookies.tests')

setup(
    name="%s_mmmm_cookies" % PROJECT_NAME,
    version="0.0.1",
    author="Niall Byrne",
    author_email="niall@niallbyrne.ca",
    description="Not the evil tracking type.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/false/mmmm_cookies",
    packages=packages,
    install_requires=[],
    license="License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.0,<3.8.0',
)
