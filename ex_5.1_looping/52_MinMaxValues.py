#this loop allows the user to enter any integer, and output the largest and smallest values

# starting values

largest = None
smallest = None

# start input loop
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        value = int(num)
        if largest is None :
            largest = value
        elif largest < value :
            largest = value
        elif smallest is None :
            smallest = value
        elif smallest > value :
            smallest = value
    # error message
    except :
        print ('Invalid input')
        continue

# print at end of loop
print('Maximum is', largest)
print('Minimum is', smallest)