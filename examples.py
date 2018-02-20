s='my global variable'
print globals()

print globals().keys()

print globals()['s']

def fun():
    print locals()

fun()   
s='hello how are you Mary,are you feeling okay? '

print "rounding 5.23222 to 2 decimals ",round(5.23222,2)
print "binary of 1024 is ",bin(1024)
print "are all letters in string lower ",s.islower()

s='twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print "no.of time 'w' in string  ",s.count('w')

s1={2,3,1,5,6,8}
s2={3,1,7,5,6,8}

print "elements in set 1 only ",s1.difference(s2)
print "common elements ",s1.intersection(s2)
d={x: x**3 for x in xrange(0,5,1) }

l=[1,2,3,4]
print "list elements ",l
l.reverse()
print "reverse the list ",l 
l.sort()
print "sort the list ",l 
