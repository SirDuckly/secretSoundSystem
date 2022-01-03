import sys
def func(args):
    return 2*args

if __name__ == "__main__":
    arguments = func(sys.argv)
    args = arguments[1] + ' ' + arguments[2]
    print (args)
    print ('Starting  server....')
    port = arguments[1]
