import sys

def main(filename):
    """ Opens and read file to repl """
    try:
        file  = open(filename, mode='rt', encoding='utf-8')
        for line in file:
            sys.stdout.write(line)
    finally:
        file.close()

def mainWith(filename):
    """ same logic as upper but we don't need to bother with open() and close() """
    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            sys.stdout.write(line)

# run from console -> name alway __main__
if __name__ == '__main__':
    main(sys.argv[1])