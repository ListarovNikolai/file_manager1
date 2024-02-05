def write_file(filename, mode):
    file = open(filename, mode)
    file.write("Hello, World!")
    file.close()

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    print(f"содержимое файла {filename}: {content}")
    file.close()




if __name__ == "__main__":
    file_name = "file_name.txt"
    # write_file(file_name, "w")
    # read_file(file_name)
    # write_file(file_name, "a")
    # read_file(file_name)
    # write_file(file_name, "a")
    # read_file(file_name)

    with open(file_name,"w") as file: 
        file.write('Hello, World!')

    with open(file_name,"r") as file: 
        content = file.read()
        print(f"содержимое файла {file_name}: {content}")