tmpcount = 0
def getTmp():
    global tmpcount
    ret = '__tmp' + str(tmpcount)
    tmpcount += 1
    return ret
