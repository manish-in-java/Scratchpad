# Overview

**[Pet Clinic](https://github.com/spring-projects/spring-petclinic)** is a
sample web application that demonstrates various features of the Java-based
[Spring framework](https://spring.io).

This sample application replicates the Pet Clinic functionality using the
following technologies:

1. [Python programming language](https://www.python.org),
1. [Flask microframework for Python](http://flask.pocoo.org), and
1. [SQLAlchemy ORM for Python](https://www.sqlalchemy.org).

The Pet Clinic application is designed for a fictitious medical clinic
where people can bring their pets for medical treatment or consultation
with a veterinarian. The users of the application are people employed by
or affiliated with the clinic. These users view and manage information
regarding the veterinarians, the clients of the clinic and the clients'
pets.

# Use Cases

This sample application currently supports the following functionality:

* Veterinarians
    * View a list of all veterinarians who work at the clinic
    * Add a veterinarian
* Clients
    * View a list of all client who have ever visited the clinic
    * Add a client
* Pets
    * View a list of all pets who have ever visited the clinic
    * Add a pet for a client

# Future Work

The following functionality needs to be added to this sample:

* Employees (other than veterinarians)
    * View a list of all employees who work at the clinic
    * Add an employee
* Visits
    * View all visits for a pet
    * Schedule a visit for a pet
    * Add a visit for a pet
    * Capture veterinarian's notes and comments about a visit
    * Capture details for a pet like weight, height, body temperature, etc. during a visit
* Procedures
    * View all procedures undertaken for a pet
    * Schedule a procedute for a pet
    * Add a procedure for a pet
    * Capture details for a procedure
* Reports
    * Daily/Weekly/Monthly/Quarterly/Yearly visit reports
    * Daily/Weekly/Monthly/Quarterly/Yearly procedure reports
