import os
import shutil
import csv
import random

random_numbers = random.sample(range(0, 10000), 2391)
new_names = [f'{number}.jpg' for number in random_numbers]

def create_dataset_3(select_folder) -> None:

    if os.path.isdir(select_folder):
        shutil.rmtree(select_folder)

    old_path = os.path.relpath('dataset_2')
    new_path = os.path.relpath(select_folder)
    shutil.copytree(old_path, new_path)

    old_names = os.listdir(new_path)
    
    old_relative_paths = list(map(lambda name: os.path.join(new_path, name), old_names))
    
    new_relative_paths = list(map(lambda name: os.path.join(new_path, name), new_names))

    for old_name, new_name in zip(old_relative_paths, new_relative_paths):
        os.replace(old_name, new_name)



def create_annotation_3() -> None:

    old_path = os.path.relpath('dataset_2')
    old_names = os.listdir(old_path)
    old_relative_paths = list(map(lambda name: os.path.join(old_path, name), old_names))

    
    new_path = os.path.relpath('dataset_3')
    new_relative_paths = list(map(lambda name: os.path.join(new_path, name), new_names))

    new_absolute_paths = list(map(lambda img: os.path.join(os.path.abspath('dataset3'), img), new_names))

    with open('annotation_3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for  absolute_path, relative_path, old_relative_path in zip(new_absolute_paths, new_relative_paths, old_relative_paths):
            if 'polarbear' in old_relative_path:
                name = 'polar bear'
            else:
                name = 'brownbear'
            writer.writerow([absolute_path, relative_path, name])


if __name__ == "__main__":
    create_dataset_3()
    create_annotation_3()

