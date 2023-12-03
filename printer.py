import tkinter as tk
import sqlite3

def display_data():
    # Create a connection with the database
    conn = sqlite3.connect('Your-database')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # SQL statement to fetch data
    cursor.execute('SELECT * FROM registration')

    # Fetch all the rows as a list of tuples
    data = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Create a new window to display and update the data
    data_window = tk.Tk()
    data_window.title("Data from Database")
    data_window.config(bg="#8B0000")

    def update_data(entry_fields):
        # Create a new connection and cursor
        conn_update = sqlite3.connect('Your-database')
        cursor_update = conn_update.cursor()

        # SQL statement to update data
        update_query = "UPDATE registration SET name=?, contact=?, email=?, address=?, gender=?, hobbies=? WHERE id=?"

        # Extract values from entry fields
        updated_values = [entry.get() for entry in entry_fields]

        # Execute the update query with the correct number of bindings
        cursor_update.execute(update_query, tuple(updated_values)[1:] + (updated_values[0],))

        # Commit changes to the database
        conn_update.commit()

        # Close the connection
        conn_update.close()

        # Refresh the displayed data after updating
        data_window.destroy()
        display_data()

    # Function to delete data from the database
    def delete_data():
        # Create a new connection and cursor
        conn_delete = sqlite3.connect('Your-database')
        cursor_delete = conn_delete.cursor()

        # SQL statement to delete data
        delete_query = "DELETE FROM registration WHERE id=?"
        cursor_delete.execute(delete_query, (row[0],))

        # Commit changes and close the connection
        conn_delete.commit()
        conn_delete.close()

        # Refresh the displayed data after deleting
        data_window.destroy()
        display_data()
    # Display headers
    for col_idx, col in enumerate(columns):
        header_label = tk.Label(data_window, text=col, bg="#8B0000", fg="white")
        header_label.grid(row=0, column=col_idx, padx=5, pady=5)

    # Display rows with update and delete buttons
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            cell_label = tk.Label(data_window, text=str(value), bg="#8B0000", fg="white")
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5)

        # Entry fields for editing each column
        entry_fields = []
        for col_idx, value in enumerate(row):
            entry = tk.Entry(data_window)
            entry.insert(0, str(value))
            entry_fields.append(entry)
            entry.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5)

        # Button to update the data
        update_button = tk.Button(data_window, text="Update", command=lambda entries=entry_fields: update_data(entries))
        update_button.grid(row=row_idx + 1, column=len(columns), padx=5, pady=5)

        # Button to delete the data
        delete_button = tk.Button(data_window, text="Delete", command=delete_data)
        delete_button.grid(row=row_idx + 1, column=len(columns) + 1, padx=5, pady=5)

    # Start the Tkinter main loop to display the window
    data_window.mainloop()
