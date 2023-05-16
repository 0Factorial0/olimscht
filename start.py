def start():
    #import libraries
    import time
    import os
    try:
        from content.additional_functions.clear import clear
        from content.additional_functions.kill import kill

        from content.menu import menu
    except:
        print("---------------------------------------")
        print("Import Error.")
        print("---------------------------------------")

    #clear screen
    clear()

    #main menu / routing
    print("---------------------------------------")
    print("Select Program Type")
    print("---------------------------------------")
    print("Press 1 For Terminal")
    print("Press 2 For Java GUI")
    print("Press 3 Install Dependencies")
    print("Press 4 Kill Python")
    print("---------------------------------------")

    #get input
    try:
        program_type = str(input("Input: "))
    except:
        print("---------------------------------------")
        print("Unexpected Error.")
        print("---------------------------------------")
        time.sleep(2)
        start()

    #route
    if program_type == "1":
        #route terminal
        menu()
    elif program_type == "2":
        install_()
        os.system("java content/execute.java")
    elif program_type == "3":
        print("---------------------------------------")
        #install dependencies and restart program
        install_()
        start()
    elif program_type == "4":
        #kill all python
        kill()
    else:
        print("---------------------------------------")
        print("Wrong Input.")
        print("---------------------------------------")
        time.sleep(2)
        start()

#install requirements
def install_():
    try:
        from content.additional_functions.install import install
    except:
        print("---------------------------------------")
        print("Import Error.")
        print("---------------------------------------")
    install()

def main():
    #import libraries
    import argparse
    import os
    try:
        from content.additional_functions.clear import clear
        from content.additional_functions.crazy import crazy
        from content.additional_functions.kill import kill
    except:
        print("---------------------------------------")
        print("Import Error.")
        print("---------------------------------------")

    #get the current location of /mitm folder
    file_path = os.path.dirname(os.path.abspath("start.py"))

    #construct terminal commands
    command1 = "python3 "+file_path+"/spider/crawler.py --file "+file_path+"/spider/url/sites.txt --output "+file_path+"/spider/link/links.txt"
    command2 = "python3 "+file_path+"/content/requester.py --list "+file_path+"/spider/link/links.txt"
   
    #create argument structure as 'python3 <start>.py --go <anything>'
    print("---------------------------------------")
    parser = argparse.ArgumentParser(description='Start Program With Arguments.')
    parser.add_argument('--go', type=str, nargs='?', const=1, help='Routing Quick. Valid Values: <now, crawl, request, crazy>')
    parser.add_argument('--gui', type=str, nargs='?', default='', const=1, help='Open GUI. Valid Values: <java>')
    parser.add_argument('--k', type=str, nargs='?', default='', const=1, help='For Killing Python. Valid Values: <p>')
    args = parser.parse_args()

    #clear screen
    clear()

    #check the argument value and route
    if args.go == "now" or args.gui == "java":
        #install dependencies and push as soon as possible
        install_()
        os.system("java content/execute.java")
    elif args.go == "crawl":
        #route to crawler
        os.system(command1)
    elif args.go == "request":
        #route to requester
        os.system(command2)
    elif args.go == "crazy":
        #open both in terminal
        crazy()
    elif args.k == "p":
        #kill the python
        kill()
    else:
        print("menu")
        start()
        
#route main function
if __name__ == "__main__":
    main()
