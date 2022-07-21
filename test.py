# value = -12345672
# print (format (value, ',d'))

# print(f'{value:,}')

a = "12345672"
e = list(a.split(".")[0])
for i in range(len(e))[::-3][1:]:
    e.insert(i+1,",")
print(result = "".join(e)+"."+a.split(".")[1])

