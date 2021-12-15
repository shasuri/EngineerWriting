from graphviz import Source

sourceFile = open("./2020.dot","r")
temp = sourceFile.read()
print(temp)
s = Source(temp, filename="2020", format="pdf")
s.view()
