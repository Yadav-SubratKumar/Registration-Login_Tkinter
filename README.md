## Registration-Login Form Application

This is a simple registration-login form application created using Python and the Tkinter library. It allows users to enter 
their registration details, including their name, contact information, email, address, gender, and hobbies.
And allow's the user to login usign the registration details i.e name and email
The application validates the data entered by the user and stores it in a SQLite database.

## Files & Purpose
 1. reg.py :- Main file which provides the GUI for Registration and Login form
 2. validate_fn.py :- File consist of validate function and data receiver function
 3. database.py :- File consist of the data insertion functionand verifying login deatils in the database
 4. printer.py :- File consist of the data printing function [from database]
 5. registration.db :- An Sqlite database to store the user registered data 

## Features

- User-friendly graphical user interface (GUI) for registration and login.
- Data validation for name, contact, address, email, gender, and hobbies.
- Storage of registration data in a SQLite database.
- Ability to view and retrieve registered data from the database.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or higher)
- Tkinter library (usually comes with Python)

## Installation

1. Clone or download the project from this repository.

2. Make sure you have Python and Tkinter installed on your system.

3. Run the `reg.py` script to start the application.



