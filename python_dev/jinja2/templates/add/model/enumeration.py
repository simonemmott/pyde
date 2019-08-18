class {{enum.class_name()}}Types(Enum):
{% for enum_val in enum.enumerations() %}
    {{to_snake_case(enum_val).upper()}} = '{{enum_val}}'
{% endfor %}
