import os
import subprocess
import sys
import ollama

def clone_repository(repo_url):
    """
    Clones the specified GitHub repository.

    Parameters:
    - repo_url (str): The URL of the GitHub repository to clone.

    Returns:
    - str: The name of the cloned directory.
    """
    try:
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        subprocess.run(['git', 'clone', repo_url], check=True)
        return repo_name
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

def generate_overview(repo_name):
    """
    Generates an overview of the repository using the Llama model.

    Parameters:
    - repo_name (str): The name of the cloned repository directory.

    Returns:
    - str: The generated overview.
    """
    readme_path = os.path.join(repo_name, 'README.md')
    if not os.path.exists(readme_path):
        return "No README.md found in the repository."

    with open(readme_path, 'r') as file:
        readme_content = file.read()

    prompt = f"Summarize this project:\n{readme_content}"
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def create_markdown_overview(repo_name, overview):
    """
    Creates a Markdown file with the overview of the repository.

    Parameters:
    - repo_name (str): The name of the cloned repository directory.
    - overview (str): The overview content to include in the Markdown file.
    """
    md_content = f"# {repo_name} Overview\n\n{overview}\n"
    with open(os.path.join(repo_name, 'overview.md'), 'w') as file:
        file.write(md_content)

if __name__ == '__main__':
    repo_url = input("Enter the GitHub repository URL to clone: ")
    repo_name = clone_repository(repo_url)
    overview = generate_overview(repo_name)
    create_markdown_overview(repo_name, overview)
    print(f"\nOverview for '{repo_name}' has been generated and saved as 'overview.md'.")
