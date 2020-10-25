import sys

# Read from file and return the largest word
def get_largest_word(filepath):
    try:
        open_file = open(filepath, 'r')
        reader = open_file.readlines()
        open_file.close()
    except:
        raise FileNotFoundError(f'No file exists with {filepath}')

    largest_word = None
    if len(reader) > 0:
        largest_word = sorted(reader, key=len)[-1].rstrip()                
    
    return largest_word

# Transpose a given word as parameter
def transpose_word(word):
    try:
        result = ''.join(reversed(word))
        return result
    except: 
        raise Exception('Only str type is allowed')

# Execute the functionality to transpose largest word
def execute():
    try:
        files = sys.argv[1]

        largest_word = get_largest_word(files)
        print(largest_word)
        transposed_word = transpose_word(largest_word)
        print(transposed_word)
    except:
        raise IndexError('Expected 1 argument got 0')

if __name__ == "__main__":
    execute()

