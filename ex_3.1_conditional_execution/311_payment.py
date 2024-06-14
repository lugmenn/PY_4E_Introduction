inp1 = input('Enter Hours:\n')
inp2 = input('Enter Rate:\n')  
hours = float(inp1)
rate = float(inp2)
# print overtime salary
if hours > 40 :
    print ('Overtime')
    # calculate regular pay
    rp = 40 * rate
    print('Regular Payment: $',rp)
    # calculate overtime pay
    op = (hours - 40) * (1.5 * rate)
    print('Overtime Payment: $',op)
    # print total payment
    tp = rp + op
else:
    tp = hours * rate
print('Total Pay: $',tp)