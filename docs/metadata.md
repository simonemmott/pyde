# Metadata

The pyde CLI extracts meta data from your development environment.

pyde assumes that you have a single root module. You may have other modules in the root of your development environment but only one 'root module'. The root module is identifies by the presence of an `about.py` module in the root module. the behaviour of `pyde` is undefined if you have more than one module in the root of you development environment with an `about.py`.

The extracted meta data is available via `python_dev.pyde.meta`.

## Meta Class

The instance of `python_dev.Meta` class at `python_dev.pyde.meta` holds the identified meta data and has the following structure.

Attribute   | Data Type | Description
------------|-----------|------------------------------
root_module | Module | The metadata of the root module
modules     | [Module] | A list of Module instances holding the metadata of all the modules found in the development environment including the `root_module`.
about       | About | The data extracted from `about.py`
includes    | [str] | A list of the names of the included modules.
name        | str   | The name of the module taken from the name of the root module `meta.root_module.name`
api         | OpenApi   | The data from the defined Open API JSON document 

### Methods

Method      | Description
------------|-------------------------
module(...) | This method takes a single str argument and returns the Module instance for named module.

#### Method module(name)

The module method takes the name of a module in the devlopment environment and returns the instance of Module which describes the meta data of the module.

Parameter | Description
----------|----------------------------
name      | The name of the module to return.

**Returns**: The meta data of the named module

Throws     | Condition
-----------|-----------------
ValueError | If the named module is not defined in the local development environement

## About Class

An instance of the about class is populated with data extracted from the `about.py` module in the `root_module` of the development environemnt.

The `about.py` module documents details about your module and is used to populate details in `setup.py` used to build the distribution of your module.

By default the `about.py` module is expected to define values for

1. The package name in the attribute `package`
1. The package version in the attribure `version`
1. The name of the author of the package in the attribure `author`
1. The support email for the package in the attribute `author_email`
1. The short description of the package in the attribute `description`
1. The documentation url of the package in the attribute `url`

These attributes are used to set the attributes of the same name in `setup.py` for module deployment.

In addition to the above attributes you can add additional attributes to `about.py` and the values of these attributes will be available in the `about` attribute of `python_dev.pyde.meta`.

## Module Class

Instances of module class represent the meta data of modules defined in the local development environment.

Attribute   | Data Type | Description
------------|-----------|------------------------------
meta | Meta | The metadata of the package defining the module
name | str  | The name of the module.

### Methods

Method                | Description
----------------------|-------------------------
testing_module_name() | The name of the testing module for the module
testing_class_name()  | The name of the `TestCase` class for the module
module_dir()          | The name of the module directory relative to the package root directory

#### Method testing_module_name()

**Returns**: The name of the testing module for the module

#### Method testing_class_name()

**Returns**: The name of the `TestCase` class for the module

#### Method module_dir()

**Returns**: The module directory relative to the package root directory
















