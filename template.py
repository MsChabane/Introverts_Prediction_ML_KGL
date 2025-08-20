import os 
from pathlib import  Path

files = [
    "data/raw/.gitkeep",
    "data/cleaned/.gitkeep",
    'data/processed/.gitkeep',
    'notebook/.gitkeep',
    'reports/.gitkeep',
    'models/.gitkeep',
    'src/ml_introvert/__init__.py',
    'src/ml_introvert/utils/.gitkeep',
    'src/ml_introvert/constant/.gitkeep',
    'src/ml_introvert/pipeline/data/.gitkeep',
    'src/ml_introvert/pipeline/features/.gitkeep',
    'src/ml_introvert/pipeline/model/.gitkeep',
    'setup.py',
    'main.py',
    'params.yaml',
    'dvc.yaml',
    'app.py',
    'README.md',
    '.gitignore',
    'template.py',
    'requirements.txt',
]

for file in files:
    file = Path(file)
    print(file)
    dirs,_=os.path.split(file)
    if dirs != '':
        
        os.makedirs(dirs,exist_ok=True)
    if not os.path.exists(file) or os.path.getsize(file)==0 :
        with open(file,'w') as f :
            pass