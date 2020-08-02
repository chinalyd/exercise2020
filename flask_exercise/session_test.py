from flask import session
from datetime import timedelta
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASDFASDF'

@app.route('/set_session')
def set_session():
    print(session)
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    session['username'] = 'alfred'
    return 'set session successful'

@app.route('/get_session')
def get_session():
    value = session.get('username')
    return 'Required session value is: {}'.format(value)

@app.route('/del-session')
def del_session():
    value = session.pop('username')
    return 'delete successful, value is {}'.format(value)

if __name__ == '__main__':
    app.run()
