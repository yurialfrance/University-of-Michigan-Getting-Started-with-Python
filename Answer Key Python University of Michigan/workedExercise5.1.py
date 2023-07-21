val = 0
total = 0.0

while True:
    val = input("Enter a number: ")
    if val == 'done':
        break
    try:
     fval = float(val)
    except:
       print("Invalid Input")
       continue
    # print(fval)
    fval+=1
    total = total + fval

# print('All Done')
print(total,fval,total/fval)