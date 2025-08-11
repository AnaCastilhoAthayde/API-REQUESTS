import requests

dados = {
    'nome': 'Ana'
    'email' 'Ana@email.com'
}

response =  requests.get('http://172.25.253.124:5000/alunos')
enviar = requests.post('http://172.25.253.124:5000/alunos',json=dados)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    enviar.json()
    print(response.json())
else:
    print(f"Erro na requisição.Código de status: {response.status_code}")