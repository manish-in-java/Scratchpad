from datetime import datetime
from flask import jsonify, render_template, request

from PetClinic import app
from PetClinic.model.Client import Client

'''
Gets a page of clients.
'''
@app.route('/client/page', methods = ['GET'])
def pageClients():
    page = request.args.get('draw', 1, int)
    total = Client.count()

    return jsonify(data = [client.serialize() for client in Client.page(page, 10, Client.firstName, Client.lastName)]
        , draw = page
        , recordsFiltered = total
        , recordsTotal = total)

'''
Saves a client if one with the specified name does not already exist.
'''
@app.route('/client', methods = ['POST'])
def saveClient():
    # Extract data from the request.
    building = request.form['building'].strip().title()
    firstName = request.form['firstName'].strip().title()
    lastName = request.form['lastName'].strip().title()
    locality = request.form['locality'].strip().title()
    postCode = request.form['postCode'].strip().title()
    province = request.form['province'].strip().title()
    street = request.form['street'].strip().title()
    town = request.form['town'].strip().title()

    # If a client with the specified name already exists, display an error
    # message.
    if (Client.count(Client.firstName == firstName, Client.lastName == lastName) > 0):
        return render_template('client.jade',
            error='Unable to add the client because the specified name already exists.',
            title='Clients',
            year=datetime.now().year)

    # Add a new client with the specified details.
    Client(firstName = firstName
           , lastName = lastName
           , building = building
           , street = street
           , locality = locality
           , town = town
           , province = province
           , postCode = postCode).save()

    return render_template('client.jade',
        title='Clients',
        year=datetime.now().year)

'''
Displays the Clients Administration page.
'''
@app.route('/client')
def showClients():
    return render_template('client.jade',
        title='Clients',
        year=datetime.now().year)
