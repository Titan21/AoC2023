

def loader(filepath):
    with open(filepath, 'r') as file:
        return file.read().splitlines()
