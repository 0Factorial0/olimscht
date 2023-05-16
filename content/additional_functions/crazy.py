def crazy():
    import os

    #get the current location of /mitm folder
    file_path = os.path.dirname(os.path.abspath("start.py"))

    #construct terminal commands
    command1 = "python3 "+file_path+"/spider/crawler.py --file "+file_path+"/spider/url/sites.txt --output "+file_path+"/spider/link/links.txt"
    command2 = "python3 "+file_path+"/content/requester.py --list "+file_path+"/spider/link/links.txt"
   
    #open both terminals
    test_os = os.name
    if test_os == "nt":
        os.system("start cmd /K "+command1)
        os.system("start cmd /K "+command2)
    elif test_os == "posix":
        import subprocess
        subprocess.call(['xterm','-e',command1])
        subprocess.call(['xterm','-e',command2])
    else:
        pass
