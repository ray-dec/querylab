def load_questions(file) :
    """Read the file then load the questions"""
    with open(file, 'r') as f : 
        try :
            f.readlines()
        except :
            print("Somethin went wrong.") 

print(load_questions('/questions-tables.csv'))