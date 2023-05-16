def menu():
    #import libraries
    import time
    import os
    try:
        from content.additional_functions.clear import clear
    except:
        print("---------------------------------------")
        print("Import Error.")
        print("---------------------------------------")

    #clear screen
    clear()

    #get the current location of /mitm folder
    file_path = os.path.dirname(os.path.abspath("start.py"))

    #construct terminal commands
    command1 = "python3 "+file_path+"/spider/crawler.py --file "+file_path+"/spider/url/sites.txt --output "+file_path+"/spider/link/links.txt"
    command2 = "python3 "+file_path+"/content/requester.py --list "+file_path+"/spider/link/links.txt"

    #menu
    print("---------------------------------------")
    print("Select Program")
    print("---------------------------------------")
    print("Press 1 For Crawler")
    print("Press 2 For Requester")
    print("---------------------------------------")

    #get input
    try:
        program_type = str(input("Input: "))
    except:
        print("---------------------------------------")
        print("Unexpected Error.")
        print("---------------------------------------")
        time.sleep(2)
        menu()

    #clear screen
    clear()

    #route
    if program_type == "1":
        #route to crawler
        os.system(command1)
    elif program_type == "2":
        #route to requester
        os.system(command2)
    else:
        print("---------------------------------------")
        print("Wrong Input.")
        print("---------------------------------------")
        time.sleep(2)
        menu()