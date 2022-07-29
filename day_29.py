# DAY 29 : MIDDLE FIGURE
# Write a function called middle_figure that takes two parameters a,
# and b. The two parameters are strings. The function joins the two
# strings and finds the middle element. If the combined string has a
# middle element, the function should return the element, otherwise,
# return 'no middle figure'. Use 'make love' as an argument for a and
# 'not wars' as an argument for b. Your function should return 'e' as 
# the middle element. White spaces should be removed.

a = 'make love'
b = 'not wars dude'

def middle_figure(a,b):
    l = (a+b).replace(' ','')
    if len(l) % 2 == 0:
        print("no middle figure")
    else:
        print(f"The middle figure is : {l[int(len(l)//2)]}")

middle_figure(a,b)
