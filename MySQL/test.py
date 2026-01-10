import requests

headers ={'Authorization': "Bearer YOUR_ACCESS_TOKEN"}
response= requests.get('https://example.com/api/data', headers=headers)
data = response.json()
print(data)