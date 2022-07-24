# DAY 5 : MY DISCOUNT
# Create a function called my_discount. The Function takes no
# argument but asks the user to inout the price and the discount
# (percentage) of the product. Once the user inputs the price and
# discount, it calculates the price after the discount. The function
# should return thr price after the discount. For exampe, if the user
# enters 150 as the price and 15% as the discount, your function should
# return 127.5

def my_discount(price, discount):
    dis_price = round(price - price * (discount/100), 2)
    return dis_price

price = round(float(input("Please enter the price :")), 2)
discount = round(float(input("Plese enter the discount percentage :")), 2)

print(f"The disounted price is : ${my_discount(price,discount)}")

# this seems rather straight forward

