from datetime import datetime
from flask import jsonify, render_template, request

from PetClinic import app
from PetClinic.model.Client import Client
from PetClinic.model.Pet import Pet

@app.route('/pet/page', methods = ['GET'])
def pagePets():
    """
    Gets a page of pets.
    """
    page = request.args.get('draw', 1, int)
    total = Pet.count()

    return jsonify(data = [pet.serialize() for pet in Pet.page(page, 10, Pet.name)]
        , draw = page
        , recordsFiltered = total
        , recordsTotal = total)

@app.route('/pet', methods = ['POST'])
def savePet():
    """
    Saves a pet if one with the specified name and client does not already
    exist.
    """
    # Extract pet details from the request.
    birthDate = request.form['birthDate'].strip()
    client = Client.findOne(request.form['client'])
    name = request.form['name'].strip().title()
    type = request.form['type'].strip().title()

    # If a pet with the specified name, type and client already exists, display
    #  an error message.
    if (Pet.count(Pet.client == client, Pet.name == name, Pet.type == type) > 0):
        return showPets(error='Unable to add pet because a pet with the specified name and type already exists for the given client.')

    # Add a new pet with the specified name.
    Pet(birthDate = datetime.strptime(birthDate, "%Y-%m-%d").date(), client = client, name = name, type = type).save()

    return showPets()

@app.route('/pet')
def showPets(**context):
    """
    Displays the Pets Administration page.
    """
    model = dict(clients=Client.findAll(Client.firstName, Client.lastName), title='Pets', year=datetime.now().year)
    model.update(context)

    return render_template('pet.jade', **model)
