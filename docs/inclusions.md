# Inclusions

## Include Command

The `include` command adds the include functionality to the local development environment.
```
pyde include <inclusion>
```

example

```
pyde include configuration
```

Includes the `configuration` inclusion into the local development environment

### Inclusions

The `include` command can include the following functionality in to the local development environment

Inclusion     | Description
--------------|------------------
configuration | Add a configuration file and module to find and read the configuration file.
logging       | Add logging configuration to the local development environment
testing       | Add testing setup to the local development environment

Inclusions are defined as jinja2 templates in the `include` directory of the defined jinja2 template locations.

#### Configuration Inclusion

The configuration inclusion adds a configuration file to the development package and a `configuration.py` to the `root_module`

The configuration file is by default named `<root_module>.ini` and includes the group `[<root_module>]`

The configuration data in the configuration file is available through `<root_module>.configuration.config`.

The default name of the configuration file can be altered by changing the value of the `config_name` attribute of the `<root_module>.configuration` module. The expected configuration file name is `<config_name>.ini`.

Additionally the name of the configuration file can be adjusted at runtime by setting the environment variable `<CONFIG_NAME>_CFG` where <CONFIG_NAME> is the uppercase variant of the `config_name` attribute.

Importing the `<root_module>.configuration` module searches the run time environment for the configuration file.

The configuration file is searched for in the following locations.

1. The current working directory
1. The directory containing the executable command
1. The users home directory identified by the environment variable `HOME`

The configuration inclusion adds the following requirements to the local development environment 

1. pyYaml

#### Logging Inclusion

The logging inclusion adds logging configuration to the local development environment. This inclusion does not alter the functionality of the local development environment. Instead it installs the files `logger.py` and `logging.yaml` into the root of the local development environment to setup a logging configuration for the local development environment.

The `logger.py` module defines a `default_config` attribute which is a dict of the default logging configuration. This default logging configuration is used if the expected logging configuration file cannot be found.

The `logging.yaml` file is the default logging configuration file expected by `logger.py`. You can alter the logging configuration of the local development environment by adjusting the details in `logging.yaml`.

To add logging to modules you should

```
import logging

logger = logging.getLogger(__name__)
```

And log messages by 

```
logger.info('Info message')
```

Or any of the other standard logger methods.

To include the logging configuration when executing python scripts in the local development environment it is necessary to execute `logger.configure_logging()`.

The `configure_logging()` method receives the following optional parameters

Parameter | Default | Description
----------|---------|------------------
config_path | 'logging.yaml' | The location of the logging configuration file.
config_format | 'YAML' | The format of the logging configuration file. Supported formats are 'YAML' or 'JSON'

The logging inclusion adds the following requirements to the local development environment 

1. pyYaml


#### Testing Inclusion

The testing inclusion adds testing support



















