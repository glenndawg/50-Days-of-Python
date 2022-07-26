# DAY 13 : PAY YOUR TAXES
# Write a function called your_vat. THe function takes no parameter.
# The function asks the user to input the price of an item and VAT.
# (VAT should be a percentage). THe function should return the price
# of the item plus VAT. If the price is 220 and, VAT is 15% your code 
# should return a vat invlusive price of 253. Make sure the code 
# can handle ValueError. Ensure the code runs until valid numbers 
# are entered. (HINT: Your code should include a while loop).

while True:
    try:
        price = round(float(input("Please enyter the price of the product :")),2)
        vat = round(float(input("Please enter the sales tax :")),2)
        break
    except ValueError:
        print("Please enter a valid number")

def your_vat(price, vat):
    pat = round(price + ((price * vat)/100), 2)
    return pat

print("Your price including sales tax is $ {:0.2f}" .format(your_vat(price,vat)))

# I can start putting the tr/except inside the def function. 
# try/except/else