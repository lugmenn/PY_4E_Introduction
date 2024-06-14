#this loop allows the user to enter any numerical values, and output the total of values entered, total and average

#start loop values

num = 0
total = 0.0

# input data
while True :
    line = input('Enter a number: ')
    if line == 'done' :
        break
    try :
        number = float(line)
    except :
        print('Invalid input')
        continue
    # values to be found
    num = num + 1
    total = total + number

# print after completed loop   
print('Number of items', num, 'Total', total, 'Avg', total/num)