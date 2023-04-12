def load_questions(file) :
    """Read the file then load the questions"""
    with open(file, 'r') as f : 
        try :
            f.readlines()
        except :
            print("Somethin went wrong.") 
            

def select_randomly(qlist=pandas.Series) :
    """Select only 5 questions from the list of questions """
    qlist['random'] = qlist.apply(lambda x : np.random.random())
    qlist_selected = qlist.sort_values(by='random',ascending=True).head()
    return qlist_selected

def create_notebook(qlist=pandas.Series):
    """"Create a notebook with those 5 questions"""
