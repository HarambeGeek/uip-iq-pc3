maxCalled = 0
minCalled = 0

def max_val(a,b):
    global maxCalled
    maxCalled = maxCalled + 1
  
    if(a > b):
        return a   
    elif(b > a):
        return b
    else:
        return a

def min_val(a,b):
    global minCalled 
    minCalled = minCalled + 1
  
    if(a < b):
        return a
    elif(b < a):
        return b
    else:
        return a 

def print_usage(init_msg, max_val=True, min_val=True):
    global maxCalled, minCalled
    print init_msg
    if max_val:
        print('functin max_val was called', maxCalled, ' times')
    if min_val:
        print('function min_val was called', minCalled, ' times')

if __name__ == '__main__':
    print('Calling function max_val')
    max_val(1,4)
    max_val(2,b=1)
    max_val(b=4,a=3)

    print('Calling function min_val')
    min_val(1,4)
    min_val(2,4)
    min_val(4,b=9)

    print_usage('The usage of functions min_val and max_val')
