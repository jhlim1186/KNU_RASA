import pandas as pd
import random as rd

quiz = pd.read_csv('C:/Users/riverame/Downloads/project/.rasa/quiz.csv',encoding='CP949')
quiz = quiz.dropna(axis=1)

## quiz_num : index 번호를 list 형태로 출력
def GetQuiz():
    problem_total_num = len(quiz.index)
    quiz_num = rd.randint(0,problem_total_num)
    
    return quiz_num

## problems : quiz_num 인덱스 번호에 따른 문제 출력
def Getproblem(quiz_num):
    problems = str(quiz.iloc[quiz_num][0])
        
    return problems

## answer : quiz_num 인덱스 번호에 따른 정답 출력
def Getanswer(quiz_num):
    answer = str(quiz.iloc[quiz_num][1])
    
    return answer