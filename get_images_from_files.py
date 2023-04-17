import urllib.request

def main():
    image_folder = '.\\images\\'
    file_extension = ".jpg"
    splits = ["dress", "shirt", "toptee"]

    not_found_file = "images_not_found.txt"

    missing_files = []

    for split in splits:
        file_name = "asin2url." + split + ".txt"

        file = open(file_name, 'r')

        for line in file:
            line_words = line.split()
            try:
                urllib.request.urlretrieve(line_words[1], image_folder + line_words[0] + file_extension)
            except:
                # print(f'{line_words[0]}\t{line_words[1]}')
                missing_image_str = f"{line_words[0]}\t{line_words[1]}"
                missing_files.append(missing_image_str)

        file.close()
        print(f"Done for {split}")

        with open(not_found_file, mode='wt') as myfile:
            myfile.write('\n'.join(missing_files))


if __name__ == '__main__':
    main()