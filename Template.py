import os #used for file and folder operation
from pathlib import Path # Path handling for windows and linux
import logging # Status message of code eg: Dir created succesfully

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # Increases Readablity

project_name = "mlProject" 

list_of_files = [
".github/workflows/.gitkeep",
f"src/{project_name}/_init__.py", # Automating the project structure
f"src/{project_name}/components/ __init__.py",
f"src/{project_name}/utils/_init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/config/_init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/_init__.py",
f"src/{project_name}/entity/init__.py",
f"src/{project_name}/entity/config_entity.py",
f"src/{project_name}/constants/_init__.py",
"config/config.yaml",
"params.yaml",
"schema.yaml",
"main.py",
"app.py",
"Dockerfile",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) # convert string path to object path.
    filedir, filename = os.path.split(filepath) # Seperating folder name and file name
    

    if filedir != "": # Folder missing, create
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f: # if file missing or file size is 0, create file
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exist") # Otherwise file already exist