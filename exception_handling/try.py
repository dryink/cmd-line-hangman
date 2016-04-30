def open_a_file():
    try:
        fh = open("testfile", "r")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print "Error: the file might not exist or problem reading data"
    else:
        print "Written content in the file successfully"
    finally:
        fh.close()
