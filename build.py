#Description: this is a script to help me start  new web development environment

#imports
import os
from termcolor import colored
import time
import sys


def mainmenu():
    os.system('cls')
    print(colored('##########################################','green'))
    print(colored('#                WELCOME                 #','green'))
    print(colored('#        WEBSITE FILE BUILDER  V1.0      #','green'))
    print(colored('##########################################','green'))
    print(colored('#                [1] HTML                #','green'))
    print(colored('#                [2] PHP                 #','green'))
    print(colored('#                [3] EXIT                #','green'))
    print(colored('##########################################','green'))
    userinput = input(colored('What Are You Coding Today: ','green'))
    if userinput == "1":
        build_html()
    elif userinput == "2":
        build_php()
    elif userinput == "3":
        exit()
    else:
        print(colored("Wrong Input","green"))
        time.sleep(1)
        mainmenu()
    
def build_html():
    os.system('cls')
    userinput = input(colored("Name Of The Folder: ","green"))
    print(colored("Making Project Folder "+userinput+"....","green"))
    os.mkdir(userinput)
    time.sleep(1)
    currentpath = os.getcwd()
    os.chdir(currentpath + '\\' + userinput)
    print(colored("Making Subfolder: css....","green"))
    os.mkdir('css')
    time.sleep(1)
    print(colored("Making Subfolder: js....","green"))
    os.mkdir('js')
    time.sleep(1)
    print(colored("Making Subfolder: images....","green"))
    os.mkdir('images')
    time.sleep(1)
    print(colored("Making File: index.html....","green"))
    f = open("index.html","w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang='en'>\n")
    f.write("<head>\n")
    f.write("   <meta charset='UTF-8'>\n")
    f.write("   <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    f.write("   <title>Document</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()
    time.sleep(1)
    print(colored("Making File: style.css....","green"))
    f = open("css\style.css","w+")
    time.sleep(1)
    print(colored("Making File: script.js....","green"))
    f = open("js\script.js","w+")
    time.sleep(1)    
    print(colored("All Done Good To go!","green"))
    time.sleep(1)
    print(colored("Starting index.html in Vs code....","green"))
    os.system("code index.html")

def build_php():
    os.system('cls')
    userinput = input(colored("Name Of The Folder: ","green"))
    print(colored("Making Project Folder "+userinput+"....","green"))
    os.mkdir(userinput)
    time.sleep(1)
    currentpath = os.getcwd()
    os.chdir(currentpath + '\\' + userinput)
    print(colored("Making Subfolder: css....","green"))
    os.mkdir('css')
    time.sleep(1)
    print(colored("Making Subfolder: js....","green"))
    os.mkdir('js')
    time.sleep(1)
    print(colored("Making Subfolder: images....","green"))
    os.mkdir('images')
    time.sleep(1)
    print(colored("Making File: index.php....","green"))
    f = open("index.php","w+")
    f.write("<?php\n")
    f.write("?>\n")
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang='en'>\n")
    f.write("<head>\n")
    f.write("   <meta charset='UTF-8'>\n")
    f.write("   <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    f.write("   <title>Document</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()
    time.sleep(1)
    print(colored("Making File: style.css....","green"))
    f = open("css\style.css","w+")
    f.close()
    time.sleep(1)
    print(colored("Making File: script.js....","green"))
    f = open("js\script.js","w+")
    f.close()
    time.sleep(1)    
    print(colored("All Done Good To go!","green"))
    time.sleep(1)
    print(colored("Starting index.html in Vs code....","green"))
    os.system("code index.php")
    sys.exit()
if __name__ == '__main__':
    mainmenu()
    