from src.img import images
import nbformat as nbf

def create_notebook(questions=list, 
                    filepath='./',
                    name='Rayane Declercq'):

    nb = nbf.v4.new_notebook() 

    with open('querylab/bin/src/introduction.txt', 'r',
            encoding='utf-8') as f : 
        intro = f.readlines()

    img1,img2,img3 = images()

    items = [img1,intro,img2,img3]

    nb['cells'] = [nbf.v4.new_markdown_cell(i) for i in items]

    for i in range (1,6) :
        text = nbf.v4.new_markdown_cell( 
            f"""### Question {i} : """)
        code = nbf.v4.new_code_cell(
            """%%bigquery --project $project  --verbose \n\n--Write below your SQL query :"""
        )
        nb['cells'].extend([text,code])
        
        if filepath.endswith('/') :
            nbf.write(nb, f'{filepath}SQL Test - {name}.ipynb')
        else :
            nbf.write(nb, f'{filepath}/SQL Test - {name}.ipynb')

    return print(f'Notebook have been created at {filepath}')

