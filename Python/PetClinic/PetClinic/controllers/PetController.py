from datetime import datetime
from flask import render_template
from PetClinic import app

'''
Displays the Pets Administration page.
'''
@app.route('/pet')
def showPets():
    return render_template(
        'pet.jade',
        title='Pets',
        year=datetime.now().year
    )
