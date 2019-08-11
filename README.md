# PythonDevelopment

Author Simon Emmott - O698609

## Installation
The python_dev module is available in the package 'python_develop' and can be installed using pip
```
pip install python_develop
```

## Description

The python_develop packages provides a Command Line Interface (CLI) `pyde` to standardise python development environments

The `pyde` CLI makes opinionated decisions about how to structure python development projects.

The `pyde` CLI uses jinja2 templates to generate source code in your development environment.

The jinja2 templates are located in the package pyhton_dev.jinja2.templates.

Access to the jinja2 environment is available from `python_dev.jinja2.env` 

The `pyde` CLI examines your development environment and extracts [metadata](.docs/metadata.md) from the found python modules. This meta data is passed to the jinja2 templates as the variable `meta`.

## See Also

Title                         | Description
------------------------------|-------------------------------------
[Metadata](.docs/metadata.md) | The definition of the mata data extracted from your development environment
[Inclusions](.docs/inclusions.md) | Details on the `pyde include` command.
[Configuring Inclusions](.docs/configuring_inclusions.md) | Details on how to define custom inclusions.

## The pyde Command Line Interface
The `pyde` CLI provides facilities for standardising python development environments.
By default the `pyde` CLI works on modules in the current working directory. This can be changed with the `--target` option

The `pyde` CLI implements help options `--help` for all the commands
To get help on the `pyde` command

```
pyde --help
```

or

```
pyde <command> --help
```

The `pyde` CLI includes the following options:

Option    | Description
----------|--------------
--help    | Show help on the about command and exit
--target  | Set the directory that the `pyde` command should update



The `pyde` CLI includes the following sub commands:

Sub command             | Description
------------------------|----------------
[about](#about-command) | Show information about the `pyde` command
[init](#init-command)   | Initialise a new development environment
[include](.docs/inclusions.md)   | Initialise a new development environment

### About Command

The `about` command outputs details about the `pyde` CLI

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

The `init` command initialises a new development environment for the given module name
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
















