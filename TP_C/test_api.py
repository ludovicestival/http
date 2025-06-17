"""Script to test HTTP API"""

import requests

#payload = {'pseudo': 'roger', 'canal': 'coincoin'}
#data = {'pseudo': 'ginette', 'message': 'coin coin'}
headers = {'X-CanaDuck': 'experience-stagiaire'}

#r = requests.get('https://httpbin.org/get', json=data)
r = requests.post('https://httpbin.org/post', json={'test': 123}, headers=headers)

#print(f'{r.url}\n')

status = r.status_code
headers = r.headers
json = r.json()

print(f'Statut: {status}\n')
print(f'En-têtes: {headers}\n')
print(f'JSON: {json}\n')
