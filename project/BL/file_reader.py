def read(file_path):
    content = ""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    print(read('..\\test_folder\call1.json'))
