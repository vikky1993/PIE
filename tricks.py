##Trick - 1
s = "practical programming"
s = s[::-1]
print "reverse string", s

##Trick - 2
val = [(1,2,3),(44,55,66)]
zip(*val)

##Trick-3
p = [11,22,33]
x,y,z = p

##Trick-4
a = 1111
b = 4444
a,b = b,a

##Trick-5
x = "practical"
y = "programming"
print x*4+' '+y*2

##Trick -6
n = 22
if n in [11,22,33,44]:
	print str(n)+' found!!!!'

##Trick -7
list1 = [11,22,33,44]
list2 = [99,88,77,66]
for x,y in zip(list1,list2):
	print x,y

##Trick -8
no = 11
no == 11
no > 11
no < 11
no <= 11
no >= 11

##Trick - 9
import calendar
cal = calendar.month(2017,3)
print cal

##Trick -10

a = ["please", "like"]
print " ".join(a)
