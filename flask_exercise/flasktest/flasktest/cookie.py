from flask import Flask, render_template, request, Response, make_response

app = Flask(__name__)

app.config['SECRET_KEY']='1234567abcdefg'

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookies():
    if request.method == 'POST':
        user = request.form['name']
        print(user)
        resp = Response(response='name accept')
        resp.set_cookie('userID', 'user', expires=None)#set a cookie named userID
    return render_template('readcookie.html')


@app.route('/getcookie')
def getcookie():
    print(request.cookies.get('userID'))
    name = request.cookies.get('userID')#get cookie userID's value
    return '<h1> welcome, {}</h1>'.format(name)
