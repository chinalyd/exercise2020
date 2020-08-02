import requests

#get
payload = {'salary':19500, 'tax':1300}
r1 = requests.get('http://127.0.0.1:5000/httptest', params=payload)
print(r1.text)

#post
user_info = {'name':['hanyuxian', 'liyingda']}
r2 = requests.post("http://localhost:5000/httptest", data=user_info)
print(r2.text)
