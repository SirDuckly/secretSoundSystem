import sys
def getArgs(args):
    return 2*args

def setPort():
    return result

if __name__ == "__main__":
    arguments = getArgs(sys.argv)
    args = arguments[1] + ' ' + arguments[2]
    print (args)
    print (arguments)
    print ('Starting  server....')
    port = arguments[1]

"""
functions:
Set port 
Start listening session 
On connection create session
On session creation ask if want to join/ create room

"""