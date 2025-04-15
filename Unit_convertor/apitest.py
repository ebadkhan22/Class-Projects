import openai

openai_client = openai.OpenAI(api_key="your open ai key")

models = openai_client.models.list()
for model in models:
    print(model.id)
