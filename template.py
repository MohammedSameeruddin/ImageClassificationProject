import os
from pathlib import Path
import logging



logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

Project_Name ='cnnClassifier'

list_of_files=[
    ".github/workflow/.getkeep",
    f"src{Project_Name}/__init__.py",
    f"src{Project_Name}/component/__init__.py",
    f"src{Project_Name}/utils/__init__.py",
    f"src{Project_Name}/config/configuration.py",
    f"src{Project_Name}/pipeline/__init__.py",
    f"src{Project_Name}/entity/__init__.py",
    f"src{Project_Name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "test.txt"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir !="":
            os.makedirs(filedir,exist_ok=True)
           # logging.INFO("created file directory with name successfully")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
          with open(filepath,"w") as f:
                pass
              #  logging.INFO("file created successfully ")
    else:
        logging.INFO("file  already exists")

            



        

      