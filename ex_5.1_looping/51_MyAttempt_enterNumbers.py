# what i tried to do


#start loop values
num = 0
total = 0.0
# input data
try :
    while True :
        line = input('Enter a number: ')
        number = float(line)
        print(number)
        if line[0] =='Invalid input' :
            continue
        if line == 'done' :
            break
except :
    print('Invalid input')
# count items on set
count=0
for itevar in 




# finding the number of items, total, and average
count=0
sum=0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)