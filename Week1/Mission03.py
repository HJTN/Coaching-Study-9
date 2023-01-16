score = [(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    for idx, info in enumerate(score):
        print(f'{idx+1}번, 평균 : {sum(info) / len(info)}')

get_avg(score)