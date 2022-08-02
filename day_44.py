# Day 44: Save Emails
# Create a function called save_emails. This function takes no
# arguments but asks the user to input email, and it saves the emails
# in a CSV file. The user can input as many emails as they want. Once
# hey hit ‘done’ the function saves the emails and closes the file.
# Create another function called open_emails. This function opens
# and reads the content of the CSV file. Each email must be in its line.
# Here is an example of how the emails must be saved:
from csv import reader
import csv

file = "emai_list.csv"
fields = ['email']
email_list = []
row = None

def save_emails():
    while True:
        row = input("Please enter an email (enter done when finished) :")
        # check here for email format
        if row in ('done','DONE'): break
        email_list.append(row)

    with open('email_list.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows([item] for item in email_list) # keep from csv the chars
        file.close()

def open_emails():
    with open('email_list.csv', 'r') as obj:
        csv_reader = reader(obj)
        for row in csv_reader:
            print(''.join(row))


save_emails()
open_emails()
    


        
