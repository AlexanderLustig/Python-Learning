import requests

#payload = {'username': 'corey', 'password': 'testing'}
#r = requests.get('https://pbs.twimg.com/media/FKhD35SWQAgzHKV?format=png&name=900x900/post')
#r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
r = requests.get('https://httpbin.org/delay/6', timeout=3)
#print(r)
#print(dir(r))
#print(help(r))
#print(r.content)
#with open('comic.png', 'wb') as f:
#    f.write(r.content)
#print(r.status_code)
#print(r.ok)
#print(r.headers)
#r_dict = r.json()
#print(r_dict['form'])
#print(r.text)
print(r)
