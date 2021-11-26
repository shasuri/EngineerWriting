import graphviz as gv

mealy = gv.Digraph(format='png', engine="neato")

mealy.node('State0', pos='0,0!')
mealy.node('State1', pos='3,0!')

mealy.edge('State0', 'State1', label='INPUT/OUTPUT')

file_name_mealy_0 = mealy.render(filename='mealy_0')
print(file_name_mealy_0)

mealy.clear()

# ---------------------------------------------------
mealy.attr(splines='curved')
# dummy node for curved edge direction
mealy.node('', pos='4.25,-0.5!', style="invis")

mealy.node('A', pos='0,0!')
mealy.node('B', pos='3,0!')
mealy.node('C', pos='6,0!')
mealy.node('D', pos='9,0!')


mealy.edge('A:e', 'A:w', label="0/0")
mealy.edge('A', 'B', label="1/0")

mealy.edge('B:e', 'B:w', label="1/0")
mealy.edge('B', 'C', label="0/0")

mealy.edge('C:s', 'A:s', label="0/0")
mealy.edge('C', 'D', label="1/0")

mealy.edge('D:s', 'B:s', label="1/1")
mealy.edge('D', 'C', label="0/0")

file_name_mealy_1 = mealy.render(filename='mealy_1')
print(file_name_mealy_1)

# --------------------------------------------------
mealy.node('E', pos='6,-3!')

mealy.edge('D', 'E', label="1/0")

mealy.edge('E:w', 'B:s', label="1/0")
mealy.edge('E:w', 'C:s', label="0/1")


file_name_mealy_2 = mealy.render(filename='mealy_2')
print(file_name_mealy_2)

# mealy.view()
