## this program creates a graph of possibilities of given inputs

import graphviz  # doctest: +NO_EXE
from functools import reduce

#rankdir LR is left to right i.e. draws vertically
#rankdir TB draws horizontally
dot = graphviz.Digraph(comment='Options',graph_attr={'rankdir':'LR'})

# inputs = {
#     "A":['a1','a2','a3'],
#     "B":['b1','b2','b3'],
#     "C":['c1','c2','c3'],
#     "d":["d1","d2"],
#     "e":["e1",'e2','e3','e4']
# }

inputs = {
    "os": ["u18 patched","u20"],
    "nginx": ["1.13","1.19","1.21"],
    "nodejs": ["8.9.4","lts"]
}

total_columns = len(inputs)
total_rows = 1
ordered_keys = list(inputs.keys())
ordered_sizes = list(map(lambda key: len(inputs[key]), ordered_keys))
total_rows = reduce(lambda x,y: x*y,ordered_sizes)

def attach_children(parent_name, current_index):
    if current_index+1 == len(ordered_keys):
        return
    #ignore current and previous level nodes
    index = current_index+1
    input_category = ordered_keys[index]
    for selected_input in inputs[ordered_keys[index]]:
        node_name='{}-{}-{}'.format(parent_name,input_category,selected_input) 
        dot.node(node_name)
        dot.edge(parent_name, node_name)
        print(node_name)
        attach_children(node_name, index)

attach_children('root',-1)
            
# dot.node('A', 'King Arthur')  # doctest: +NO_EXE
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')
#dot.mark_exe()

dot.render('doctest-output/round-table.gv',outfile='doctest-output/round-table.svg').replace('\\', '/')
