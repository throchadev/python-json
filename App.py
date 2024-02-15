import json

data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# lendo json
data_1 = json.loads(data_JSON)

print(data_1)

# leitura arquivo json
with open('dados.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    print(dados)

    dados['Apelido'] = 'Thi'

#escrita arquvo json
with open('dados2.json', 'w', encoding='utf8') as arquivo2:
    json.dump(dados, arquivo2)    