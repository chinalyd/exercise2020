from flask import Flask 
from flask import url_for
from flask import redirect
from flask import make_response
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

'''@app.route('/delete_cookies')
def delete():
    resp.delete_cookie('username')
    return 'Delete cookies'
'''
@app.route('/user/<username>')
def user_index(username):
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username',username)
    return resp

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/<username>')
def hello(username):
    if username == 'shiyanlou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))

@app.route('/courses/<courses_name>')
def courses(courese_name):
    return 'courses:{}'.format(courses_name)

@app.route('/test')
def test():
    print(url_for('courses', courses_name='java'))
    return redirect(url_for('index'))

if __name__ =='__main__':
    app.run()
