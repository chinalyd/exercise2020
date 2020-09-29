from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD']= True

def hidden_email(email):
    parts = email.split('@')
    parts[0] = '*****'
    return '@'.join(parts)

app.add_template_filter(hidden_email)

@app.route('/')
def index():
    teacher = {
            'name': 'Adam',
            'email': 'luoanxian@gmail.com'
            }

    course = {
            'name': 'Python Basic',
            'teacher': teacher,
            'python': 'lou+ python',
            'java': 'java base',
            'bigdata': 'spark sql',
            #'teacher': 'shiyanlou',
            'is_unique': False,
            'has_tag': True,
            'tags': ['c', 'c++', 'docker']
            }
    return render_template('index.html', course=course)

@app.route('/courses/<course_name>')
def courses(course_name):
    return render_template('course.html', course_name=course_name)
