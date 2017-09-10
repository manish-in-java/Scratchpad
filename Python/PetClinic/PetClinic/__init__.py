"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import PetClinic.controllers.ClientController
import PetClinic.controllers.DoctorController
import PetClinic.controllers.HomeController
import PetClinic.controllers.PetController

import PetClinic.model.Client
import PetClinic.model.Doctor
import PetClinic.model.Pet

from PetClinic.model.Entity import Base, Engine

Base.metadata.create_all(Engine)
