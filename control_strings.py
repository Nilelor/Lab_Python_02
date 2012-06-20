x = 2
y = 5
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x
x=3
y=1
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

x=1
y=1
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

x=4
y=3
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

x=3
y=5
z = x+3
if z==1:
    y=0
elif z==2:
    y=10
elif z==4:
    y+=1
else:
    y=1
print "y is equal to",y

x=2
y=5
z = x+3
if z==1:
    y=0
elif z==2:
    y=10
elif z==4:
    y+=1
else:
    y=1
print "y is equal to",y

i=0
j=0
while i < 10:
    i+=1
    if i%2 == 0:
        print i   
    j+=1
print "We run through the loop body",j,"times"

i=0
while i > 10:
    i+=1
    if i%2 == 0:
        print i

pSchoolAge=6
Vote_age=18
presAge=40
retireAge=60
personAge=input("Enter an age:")
if personAge < pSchoolAge:
    print 'Too young'
elif personAge >= Vote_age:
    print 'Remember to vote'
elif personAge >= presAge:
    print 'Vote for me'
elif personAge < presAge:
    print "You can't be president"
elif personAge >= retireAge:
    print 'Too old'
print '---------'

rev=""
for i in range (0,40,3):
    if i<39:
        rev=","+ str(i)+str(rev)
    if i==39:
        rev=str(i)+str(rev)
print rev
print'---------'

for i in range (7,30,1):
    if (i%2 != 0 and i%3 != 0 and i%3 != 0):
        print i

print '------------'

n=0
count=0
while n>=0:
    if ((79.0*n)%97==1):
        print n
        count+=1
    n+=1
    if count==1:

        break

    
      
        
         
        
        
        
        


    
    
    
   

        




    


    
    
