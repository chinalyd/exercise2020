from flask import Flask 
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/user/<username>')
def user_index(username):
    return 'hello {}'.foramt(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/<username>')
def hello(username):
    if username == 'shiyanlou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))

if __name__ =='__main__':
    app.run()
