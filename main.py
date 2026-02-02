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