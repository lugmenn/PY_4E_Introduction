try : 
    inp = input('Enter score: ')
    score = float(inp)
    score <= 1.0 and score > 0
    if 1.0 >= score >= 0.9 :
        grade = 'A'
    elif 0.9 > score >= 0.8 :
        grade = 'B'
    elif 0.8 > score >= 0.7 :
        grade = 'C'
    elif 0.7 > score >= 0.6 :
        grade = 'D'
    elif 0.6 > score :
        grade = 'F'
    print(grade)
except :
    print('Bad score. Enter a numeric value between 0 and 1.0')