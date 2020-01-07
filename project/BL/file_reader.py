def read(file_path):
    '''
    This function reads content from a file

    Args:
        file_path: path to a file to read.
    
    Returns:
        content of a file as a string.
    '''
    content = ""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    print(read('..\\test_folder\call1.json'))
