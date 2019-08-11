# Configuring Inclusions

Inclusions are defined as sub directories of the `include` directory in the jinja2 template locations.

**e.g.**

The jinja2 template location structure shown below

- templates
  - include
    - my_cool_inclusion
      - inclusion.yaml
      - my_cool_template.py
      - my_other_template.py
    - some_other_inclusion
      - inclusions.yaml
      - some_other_template.txt
      - sub_package
        - another_template.py
      
defines two additional inclusions `my_cool_inclusion` and `some_other_inclusion`

The inclusion templates are rendered with the context `meta` equal to the meta data extracted from the local development environment.

The templates in the inclusion are rendered into the root of the local development environment following any directories defined in the inclusion.

**e.g.**

With the above custom inclusions 

```
pyde include some_other_inclusion
```

would add the file `some_other_template.txt` to the root of the local development environment.
Create the directory `sub_package` in the root of the local development environment if it does not already exist and create the file `another_template.py` in the `sub_package` directory.

The includes files contain the rendered results of the templates that created them.

## Controlling The Inclusion

Each inclusion should contain a file `inclusion.yaml` in the root directory of the inclusion. Each directory in the inclusion can also specify an `inclusion.yaml` file.
The `inclusion.yaml` files define meta data for the inclusion.

### Checking If The Local Development Environment Contains The Inclusion
The `inclusion.yaml` file in the root of directory of the inclusion should define the attribute `check`. 
The check attribute of inclusion is a dot separated string giving the location of a python method to execute to determine whether or not the local development environment includes the inclusion.
The method pointed at by the check attribute receives the OS location of the local development environment as a string and is expected to return True if the local development environment contains the inclusion.
This method is called when identifying the values to be added to the `pyde.meta.includes` list.

**e.g.**

The `inclusion.yaml` below

```yaml
check: python_dev.logging.check_includes
```

identifies that the method `python_dev.logging.check_includes` should be called with the location of the local development environment to determine whether or not the inclusion is included.

If the check attribute is not defined then the meta data will not indicate whether the inclusion is present or not.

### Specifying Requirements For The Inclusion

In addition to the `check` attribute the root `inclusion.yaml` can define a list of requirements to be added to the local development environment in the attribute `requires`. 

Each requirement in the `inclusion.yaml` must define the name of the required package in the `package` attribute of the inclusion.
Each requirement can optionally define the following attributes

Attribute      | Description
---------------|---------------
version        | The required version of the package or the lower bound version if the requirement is for any version between two version.
operator       | The requirement operator for the given version. This attribute is required if a `version` attribute is defined.
upper_version  | The upper bound version number if the requirement is for any version between two version.
upper_operator | The upper bound operator if the requirement is for any between two version.
hash           | The hash value of the requirement.

**e.g.**

The requirement:

```yaml
requires:
  - package: pyYaml
    version: 1.2.3
    operator: >=
    upper_version: 2.0.0
    upper_operator: <
```

defines a requirement for the package `pyYaml` greater than or equal to version `1.2.3` and less than version `2.0.0`

Each requirement for the inclusion is added to the required packages for the local development environment by updating the `requirements.txt` file. 
The `requirements.txt` file is created if it does not already exist. 
The requirements are also automatically imported into the local development environment using `pip install`

### Controlling Included Filenames

Often the final name of the included files is dependent on the extracted meta data.
Inclusions support this requirement by allowing the filename to be generated with jinja2.

Each file or directory in the inclusion can optionally have its installed name templated.

Such files are identified by adding a template attribute to the `inclusion.yaml` file with the name of the included template.

If a template attribute exists for the included file and the template attribute defined an attribute `name` then that name is passed through jinja2 to generate the final name for the installed file or directory.

The context of the jinja2 generation of the final file name is the same as the context supplied to the inclusion.

**e.g.**

The `inclusion.yaml` defined below

```yaml
some_file.txt:
  name: some_file_{{meta.about.version}}.txt
```

Causes the content of the `some_file.txt` template in the inclusion to the installed in the local development environment with the name `some_file_1.2.3.txt` if the version defined in `about.py` is `1.2.3`.

### Repeating Included Files For A List Of Items

Often an included file should be included for each item in a list of data and the context of each included instance should be set to the data from the item in the list.
Inclusions support this requirement by allowing template files to define a data path to a list of items for which to repeat the template.

To repeat a template file for each item in a list of data the template file must be included in the `inclusion.yaml` as a template attribute.

If the template attribute defines a `path` attribute then the given path is used to lookup values in the mata data using the `__find__(path)` method of the Meta class. The `__find__(path)` method of the Meta class is inherited from the `Finder` mixin defined in the `json_model` module.

The `__find__(path)` method returns a list of data items matching the given path.

The template file is repeated for each item in this list with the additional contect parameter `item` containing the item of data in the list.

**e.g.**

The `inclusion.yaml` file below

```yaml
some_template.py
  path: modules
  name: some_{{item.name}}.py
```

causes the template file some_template.py to be repeated for each module in the list of modules in the meta data.
Assuming the meta data includes modules named `foo` and `bar` the files `some_foo.py` and `some_bar.py` would be included by the inclusion. Also the context when rendering `some_template.py` will include the variable `item` with the module being processed.













