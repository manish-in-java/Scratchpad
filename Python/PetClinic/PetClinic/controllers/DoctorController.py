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
    page = request.args.get('draw', type=int)

    return jsonify(
        data = Doctor.page(page, 10, Doctor.firstName)
        , draw = page
        , recordsTotal = Doctor.count()
        )

'''
Displays the Veterinarians Administration page.
'''
@app.route('/doctor', methods = ['GET'])
def showDoctors():
    return render_template(
        'doctor.jade',
        title='Veterinarians',
        year=datetime.now().year
    )
