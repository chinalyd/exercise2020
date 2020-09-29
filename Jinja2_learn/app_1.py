#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    teacher = {
            'name' : 'Jack',
            'email': 'chinalyd0820@sina.cn'
            }
    course = {
            'name': 'Python3 basic',
            'teacher': teacher,
            'user_count': 2345,
            'price': 'Free',
            'lab': None,
            'is_private': False,
            'is_member_course': True,
            'tags': ['python', 'bigdata', 'Linux']
            }
    return render_template('index_1.html', course=course)
