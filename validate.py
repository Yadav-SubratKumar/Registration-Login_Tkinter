import re

# Function to validate the user data
def validate_data(data):
    errors = {}
    # validating Name
    if not data["Name"]:
        errors["Name"] = "Name is required."
    else:
        if not data["Name"].isalpha():
            errors["Name"] = "Name must be all alphabet."

    # validating Contact
    if not data["Contact"]:
        errors["Contact"] = "Contact is required."
    else:
        if not data["Contact"].isdigit() or len(data["Contact"]) != 10:
            errors["Contact"] = "Contact must be a 10-digit numeric value."

    # validating Email
    if not data["Email"]:
        errors["Email"] = "Email is required."
    else:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
        if not re.match(email_pattern, data["Email"]):
            errors["Email"] = "Invalid email format."

    # validating Address
    if not data["Address"]:
        errors["Address"] = "Address is required."

    # validating Gender
    if not data["Gender"]:
        errors["Gender"] = "Gender is required."

    # validating Hobbies
    if not data["Hobbies"]:
        errors["Hobbies"] = "At least one hobby must be selected."
    # returning dictionary of errors
    return errors

def get_registration_data(text1, text2, text3, text4, gender, hobbies):
    ''' Function to get the data from the registration form '''
    name = text1.get("1.0", "end-1c")  # Get the text from the Name field
    contact = text2.get("1.0", "end-1c")  # Get the text from the Contact field
    email = text3.get("1.0", "end-1c")  # Get the text from the Email field
    address = text4.get("1.0", "end-1c")  # Get the text from the Address field
    gender_value = gender.get()  # Get the selected gender
    hobbies_selected = hobbies.curselection()  # Get the selected hobbies

    data = {
        "Name": name,
        "Contact": contact,
        "Email": email,
        "Address": address,
        "Gender": gender_value,
        "Hobbies": [hobbies.get(idx) for idx in hobbies_selected]
    }
    # returning data
    return data

