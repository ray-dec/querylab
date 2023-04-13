from bin.load_and_handle import load_questions, select_questions_and_randomize
from bin.create_notebook import create_notebook

def main():
    load_questions('querylab/sample/questions_table.csv')
    select_questions_and_randomize()
    create_notebook() 
    

