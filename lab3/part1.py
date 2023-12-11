import os
import csv
from typing import List

def Get_Absolute_Path(name: str) -> List[str]:
    name_absolute_path=os.path.abspath(f"dataset/{name}")
    image_names = os.listdir(name_absolute_path)

    image_absolute_paths = list(map(lambda img: os.path.join(name_absolute_path, img), image_names))
    
    return image_absolute_paths

def Get_Relative_Path(name: str) -> List[str]:
    name_relative_path=os.path.relpath(f"dataset/{name}")
    image_names = os.listdir(name_relative_path)

    image_relative_paths = list(map(lambda img: os.path.join(name_relative_path, img), image_names))

    return image_relative_paths
    
def Create_Annotation() -> None:
    polarbear='polarbear'
    brownbear='brownbear'

    polarbear_absolute_paths = Get_Absolute_Path(polarbear)
    polarbear_relative_paths = Get_Relative_Path(polarbear)
    brownbear_absolute_paths = Get_Absolute_Path(brownbear)
    brownbear_relative_paths = Get_Relative_Path(brownbear)

    with open('annotation.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for absolute_path, relative_path in zip(polarbear_absolute_paths, polarbear_relative_paths):
            writer.writerow([absolute_path, relative_path, polarbear])

        for absolute_path, relative_path in zip(brownbear_absolute_paths, brownbear_relative_paths):
            writer.writerow([absolute_path, relative_path, brownbear])
