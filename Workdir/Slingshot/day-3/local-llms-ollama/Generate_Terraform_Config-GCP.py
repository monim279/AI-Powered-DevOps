import ollama

CONFIG_PROMPT = """
Generate a Terraform configuration for a GCP {resource_type} with best practices. 
Include:
- Provider configuration
- Resource definition
- Necessary variables
- Outputs if applicable
Do not provide any description, only the configuration.
"""

TIPS_PROMPT = """
Based on the following Terraform configuration for a GCP {resource_type}, provide unique setup tips or notes:
{configuration}
"""

def generate_terraform_config(resource_type):
    """
    Generates a Terraform configuration for a specified GCP resource type using the Llama model.

    Parameters:
    - resource_type (str): The type of GCP resource (e.g., vm, security group, vpc).

    Returns:
    - str: The generated Terraform configuration as a string.
    """
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': CONFIG_PROMPT.format(resource_type=resource_type)}])
    return response['message']['content']

def generate_tips(resource_type, configuration):
    """
    Generates unique setup tips or notes for a specified Terraform configuration using the Llama model.

    Parameters:
    - resource_type (str): The type of GCP resource.
    - configuration (str): The Terraform configuration for which tips are needed.

    Returns:
    - str: Unique setup tips or notes.
    """
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': TIPS_PROMPT.format(resource_type=resource_type, configuration=configuration)}])
    return response['message']['content']

if __name__ == '__main__':
    resource_type = input("Enter the GCP resource type (e.g., vm, security group, vpc): ")
    terraform_config = generate_terraform_config(resource_type)
    tips = generate_tips(resource_type, terraform_config)
    print("\nGenerated Terraform Configuration:\n")
    print(terraform_config)
    print("\nUnique Tips for setting up the resource:\n")
    print(tips)
