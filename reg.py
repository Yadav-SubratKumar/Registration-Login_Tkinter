''' Registration and login form in tkinter '''
import tkinter as tk
from validate import get_registration_data, validate_data
from database import insert_data, logindetails
from printer import display_data
# Create dictionaries to store text fields and their corresponding error labels
text_fields = {}
error_labels = {}

def createMain():
    top = tk.Tk()
    top.title("Register Yourself")
    top.geometry('500x500')
    top.configure(bg="#8B0000")
    # header/title
    header = tk.Label(top, text="Registration Form", font=(
        "serif", 17), padx=35, pady=1, bg="#8B0000", fg="white")
    header.pack()
    # Name section
    name = tk.Label(top, text="Name:", padx=5, pady=1,
                        bg="#8B0000", fg="white", font=13)
    name.place(x=30, y=50)
    text1 = tk.Text(top, bg="white", bd=0, width=30,
                        fg="black", height=1, padx=5, pady=1)
    text1.place(x=150, y=50)
    # Error label for name
    name_error_label = tk.Label(
        top, text="", bg="#8B0000", fg="white", font=("Helvetica", 8))
    name_error_label.place(x=150, y=70)
    text_fields['Name'] = text1
    error_labels['Name'] = name_error_label
    text1.bind("<FocusOut>", lambda event,
                field="Name": validate_field(event, field))

    # Contact section
    contact = tk.Label(top, text="Contact:", padx=5,
                        pady=1, bg="#8B0000", fg="white", font=13)
    contact.place(x=30, y=90)
    text2 = tk.Text(top, bg="white", bd=0, width=30,
                        fg="black", height=1, padx=5, pady=1)
    text2.place(x=150, y=90)
    # Error label for contact
    contact_error_label = tk.Label(
        top, text="", bg="#8B0000", fg="white", font=("Helvetica", 8))
    contact_error_label.place(x=150, y=110)
    text_fields['Contact'] = text2
    error_labels['Contact'] = contact_error_label
    text2.bind("<FocusOut>", lambda event,
                field="Contact": validate_field(event, field))

    # Email section
    email = tk.Label(top, text="Email:", padx=5,
                        pady=1, bg="#8B0000", fg="white", font=13)
    email.place(x=30, y=130)
    text3 = tk.Text(top, bg="white", bd=0, width=30,
                        fg="black", height=1, padx=5, pady=1)
    text3.place(x=150, y=130)
    # Error label for email
    email_error_label = tk.Label(
        top, text="", bg="#8B0000", fg="white", font=("Helvetica", 8))
    email_error_label.place(x=150, y=150)
    text_fields['Email'] = text3
    error_labels['Email'] = email_error_label
    text3.bind("<FocusOut>", lambda event,
                field="Email": validate_field(event, field))

    # Address section
    address = tk.Label(top, text="Address:", padx=5,
                        pady=1, bg="#8B0000", fg="white", font=13)
    address.place(x=30, y=170)
    text4 = tk.Text(top, bg="white", bd=0, width=30,
                        fg="black", height=3, padx=5, pady=1)
    text4.place(x=150, y=170)
    # Error label for address
    address_error_label = tk.Label(
        top, text="", bg="#8B0000", fg="white", font=("Helvetica", 8))
    address_error_label.place(x=150, y=220)
    text_fields['Address'] = text4
    error_labels['Address'] = address_error_label
    text4.bind("<FocusOut>", lambda event,
                field="Address": validate_field(event, field))

    # Gender section
    gender = tk.Label(top, text="Gender:", padx=5,
                        pady=1, bg="#8B0000", fg="white", font=13)
    gender.place(x=30, y=245)
    g_val = tk.StringVar()
    tk.Radiobutton(top, text="Male", variable=g_val, value="Male",
                bg="#8B0000", fg="white", selectcolor='black').place(x=150, y=245)
    tk.Radiobutton(top, text="Female", variable=g_val, value="Female",
                bg="#8B0000", fg="white", selectcolor='black').place(x=220, y=245)
    tk.Radiobutton(top, text="Others", variable=g_val, value="Other",
                bg="#8B0000", fg="white", selectcolor='black').place(x=300, y=245)
    g_val.set("Male")

    # Subject section
    subject = tk.Label(top, text="Subjects :-", padx=5,
                        pady=1, bg="#8B0000", fg="white", font=13)
    subject.place(x=30, y=280)

    # Use IntVar to store subject selections
    c_selected = tk.IntVar()
    java_selected = tk.IntVar()
    python_selected = tk.IntVar()
    other_selected = tk.IntVar()

    c = tk.Checkbutton(top, text='C', variable=c_selected, onvalue=1,
                        offvalue=0, padx=5, pady=1, bg="#8B0000", fg="white", selectcolor='black')
    c.place(x=150, y=280)
    java = tk.Checkbutton(top, text='Java', variable=java_selected, onvalue=1,
                            offvalue=0, padx=5, pady=1, bg="#8B0000", fg="white", selectcolor='black')
    java.place(x=220, y=280)
    python = tk.Checkbutton(top, text='Python', variable=python_selected,
                                onvalue=1, offvalue=0, padx=5, pady=1, bg="#8B0000", fg="white", selectcolor='black')
    python.place(x=290, y=280)
    ot_subject = tk.Checkbutton(top, text='Other', variable=other_selected,
                                    onvalue=1, offvalue=0, padx=5, pady=1, bg="#8B0000", fg="white", selectcolor='black')
    ot_subject.place(x=360, y=280)

    # Set default selections
    c_selected.set(1)
    java_selected.set(1)

    # Hobbies section
    hobbies_label = tk.Label(
        top, text="Hobbies:", padx=5, pady=1, bg="#8B0000", fg="white", font=13)
    hobbies_label.place(x=30, y=320)
    hobbies = tk.Listbox(top, height=4, width=30, bg="white",
                            activestyle='dotbox', font="Helvetica", fg="black")
    hobbies.insert(1, "Dancing")
    hobbies.insert(2, "Singing")
    hobbies.insert(3, "Sports")
    hobbies.insert(4, "Other")
    hobbies.place(x=150, y=320)
    default_hobby = "Other"
    for index, hobby in enumerate(hobbies.get(0, "end")):
        if hobby == default_hobby:
            hobbies.select_set(index)



    def submit_registration():
        ''' Function to call the validate and insert function '''
        registration_data = get_registration_data(
            text_fields['Name'],
            text_fields['Contact'],
            text_fields['Email'],
            text_fields['Address'],
            g_val,
            hobbies
        )
        validation_errors = validate_data(registration_data)

        # Clear error labels
        for field, error in error_labels.items():
            error.config(text="")

        if validation_errors:
            # Handle validation errors and display them in the respective error labels
            for field, error_message in validation_errors.items():
                error_labels[field].config(text=error_message)
        else:
            # Data is valid, show a confirmation window with entered data
            show_registration_data()


    def show_registration_data():
        data_window = tk.Toplevel()
        data_window.configure(bg='#8D0000')
        data_window.title("Registration Data Confirmation")

        # Get the registration data
        registration_data = get_registration_data(
            text_fields['Name'],
            text_fields['Contact'],
            text_fields['Email'],
            text_fields['Address'],
            g_val,
            hobbies
        )

        # Create StringVar variables for editable fields
        name_var = tk.StringVar(value=registration_data['Name'])
        contact_var = tk.StringVar(value=registration_data['Contact'])
        email_var = tk.StringVar(value=registration_data['Email'])
        address_var = tk.StringVar(value=registration_data['Address'])

        # Display the registration data in entry widgets for editing
        tk.Label(data_window, text="Name:", bg="#8B0000", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(data_window, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(data_window, text="Contact:", bg="#8B0000", fg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(data_window, textvariable=contact_var).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(data_window, text="Email:", bg="#8B0000", fg="white").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(data_window, textvariable=email_var).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(data_window, text="Address:", bg="#8B0000", fg="white").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(data_window, textvariable=address_var).grid(row=3, column=1, padx=5, pady=5)
        # Display other registration data in labels (non-editable)
        tk.Label(data_window, text=f"Gender: {registration_data['Gender']}", bg="#8B0000", fg="white").grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        tk.Label(data_window, text="Hobbies:", bg="#8B0000", fg="white").grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        hobbies_list = tk.Listbox(data_window, height=4, width=30, bg="white", activestyle='dotbox', font="Helvetica", fg="black")
        hobbies_list.insert(1, "Dancing")
        hobbies_list.insert(2, "Singing")
        hobbies_list.insert(3, "Sports")
        hobbies_list.insert(4, "Other")
        hobbies_list.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        
        default_hobby = "Other"
        for index, hobby in enumerate(hobbies_list.get(0, "end")):
            if hobby == default_hobby:
                hobbies_list.select_set(index)

        # Add a button to confirm registration and insert data into the database
        def confirm_registration():
            # Get the updated data
            updated_data = {
                'Name': name_var.get(),
                'Contact': contact_var.get(),
                'Email': email_var.get(),
                'Address': address_var.get(),
                'Gender': g_val.get(),
                'Hobbies': [hobbies_list.get(index) for index in hobbies_list.curselection()]
            }

            # Insert the updated data into the database
            insert_data(updated_data)

            # Close the pop-up window
            data_window.destroy()

            # Show the success window
            success()

        tk.Button(data_window, text="Confirm Registration", padx=15, pady=5, bg="black", fg="white",
                command=confirm_registration).grid(row=4, column=0, columnspan=2, pady=10)

        # Add a button to close the pop-up window
        tk.Button(data_window, text="Close", padx=15, pady=5, bg="black", fg="white",
                command=data_window.destroy).grid(row=5, column=0, columnspan=2, pady=10)


    def success():
        ''' Function for displaying the Successful registration message'''
        success_window = tk.Tk()
        success_window.configure(bg='#8D0000')
        success_window.title("Registration Successful")

        def on_show_click(window_close):
            window_close.destroy()
            login()

        # Create a label to display the success message
        success_label = tk.Label(
            success_window, text="Data has been successfully registration.",
            bg="#8B0000", fg="white")
        success_label.pack(padx=20, pady=20)
        success_window.geometry("300x100+510+290")
        exitbtn = tk.Button(success_window, text="Exit", padx=18, pady=7, bg="black", fg="white",
                            activebackground="white", activeforeground="black", command=success_window.destroy)
        exitbtn.place(x=60, y=60)
        log = tk.Button(success_window, text="Login", padx=15, pady=7, bg="black", fg="white",
                            activebackground="white", activeforeground="black", command=lambda: on_show_click(success_window))
        log.place(x=170, y=60)
        top.destroy()


    def details(uname):
        '''Function to show data after Successful login '''
        details_window = tk.Tk()
        details_window.configure(bg='#8D0000')
        details_window.title("Login Successful")
        details_window.geometry("300x100+510+290")

        def on_show_click(window_close):
            window_close.destroy()
            display_data()

        # Create a label to display the success message
        details_label = tk.Label(
            details_window, text=f'Welcome {uname}, Login Successful', bg="#8B0000", fg="white")
        details_label.pack(padx=20, pady=20)
        show = tk.Button(details_window, text="Show data", padx=15, pady=10, bg="black", fg="white",
                            activebackground="white", activeforeground="black", command=lambda: on_show_click(details_window))
        show.pack(pady=5, padx=20)
        # Start the Success to display the window
        details_window.mainloop()


    def login():
        """Checks the login details of the user."""

        # Create a login window
        login_window = tk.Tk()
        login_window.configure(bg='#8D0000')
        login_window.geometry('500x400')
        login_window.title("Login Form")

        # Define a function to close the login window and open the details window
        def on_show_click(window_close):
            # Get the values of username and email when the login button is clicked
            username = logtext1.get("1.0", "end-1c")
            useremail = logtext2.get("1.0", "end-1c")

            login_details = {"username": username, "email": useremail}
            true ,uname = logindetails(login_details)
            if true:
                window_close.destroy()
                details(uname)
            else:
                error_label = tk.Label(
                    login_window, text="**Login failed. Please check your credentials.**", fg="white", padx=20, pady=5, bg='#8D0000')
                error_label.place(x=120, y=170)

        # Create header label
        logheader = tk.Label(login_window, text="Login Form", font=(
            "serif", 16), padx=35, pady=1, bg="#8B0000", fg="white")
        logheader.pack()

        # Create login name label and text box
        logname = tk.Label(login_window, text="Name:",
                            padx=5, pady=1, bg="#8B0000", fg="white", font=13)
        logname.place(x=30, y=50)
        logtext1 = tk.Text(login_window, bg="white",
                            bd=0, width=30, fg="black", height=1, padx=5, pady=1)
        logtext1.place(x=120, y=50)

        # Create login email label and text box
        logemail = tk.Label(login_window, text="Email:",
                                padx=5, pady=1, bg="#8B0000", fg="white", font=13)
        logemail.place(x=30, y=80)
        logtext2 = tk.Text(login_window, bg="white",
                            bd=0, width=30, fg="black", height=1, padx=5, pady=1)
        logtext2.place(x=120, y=80)

        # Create a cancel button
        tk.Button(login_window, text="Cancel", padx=15, pady=5, command=login_window.destroy,
                bg="black", fg="white", activebackground="white", activeforeground="black").place(x=120, y=130)

        log = tk.Button(login_window, text="Login", padx=15, pady=5, bg="black",
                            fg="white", activebackground="white", activeforeground="black", command=lambda: on_show_click(login_window))
        log.place(x=250, y=130)
        reg_btn = tk.Button(login_window, text="Register", padx=15, pady=5, bg="black",
                            fg="white", activebackground="white", activeforeground="black", command=lambda:(login_window.destroy(),createMain()))
        reg_btn.place(x=370, y=130)

        # Start the mainloop
        login_window.mainloop()


    def validate_field(event, field_name):
        '''Function to validate and display errors dynamically'''
        registration_data = get_registration_data(
            text_fields['Name'],
            text_fields['Contact'],
            text_fields['Email'],
            text_fields['Address'],
            g_val,
            hobbies
        )
        validation_errors = validate_data(registration_data)

        for error in error_labels.values():
            error.config(text="")

        if field_name in validation_errors:
            error_labels[field_name].config(
                text=validation_errors[field_name])


    # Button section
    tk.Button(top, text="Cancel", padx=15, pady=5, command=top.destroy, bg="black",
            fg="white", activebackground="white", activeforeground="black").place(x=160, y=415)
    tk.Button(top, text="Register", padx=15, pady=5, bg="black", fg="white",
            activebackground="white", activeforeground="black", command=submit_registration).place(x=250, y=415)
    tk.Button(top, text="Login", padx=15, pady=5, bg="black", fg="white",
            activebackground="white", activeforeground="black", command=lambda: (top.destroy(), login())).place(x=340, y=415)


    top.mainloop()

createMain()