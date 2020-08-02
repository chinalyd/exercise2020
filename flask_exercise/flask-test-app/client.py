import requests

user_info = {'name':'hanyuxian', 'password':'LYD0820@sh', 'hobbies':['shoot', 'economy']}
r = requests.post("http://127.0.0.1:5000/register", data=user_info)

print(r.text)
