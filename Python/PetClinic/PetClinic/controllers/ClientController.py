from datetime import datetime
from flask import render_template
from PetClinic import app

'''
Displays the Clients Administration page.
'''
@app.route('/client')
def showClients():
    return render_template(
        'client.jade',
        title='Clients',
        year=datetime.now().year
    )
