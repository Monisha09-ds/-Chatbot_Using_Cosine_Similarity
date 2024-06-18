from main import QASystem
import pandas as pd
import csv

def chatbot(inp):
    qa = QASystem('test.csv')
    try:
        qa_response = qa.get_response(inp)
        print("Try")
    except:
        qa_response = "I am unable to ans the question"
        print('Except')
           #df = pd.DataFrame([['"' + input + '"', '"' + reply + '"']], columns=['Questions'])
            #df.to_csv('bank.csv', mode='a', header=False, index=False)
            
    return qa_response