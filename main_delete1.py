import requests
url = 'http://172.25.253.124:5000/deletar_alunos'

id = 7

response = requests.delete(f"{url}/{id}")
print(response.status_code)