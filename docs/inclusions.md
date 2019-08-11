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

Additional inclusions can be defined by adding contents to the `include` directory of any of the configured jinja2 template locations.

See [defining inclusions](.configuring_inclusions.md) for details on how to define additional inclusions.

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

```python
import logging

logger = logging.getLogger(__name__)
```

And log messages by 

```python
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

The testing inclusion adds testing support to the local development environment.

The testing inclusions adds the module `testing` to the root of the local development environment. This module is ignored when `pyde` scans the local development environment for modules in the meta data. The testing module will contain the test modules for the local development environment.

The testing module is configured as a python barrel into which all the `TestCase` classes should be imported.

**e.g.**

Given the testing module structure of
testing
 - __init__.py
 - module_a_tests.py
    - ModuleATests(TestCase)
 - module_b_tests.py
    - ModuleBTests(TestCase)

The `__inti__.py` of the `testing` module should contain

```python
from .module_a_tests import ModuleATests
from .module_b_tests import ModuleBTests
```

The testing inclusions automatically creates test modules as sub modules of the `testing` module with a `TestCase` class for each module found in the local development environment and adds these modules and classes to the testing barrel.

The testing inclusion adds the module `test.py` to the root of the local development environment.
The `test.py` module should be executed to execute all the defined tests.

**e.g.**

```
python test.py
```

will execute all the `TestCase` classes in the local development environment.

The `test.py` executes the test cases using the `unittest.main()` method passing in the arguments passed to `test.py`.
Test execution can be limited to a single test case by specify the name of the test case on the command line.

**e.g.**

```
python test.py ModuleATests
```

will only execute the test case `ModuleATests`

and

```
python test.py ModuleATests.test_some_cool_stuff
```

will only execute the test `test_some_cool_stuff` from the `ModuleATests` test case.

The testing inclusion adds the module `settings.py`. The settings module includes attributes used in test execution.
By default this module only contains the attribute `SKIP` with the value `True`.
This allows tests to be optionally skipped using the `@unittest.skipIf(settings.SKIP, <message>)` decorator.

This configuration will by default skip such decorated tests. It is possible to execute such decorated tests at execution time by adding the `--no-skip` option to the call to `test.py`

**e.g.**

```
python test.py --no-skip
```

will execute all the tests in all the test cases including those decorated with the `@skipIf(...)` decorator.

Unit tests should be decorated with the `@skipIf(...)` decorator if the tests invoke remote services which cannot be guaranteed to be available during automated builds. 
Often such tests will require credential information or other details to be supplied at run time.

The `test.py` module supports this requirement by allowing setting values to be defined at runtime. Any options passed to the `test.py` module are removed from the arguments passes to `unittest.main()` and instead are added to as attributes to the `settings.py` module.

**e.g.**

```
python test.py --USER=username --PASSWORD=password
```

adds the attributes `USER` and `PASSWORD` to the `settings.py` module with the values 'username' and 'password' before executing the tests.

The testing inclusion adds a requirement for `coverage` to the local development environment.
The `coverage` package provides support for test coverage analysis.

Test coverage is analysed by executing the `run` sub command of the ` coverage` executable.

**e.g.**

```
coverage run test.py --no-skip
```

Will execute all the unit tests including the skipped tests and record the test coverage in a binary file `.coverage`. The test coverage can be exported as HTML and viewed in a browser.

**e.g.**

```
coverage html
```

generates html pages detailing the test coverage in the directory `htmlcov`. The coverage report can be viewed in a browser by opening the file `htmlcov/index.html` in a browser.

The `.gitingore` file by default is configured to ignore the `.coverage` file and the `htmlcov` directory.


















