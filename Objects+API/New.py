import requests

json_url = 'https://jsonplaceholder.typicode.com/todos/' 
response = requests.get(json_url)
get = response.json()

#print(get)
#print(type)
#print(get[0])
#print(type(get[0]))
#print(get[0]["title"])

#for post in get[:3]:
#    print(post)

for t in range(3):
    id = get[t]['id']
    inc = get[t]['title']

    print(f"id: {id}, title: {inc}")