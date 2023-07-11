from tkinter import *
import sqlite3


root = Tk()
root.geometry("400x600")
root.iconbitmap("icon.ico")
root.title("Database")

db = sqlite3.connect("address_book.db")
cursor = db.cursor()

def update():
    db = sqlite3.connect("address_book.db")
    cursor = db.cursor()

    record_id = delete_box.get()

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
         'last' : l_name_editor.get(),
         'address' : address_editor.get(),
         'city' : city_editor.get(),
         'state' : state_editor.get(),
         'zipcode' : zipcode_editor.get(),

         'oid' : record_id
         })


    db.commit()

    db.close()

    editor.destroy()

# Create Edit Function to Update a Record
def edit():
    global editor
    editor = Tk()
    editor.geometry("400x200")
    editor.iconbitmap("icon.ico")
    editor.title("Edit A Record")

    # Create a database or connect to one
    db = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = db.cursor()

    record_id = delete_box.get()

    # Query The Database
    cursor.execute(f"SELECT * FROM addresses WHERE oid = {record_id}")
    records = cursor.fetchall()

    # Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create A Text Box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)


    # Create Text Box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # Create a Save Button To Save Edited Record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Loop Thru Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


# Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    db = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = db.cursor()

    # Delete a record
    cursor.execute(f"DELETE from addresses WHERE oid={delete_box.get()}")




    # Commit changes
    db.commit()

    # Close Connection
    db.close()

# Create Submit Function For Database
def submit():

    # Create a database or connect to one
    db = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = db.cursor()

    # Insert Into Table
    db.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
               {
                   'f_name': f_name.get(),
                   'l_name': l_name.get(),
                   'address': address.get(),
                   'city': city.get(),
                   'state': state.get(),
                   'zipcode': zipcode.get()
               })

    # Commit changes
    db.commit()

    # Close Connection
    db.close()

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def query():
    # Create a database or connect to one
    db = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = db.cursor()

    # Query The Database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    #print(records)

    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    # Commit changes
    db.commit()

    # Close Connection
    db.close()

# Create Text Boxes

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="ID Number")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=109)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# Commit changes
db.commit()

# Close Connection
db.close()

root.mainloop()