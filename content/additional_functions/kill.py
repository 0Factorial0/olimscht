def kill():
    import os
    #kill python
    test_os = os.name
    if test_os == "nt":
        os.system('taskkill /IM python.exe /F /T /FI "MEMUSAGE gt 0" /FI "WINDOWTITLE eq crawler.py"')
        os.system('taskkill /IM python.exe /F /T /FI "MEMUSAGE gt 0" /FI "WINDOWTITLE eq requester.py"')
        pass
    elif test_os == "posix":
        os.system('pkill -9 -f ../../spider/crawler.py')
        os.system('pkill -9 -f ../requester.py')
        os.system('pkill -9 -f spider/crawler.py')
        os.system('pkill -9 -f content/requester.py')
    else:
        pass