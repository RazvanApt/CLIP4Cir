"""

go through images_not_found.txt
create an array of string for image names

go through the captions and image_splits json files
remove the records that have the image names of images not found

"""
import os
import json

def clearFromImageSplit(missing_files_names):
    path = "fashionIQ_dataset\\image_splits"
    
    output_path = "fashionIQ_dataset\\cleared"

    files = os.listdir(path)
    for file_name in files:
        print("Start cleaning: " + file_name)

        with open(path + "\\" +  file_name, 'r') as file:
            arr = json.load(file)

            result = []

            for i in arr:
                hasMissingFile = False
                for j in missing_files_names:
                    if i == j:
                        hasMissingFile = True
                        break
                if hasMissingFile == False:
                    result.append(i)


        output_file_name = file_name[4:]
        with open(output_path + '\\' + output_file_name, "w") as f:
            json.dump(result, f)

        print("Finish cleaning: " + file_name)



def clearFromCaptions(missing_files_names):

    path = "fashionIQ_dataset\\captions"
    
    output_path = "fashionIQ_dataset\\cleared"

    files = os.listdir(path)
    for file_name in files:
        print("Start cleaning: " + file_name)

        result = []

        with open(path + "\\" +  file_name, 'r') as file:
            arr = json.load(file)
            for item in arr:
                hasMissingFile = False
                for missing_file in missing_files_names:
                    if ('target' in item and item['target'] == missing_file) or ('candidate' in item and item['candidate'] == missing_file):
                        hasMissingFile = True
                        break
                if hasMissingFile == False:
                    result.append(item)

        output_file_name = file_name[4:]
        with open(output_path + '\\' + output_file_name, "w") as f:
            json.dump(result, f)

        print("Finish cleaning: " + file_name)


if __name__ == '__main__':
    missing_files_names = []

    file_name = "images_not_found.txt"

    file = open(file_name, 'r')

    for line in file:
        line_words = line.split()
        missing_files_names.append(line_words[0])

    print("Image Splits files:")
    clearFromImageSplit(missing_files_names)
    print()
    print("Captions files:")
    clearFromCaptions(missing_files_names)

