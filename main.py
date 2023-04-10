import os
import openai
# openai.organization = "org-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"
openai.api_key = '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'
# Function to call the OpenAI API
def generate_text(prompt, model="text-davinci-002", max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define a prompt and call the function
prompt = "What are the key principles of a successful business?"
response_text = generate_text(prompt)

# Print the generated response
print(response_text)