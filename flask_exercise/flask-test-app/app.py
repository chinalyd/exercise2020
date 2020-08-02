from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/user/<name>')
def user_index(name):
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time:', request.args.get('time'))
    print('q:', request.args.get('q'))
    print('Q:', request.args.getlist('Q'))
    return render_template('user_index.html', username=name)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('method:', request.method)
    print('name:', request.form.get('name'))
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.get('hobbies'))
    print('age:', request.form.get('age', default=1))
    return 'registered successfully!'

@app.route('/courses/<name>')
def course(name):
    return render_template('courses.html', coursesname=name)


