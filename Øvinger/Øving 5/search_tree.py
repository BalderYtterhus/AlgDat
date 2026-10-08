def search_tree(root, dna:str):
    current_node = root

    for char in dna:
        if char not in current_node.children:
            return 0
        
        current_node = current_node.children[char]

    return current_node.count
