s = "Jayesh"

#name[0] = "R"

# a = len(s) #len is python function 
# print(a)
# #print(s.upper(), s)
# print(s.lower(), s)
# print(s.capitalize(), s) #first character of the string gets converted into capital
# print(s.title(), s)

# text = " hello world"
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text = "Python is fun and fun fun"
# print(text.find("is")) #output: 7
# print(text.replace("fun", "awesome"))

# text = "Apples,Banana,Pineapple"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples'])) #join is the function of python

text = "Python123"
print(text.isalpha()) #all alphabetic or not so this is False
print(text.isdigit()) #all digit or not but if string is converted into digit then its digit and true but here it is false.
print(text.isalnum()) #alphanumberic string only so its true
print(text.isspace()) #whiteSpace characters → " " ,Tab → "\t" ,New line → "\n" if those are there then it is true but here it is false.