# Template project 
A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for 
conda packages using Python
 Customized for use with my projects

## Features

 - Automatic versioning with versioneer (requires git annotated tags before it'll work)
 - Ready-made conda recipe found in conda.recipe/meta.yaml
 - Coverage report hosted on Codecov.io (activated after first successful CI run, which uploads results)
 - setup.cfg with flake8 opinions and pytest/pytest-cov configuration (including fixed PYTHONHASHSEED)

## Installation

Prior to installing cookiecutter-conda-python, the cookiecutter package must be installed in your environment. This is achieved via the following command::

    $ conda install cookiecutter

With cookiecutter installed, the cookiecutter-conda-python template can be installed with::

    $ cookiecutter https://github.com/dwr-psandhu/cookiecutter-conda-python

Once cookiecutter clones the template, you will be asked a series of questions related to your project::

    $ full_name [Full Name]: Enter your full name.

    $ email [Email Address]: Enter your email address.

    $ github_username [github_username]: Enter your github username.

    $ repo_name [repository_name]: Enter the name of your project's repository.

    $ package_name [package_name]: Enter the name of your package.

    $ application_name [application]: Enter the name of your GUI application.

    $ project_short_description [Short description]: Enter a short description about your project.


## Usage

After answering the questions asked during installation, a conda Python package will be
created in your current working directory. This package will contain a simple CLI script
and the conda recipe necessary to build the application into a conda package.

You'll still need to activate the web services you want to use - they won't be active automatically.

 - __Codecov__: No configuration necessary - project will be created when first successful CI run completes and uploads coverage results
