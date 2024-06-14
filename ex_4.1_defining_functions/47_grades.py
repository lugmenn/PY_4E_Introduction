def computegrade(sc) :
    score = float(sc)
    score <= 1.0 and score > 0
    if 1.0 >= score >= 0.9 :
        return 'A'
    elif 0.9 > score >= 0.8 :
        return 'B'
    elif 0.8 > score >= 0.7 :
        return 'C'
    elif 0.7 > score >= 0.6 :
        return 'D'
    elif 0.6 > score :
        return 'F'
    print(grade)
    
try : 
    sc = input('Enter score: ')
    grade = computegrade(sc)
    print(grade)
except :
    print('Bad score. Enter a numeric value between 0 and 1.0')