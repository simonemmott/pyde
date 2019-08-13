# Support For OpenApi

The `pyde` CLI can read OpenApi documents and includes the parsed API documentation in the
[Meta class](metadata.md)

The `pyde` CLI includes the option `--api` specifying a value for this option causes the 
[OpenApi](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) document referenced by the api option to be parsed as a JsonModel object.
The resultant object is included as the value of the `api` attribute of the `Meta` class.
The api data is available in the jinja2 templates through the attribute `meta.api`.

**e.g.**

```
pyde --api=myApi.json ...
```

Causes the JSON document `myApi.json` to be loaded into the `meta.api` attribute as an OpenApi document and is available in the subsequent commands

The value of the `--api` option can be.

1. A file in the local file system relative to the current working directory.
1. A file in the local file system with an absolute path.
1. A URL

If the value of the `--api` option includes the text `://` then it is assumed to be a URL

Otherwise the value is treated as a location in the local file system either relative or absolute.
















