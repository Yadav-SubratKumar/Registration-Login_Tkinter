import sqlite3
# Created a connection with database
conn = sqlite3.connect('Your-Database')

# Create a table for registration data
cursor = conn.cursor()
"""
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registration (
        id INTEGER PRIMARY KEY,
        name TEXT,
        contact VARCHAR,
        email TEXT,
        address TEXT,
        gender TEXT,
        hobbies TEXT
    )
''')
"""
# Function to insert data in database


def insert_data(data):
    ''' Create a table for registration data '''
    conn = sqlite3.connect('Your-Database')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO registration (name, contact, email, address, gender, hobbies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data["Name"], data["Contact"], data["Email"],
          data["Address"], data["Gender"], ', '.join(data["Hobbies"])))
    conn.commit()
    conn.close()


def logindetails(login_details):
    """Displays the details of the user.
    Args:
    login_details: A dictionary containing the login details of the user.
    """
    # Create a table for registration data
    conn = sqlite3.connect('Your-Database')
    cursor = conn.cursor()
    # Get the login name and email from the dictionary
    logname = login_details["username"]
    logemail = login_details["email"]

    # Check if the user exists in the database
    query = "SELECT * FROM registration WHERE name = ? AND email = ?"
    cursor.execute(query, (logname, logemail))
    num_rows = cursor.fetchall()
    # If there are any rows, then the user exists
    if num_rows:
        return True, logname

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    return False
