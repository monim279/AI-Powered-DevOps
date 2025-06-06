import ollama

def get_llama_response(prompt):
    """
    Sends a prompt to the Llama model and returns the response.

    Parameters:
    - prompt (str): The input prompt to be sent to the Llama model.

    Returns:
    - str: The response from the Llama model.
    """
    try:
        response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    user_prompt = input("Enter your prompt: ")
    response = get_llama_response(user_prompt)
    print("\nLlama Model Response:\n")
    print(response)
