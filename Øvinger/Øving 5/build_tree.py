def build_tree(dna_sequences):
    root = Node()
    current_node = root

    for seq in dna_sequences:
        current_node = root

        for c in seq:

            if c not in current_node.children:
                node_c = Node()
                current_node.children[c] = node_c

            current_node = current_node.children[c]
        
        current_node.count = current_node.count + 1

    return root



    