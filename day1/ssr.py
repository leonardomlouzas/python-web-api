# carregar os dados
dados = [
    {"nome": "Bruno", "cidade": "Viana"},
    {"nome": "Caio", "cidade": "Brasilia"}
]

# processar os dados
template = """\
<html>
<body>
<ul>
<li> Nome: {dados[nome]}</li>
<li> Cidade: {dados[cidade]}</li>
</ul>
</body>
</html>
"""
# renderizar os dados

for item in dados:
    print(template.format(dados=item))