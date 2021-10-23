import requests

headers = {'User-Agent':'Anonymous'}

# responce = requests.get('http://httpbin.org/get', headers=headers, params={'a':'b', 'c':10})
responce = requests.post('http://httpbin.org/post',
                         headers=headers,
                         params={'a':'b', 'c':10},
                         json={'username':'superuser'})

# if responce.status_code == 200:
#     print('OK!')
#
# if responce.ok:
#     print('OK!')

# responce.raise_for_status()

print(responce.text)