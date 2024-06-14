# excute only if data entry was correct
try :
    inp1 = input('Enter Hours:\n')
    hours = float(inp1)
    inp2 = input('Enter Rate:\n')  
    rate = float(inp2)
    # print overtime salary
    if hours > 40 :
        # calculate regular pay
        rp = 40 * rate
        # calculate overtime pay
        op = (hours - 40) * (1.5 * rate)
        # calculate total payment
        tp = rp + op
    else:
        tp = hours * rate
    print('Total Pay: $',tp)
# error message
except :
    print('Error, please enter numeric input')