from jinja2 import Template
import json

param_kwargs = {'parameterOne': 'Value1',
                'parameterTwo': 'Value2',
                'parameterThree': 'Value3',}

with open('cfn-parameter.json.j2') as j2f:
    template = Template(j2f.read())

template_as_string = template.render(**param_kwargs)
template_as_dict = json.loads(template_as_string)
print(template_as_dict)


