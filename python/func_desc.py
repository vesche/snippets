import platform

for m in dir(platform):
    
    mtc = getattr(platform, m)
    
    if type(mtc) == "function":
        result = mtc()
    else:
        result = mtc
    
    print '-'*10
    
    print "platform.{}".format(m)
    print mtc.__doc__
    print "{}".format(result)
