"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PetClinic import app

'''
Displays the home page.
'''
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.jade',
        title='Welcome',
        year=datetime.now().year
    )

'''
Displays the Clients Administration page.
'''
@app.route('/client')
def client():
    return render_template(
        'client.jade',
        title='Clients',
        year=datetime.now().year
    )

'''
Displays the Veterinarians Administration page.
'''
@app.route('/doctor')
def doctor():
    return render_template(
        'doctor.jade',
        title='Veterinarians',
        year=datetime.now().year
    )

'''
Displays the Pets Administration page.
'''
@app.route('/pet')
def pet():
    return render_template(
        'pet.jade',
        title='Pets',
        year=datetime.now().year
    )
