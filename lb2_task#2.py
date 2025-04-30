import hashlib
#file_paths = ["file1_for_lb2_tsk2_heshes.txt", "file2_for_lb2_task2_heshes.txt"] # file_paths will be a tuple of transferred files
def generate_file_hashes(*file_paths):
    hashed_dict = {}
    for path in file_paths:
        try:
            with open(path, "rb") as file:
                reading_file = file.read()
                print(reading_file)
                hashed_file = hashlib.sha256(reading_file).hexdigest()
                print(hashed_file)
                hashed_dict[path] = hashed_file

        except FileNotFoundError:
            print("File is not found")
        except IOError:
            print("Error reading file")

    return hashed_dict
res = generate_file_hashes("file1_for_lb2_task2_heshes.txt", "file2_for_lb2_task2_heshes.txt")
print(res)

