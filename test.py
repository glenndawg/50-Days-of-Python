import csv

file = "emai_list.csv"
fields = ['email']
email_list = []
row = None

while True:
    row = input("Please enter an email (enter done when finished) :")
    # check here for email format
    if row in ('done','DONE'): break
    email_list.append(row)

with open('email_list.csv', 'w', encoding='UTF8') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(email_list)):
        writer.writerow(email_list[i])

print(email_list)