def clear():
    import os
    #clear screen
    test_os = os.name
    if test_os == "nt":
        os.system('cls')
    elif test_os == "posix":
        os.system('clear')
    else:
        pass
