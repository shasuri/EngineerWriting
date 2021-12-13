from graphviz import Source

sourceFile = open("./graph.dot","r")
temp = sourceFile.read()
print(temp)
s = Source(temp, filename="test", format="pdf")
s.view()