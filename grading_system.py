def determine_grade(scores):
    if scores >= 80 and scores <=100:
        print('A+'+'\t4.00'+'\tOutstanging')
    elif scores >= 75 and scores < 80:
        print('A'+'\t3.750'+'\tExcellent')
    elif scores >= 70 and scores < 75:
        print('A-'+'\t3.50'+'\tVery good')
    elif scores >= 65 and scores < 70:
        print('B+'+'\t3.25'+'\tGood')
    elif scores >= 60 and scores < 65:
        print('B'+'\t3.00'+'\tSatisfactory')
    elif scores >= 55 and scores < 60:
        print('B-'+'\t2.75'+'\tAbove average')
    elif scores >= 50 and scores < 55:
        print('C+'+'\t2.50'+'\tAverage')
    elif scores >= 45 and scores < 50:
        print('C'+'\t2.25'+'\tBellow Average')
    elif scores >= 40 and scores < 45:
        print('D'+'\t2.00'+'\tPass')
    else:
        print('F'+'\t00'+'\tFail')
scores = int(input())   
determine_grade(scores)