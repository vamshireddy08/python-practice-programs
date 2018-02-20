try:
    for i in ['a','b','c']:
        print i**2
except:
    print "An error occured!"



x=5
y=0
try:
    z=x/y 
except:
    print   "ZeroDivisionError: denominator is zero "
finally:
    print "All Done "

def ask():
    while True:
        try:
            x=int(raw_input("enter an integer"))
         
        except:
            print 'An error occured! Please try again!'
            continue 
        else:
            print "Thank you, you number squared is: ", x*x
            break

ask(  )        
