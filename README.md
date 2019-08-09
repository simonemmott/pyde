# PythonDevelopment

Author Simon Emmott - O698609

## Installation
The json_model module is available in the package 'python_develop' and can be installed using pip
```
pip install python_develop
```

## Description

The python_develop packages provides a Command Line Interface (CLI) `pyde` to standardise python development environments

The `pyde` CLI makes opinionated decisions about how to structure 

## The pyde Command Line Interface
The `pyde` CLI provides facilities for standardising python development environments.
The `pyde` CLI implements help options `--help` for all the commands
To get help on the `pyde` command
```
pyde --help
```

The `pyde` CLI includes the following sub commands:

Sub command             | Description
------------------------|----------------
[about](#about-command) | Show information about the `pyde` command
[init](#init-command)   | Initialise a new development environment

### About Command

The about command output details about the `pyde` CLI

```
pyde about
```

outputs

```
#####################################

A utility for automating and standardising python development environments

Version: 0.0.0

Author:  Simon Emmott

Email:   simon.emmott@yahoo.co.uk

Package: python_developer

URL:     https://github.com/simonemmott/python_developer

#####################################
```

And

```
pyde about --version
```

outputs

```
0.0.0
```

The about command includes the following options
Option    | Description
----------|--------------
--help    | Show help on the about command and exit
--version | Show the version of the `pyde` command

### Init Command

The Init command initialises a new development environment for the given module name
```
pyde init my_module
```

Creates a new module named `my_module` in the current directory.
The new module is initialised with a `__init__.py` file and an `about.py` file.
The `about.py` file contains the details of the module defined by the init command.

If the module directory already exists or the `about.py` already exists then the `about.py` file is updated with the initialisation options.

Unless given through the command options the init command prompts the user for the about values.

The about command includes the following options
Option        | Description
--------------|--------------
--help        | Show help on the about command and exit
--version     | Define the version of the module
--author      | Define the author of the module
--email       | Define the support email of the module
--description | Define the short description of the module
--package     | Define the package which contains the module
--url         | Define the url which documents the module


















