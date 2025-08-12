import requests
url = 'http://172.25.253.124:5000/put_alunos'
dados = {
    'Nome': 'Ana',
    'Email': 'Ana@email',
}
id = 7

response = requests.put(f"{url}/{id}",json=dados)
print(response.status_code)
