from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/httptest', methods=['GET', 'POST'])
def httptest():
    if request.method == 'GET':
        print('salary:', request.args.get('salary'))
        print('tax:', request.args.get('tax'))
        return 'It is a get request!'
    if request.method == 'POST':
        print('name:', request.form.getlist('name'))
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()
