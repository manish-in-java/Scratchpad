from datetime import datetime
from flask import render_template
from PetClinic import app

'''
Displays the home page.
'''
@app.route('/')
@app.route('/home')
def showHome():
    return render_template(
        'index.jade',
        title='Welcome',
        year=datetime.now().year
    )
