#Project 1: SQLite with Python on VS Code
#Built on Python ver 3.9.6 64-bit
#Co-created with Github Copilot
#Purpose: To create a database named client.db, create a table named clients with 3 columns, insert client records into the table, query the database and return all records, write the records to a CSV file, use 'SELECT rowid' to query the database and return selected records, and write the selected records to a new CSV file.  
#Output: client.db, clients_data.csv, clients_data_selected.csv


#Import SQLite3 module & connect to a database named client
import sqlite3
import csv
import os

#Practise Purpose Only!
# Remove the database and CSV file if they exist
os.remove('client.db')
os.remove('clients_data.csv')
os.remove('clients_data_selected.csv')

conn = sqlite3.connect('client.db')


#Create a cursor that points to the database. Create a table named clients with 3 columns
pointer = conn.cursor()
pointer.execute("""CREATE TABLE clients ( 
    first_name text,
    last_name text,
    email text
    )""")
conn.commit()
#After this point, client.db should be created)

#Insert client records into the table clients
many_clients = [
    ('Elon', 'Musk', 'elon@musk.com'),
    ('Jeff', 'Bezos', 'jeff@bezos.com'),
    ('Bill', 'Gates', 'bill@gates.com'),
    ('Steve', 'Jobs', 'steve@jobs.com')    
]
pointer.executemany("INSERT INTO clients VALUES (?,?,?)", many_clients) 
conn.commit()

pointer.execute("SELECT * FROM clients")
pointer.fetchall()
conn.commit()

#Query the database and return all records
conn = sqlite3.connect('client.db')
pointer = conn.cursor()
pointer.execute("SELECT * FROM clients")
rows = pointer.fetchall()

#Write the records to a CSV file
csv_file_path = 'clients_data.csv'

with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([['First Name', 'Last Name', 'Email']])
    csv_writer.writerows(rows)    

conn.commit()

#Use 'SELECT rowid' to query the database and return selected

conn = sqlite3.connect('client.db')
pointer = conn.cursor()

pointer.execute("SELECT rowid, * FROM clients WHERE first_name LIKE '%e%'")
items = pointer.fetchall()
for item in items:
    print(item)

new_csv_file_path = 'clients_data_selected.csv'

with open(new_csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows([['Row ID', 'First Name', 'Last Name', 'Email']])
    csv_writer.writerows(items) 

conn.commit()
conn.close()

