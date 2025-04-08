import json

def generate_terraform(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    terraform_content = ''
    if "resource_type" in data:
        terraform_content += f'resource "{data["resource_type"]}" "{data["resource_name"]}" {{\n'
        for key, value in data["parameters"].items():
            if isinstance(value, dict):
                terraform_content += f'  {key} = {{\n'
                for sub_key, sub_value in value.items():
                    terraform_content += f'    {sub_key} = "{sub_value}"\n'
                terraform_content += f'  }}\n'
            else:
                terraform_content += f'  {key} = "{value}"\n'
        terraform_content += '}\n'

    with open("main.tf", "w") as tf_file:
        tf_file.write(terraform_content)

generate_terraform("dr_project.json")

