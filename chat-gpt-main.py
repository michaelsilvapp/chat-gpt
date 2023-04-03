import openai
import os


# Define a chave da API do OpenAI
os.environ["k"] = 'KEY'

api_key = os.environ.get("k")

if api_key is None:
    print("A chave da API do OpenAI não foi encontrada no ambiente.")
else:
    openai.api_key = api_key

    # Define o modelo a ser usado
    model_engine = "text-davinci-002"

    # Define a pergunta
    prompt = "quantos paises existem?"

    print(prompt)
    # Define o número de respostas a serem geradas
    num_responses = 1

    # Define o comprimento máximo da resposta
    max_tokens = 50

    # Gera as respostas usando o modelo selecionado
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=num_responses,
    )

    # Imprime a resposta
    print(response.choices[0].text)
