from datetime import datetime
from flask import render_template
from PetClinic import app

@app.route('/')
@app.route('/home')
def showHome():
    """
    Displays the home page.
    """
    return render_template('index.jade',
        title='Welcome',
        year=datetime.now().year)
