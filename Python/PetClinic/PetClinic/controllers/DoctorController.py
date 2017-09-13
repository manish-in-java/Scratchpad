from datetime import datetime
from flask import jsonify, render_template, request

from PetClinic import app
from PetClinic.model.Doctor import Doctor

import sys

'''
Gets a page of veterinarians.
'''
@app.route('/doctor/page', methods = ['GET'])
def pageDoctors():
    page = request.args.get('draw', 1, int)
    total = Doctor.count()

    return jsonify(data = [doctor.serialize() for doctor in Doctor.page(page, 10, Doctor.firstName, Doctor.lastName)]
        , draw = page
        , recordsFiltered = total
        , recordsTotal = total)

'''
Saves a veterinarian if one with the specified name does not already exist.
'''
@app.route('/doctor', methods = ['POST'])
def saveDoctor():
    # Extract first and last name from the request.
    firstName = request.form['firstName'].strip().title()
    lastName = request.form['lastName'].strip().title()

    # If a doctor with the specified name already exists, display an error
    # message.
    if (Doctor.count(Doctor.firstName == firstName, Doctor.lastName == lastName) > 0):
        return render_template('doctor.jade',
            error='Unable to add veterinarian because the specified name already exists.',
            title='Veterinarians',
            year=datetime.now().year)

    # Add a new doctor with the specified name.
    Doctor(firstName = firstName, lastName = lastName).save()

    return render_template('doctor.jade',
        title='Veterinarians',
        year=datetime.now().year)

'''
Displays the Veterinarians Administration page.
'''
@app.route('/doctor', methods = ['GET'])
def showDoctors():
    return render_template('doctor.jade',
        title='Veterinarians',
        year=datetime.now().year)
