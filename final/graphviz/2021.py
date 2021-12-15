from graphviz import Source

temp = """
digraph g {
 node [shape = Mrecord,height=.1];
 node1[label = "zipper5", shape = none];
 node2[label = "<f0> Zipper |{ left |<f1> ∙ }|{ focus |<f2> ∙ }|{right | ∅} | {top | ∙∙∙ } "];
 node3[label = "<f0> List | <f1> ∙ |<f2> ∙ |<f3> ∙ "];
 node4[label = "<f0> \<worm\>"];
 node5[label = "<f0> \<fruit\>"];
 node6[label = "<f0> \<leaf\> |{ value |<f1> ∙ }"];
 node7[label = "<f0> \<leaf\> |{ value |<f1> ∙ }"];
 node8[label = "3"];
 node9[label = "2"];
 
 "node1" -> "node2":f0:n;
 "node2":f1:s -> "node3":f0:n;
 "node2":f2:s -> "node4":f0:n;
 "node3":f1:s -> "node5":f0:n;
 "node3":f2:s -> "node6":f0:n;
 "node3":f3:s -> "node7":f0:n;
 "node6":f1:s -> "node8";
 "node7":f1:s -> "node9";
 }
 """
# sourceFile = open("./2021.dot","r")
# temp = sourceFile.read()
s = Source(temp, filename="final", format="pdf")
s.view()