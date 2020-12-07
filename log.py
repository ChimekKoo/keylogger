def log(data, read_or_append):
    if read_or_append == "a":
        logfileobj = open("data/.log", "a")
        logfileobj.write(data)
        logfileobj.close()
    elif read_or_append == "r":
        logfileobj = open("data/.log", "r")
        data = logfileobj.read()
        logfileobj.close()
        return data