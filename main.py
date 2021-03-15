from pathlib import Path
import requests
import dicttoxml
from xml.dom.minidom import parseString 
import json
import toml
import yaml
import shutil


outputdir = Path('results')
#shutil.rmtree(outputdir)

fout = outputdir / 'result_api.json'
fout.parent.mkdir(exist_ok=True)


## Get a json result
url_api = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url_api)
print(response, end='\n\n')

content_list = response.json()


## list > dict
content_dict = {'clients': {str(i): item for i, item in enumerate(content_list)}}
print(content_dict, end='\n\n')

# content_list > json
with fout.with_suffix('.json').open('w') as f:
    json.dump(content_list, f, indent=2)


# content_dict > json
with fout.with_name(f'{fout.stem}0.json').open('w') as f:
    json.dump(content_dict, f, indent=2)


# list2yaml
with fout.with_suffix('.yaml').open('w') as f:
    yaml.dump(content_list, f, default_flow_style=False)


# dict2yaml
with fout.with_name(f'{fout.stem}0.yaml').open('w') as f:
    yaml.dump(content_dict, f, default_flow_style=False)


# content_list > xml
xml = dicttoxml.dicttoxml(content_list, custom_root='clients', attr_type=False)
print(parseString(xml).toprettyxml(), end='\n\n')
fout.with_suffix('.xml').write_text(parseString(xml).toprettyxml())


# dict2toml
with fout.with_name(f'{fout.stem}0.toml').open("w") as f:
    toml.dump(content_dict, f)
