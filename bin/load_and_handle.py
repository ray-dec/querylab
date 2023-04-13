import pandas as pd
import time

candidat_level = input('What is the level of the candidate ?  : ')

def load_questions(file=str, 
                   columns = str or list,
                   encoding='utf-8',
                   engine='openpyxl',
                   ) :
        """
This function reads the file from the given location and loads the questions.

Args
file (str) : The file path of the file to be read.
columns (str or list) : The columns to be used from the file.
encoding (str) : The encoding of the file.
engine (str) : The engine to be used for reading the file.

Returns
A DataFrame object containing the questions read from the file.
        """

        try :
                if file.endswith('.xlsx'):
                        data = pd.read_excel(file,
                                        usecols=['Questions','Difficulté'],
                                        engine=engine
                                        )
                        print(f"\n Questions have been well loaded from {file}.\n")
                        time.sleep(2)
                        return data
                
                elif file.endswith('.csv'):
                        data = pd.read_csv(file,
                                        usecols=['Questions','Difficulté'],
                                        encoding=encoding
                                        )
                        print(f"\n Questions have been well loaded from {file}.\n")
                        time.sleep(2)
                        return data
                
                else :
                        print('The file is not a csv nor xlsx. Please use this format.')

        except FileNotFoundError :
                print('Filepath passed does not exists. Check the location of the file and try again.')

        except NameError:    
                print("One or more arguments are incorrect.") 

def select_questions_and_randomize(data=None) : 
    """
This function takes in a dataframe of questions and returns a dataframe of randomly selected questions.

Args

data (optional) :  a dataframe of questions.

Returns

A dataframe of randomly selected questions.

    """
    # Initialize empty dataset
    randomized = pd.DataFrame()

    # Get unique difficulty levels from data
    difficulty_levels = set(data['Difficulté'])

    # Iterate over each difficulty level and sample two questions
    if candidat_level =='Junior':
        for level, i in difficulty_levels,range(1,3):
                randomized = pd.concat([
                data[data['Difficulté']==level].sample(2),
                randomized
                        ])
    elif candidat_level =='Confirmé':
        for level in difficulty_levels :
                randomized = pd.concat([
                data[data['Difficulté']==level].sample(2),
                randomized
                        ])

    else :
        for level in difficulty_levels :
                randomized = pd.concat([
                data[data['Difficulté']==level].sample(2),
                randomized
                        ])

           
    # randomly shuffles the elements of the randomized dataframe
    randomized = list(randomized['Questions'].sample(frac=1))

    return randomized
