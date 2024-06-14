def computepay(h, r):
    hours=float(h)
    rate=float(r)
    if hours > 40 :
        rp = 40 * rate
        op = (hours - 40) * (1.5 * rate)
        salary = rp + op
        return salary
    else :
        salary = hours * rate
        return salary

h = input("Enter Hours:")
r = input ("Enter Rate:")
p = computepay(h, r)
print("Pay", p)