def getNode(node_name, nodes):
    for node in nodes:
        if node[0] == node_name:
            return node
    print "NOT FOUND", node_name
    return None

def setTotalWeight(node_name, nodes):
    node = getNode(node_name, nodes)
    if node[3] > 0:
        return
    for child_name in node[2]:
        setTotalWeight(child_name, nodes)
    totalWeight = node[1] + sum([getNode(child_name, nodes)[3] for child_name in node[2]])
    nodes.remove(node)
    nodes.append((node[0], node[1], node[2], totalWeight))


lines = open("7").readlines()
nodes = []
all_children = []
for line in lines:
    words = line.split()
    name = words[0]
    weight = int(words[1][1:-1])
    children = []
    for child in words[3:]:
        child_name = child.replace(',', '')
        children.append(child_name)
        all_children.append(child_name)
    nodes.append((name, weight, children, -1))

print len(nodes)

for node in nodes:
    if node[0] not in all_children:
        setTotalWeight(node[0], nodes)
        print node


print len(nodes)

for node in nodes:
    balanced = True
    if len(node[2]) > 0:
        child_weight = getNode(node[2][0], nodes)[3]
        for child_name in node[2][1:]:
            if getNode(child_name, nodes)[3] != child_weight:
                balanced = False
    if not balanced:
        print "UNBALANCED", node
        for child_name in node[2]:
            print getNode(child_name, nodes)
        print