import sys
import os
import time

def main():
    assert len(sys.argv) == 3, 'Need exactly 2 arguments'

    operator = sys.argv[1]

    assert operator in ['create', 'destroy'], \
        'Operator is not one of create, destroy: bailing out'

    try:
        operand1 = str(sys.argv[2])

    except ValueError:
        print('cannot convert input to a number: bailing out')
        return

    newfile(operand1, operator)

def newfile(operand1, operator):
    print("Creating Folder"+" "+operand1)
    time.sleep(1)
    if operator == 'create':
        os.mkdir(operand1)
        os.chdir(operand1)
        print("creating index.html")
        time.sleep(1)
        f=open("index.html","w+")
        f.write("!docktype html")
        f.close() 
        time.sleep(1)
        print("All Done!")
if __name__ == "__main__":
    main()

