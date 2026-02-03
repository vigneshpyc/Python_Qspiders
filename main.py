#02.02.2026 Type casting/conversion
a = 25 # int
print(a)
print(type(a))
float(a) # convert the a into float datatype
print(a)
complex(0,a) # convert the a into complex datatype which consiste of real and imaginary part
complex(a,a) # 25+25j
bool(a) # convert the a into bool datatype
str(a) #convert the a into string datatype

#convert complex into other
c = 2.5+0j
f = 2.5
print(type(c))
e = True
print(bool('string'))
print(type(str(e)))

l = [10,20]
print(set(l))
print(tuple(l))
#print(dict(l))
s = "vicky"
print(list(s))
di = {0:'a',1:'b'}
print(list(di))


#convert tuple into other datatypes
t = ('py', ['python', 'django'], ('db','sql'), {25, 10})
print("tupple into list -> ",list(t))
print("tuple into dictionary -> ",dict(t))
print("tuple into boolean -> ",bool(t))
print("tuple into string -> ",str(t))
# print("tuple into set -> ", set(t)) -> error can not convert into tuple into set