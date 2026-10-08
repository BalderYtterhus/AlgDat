"""
    1. lag tre med segmenter, count = 1 for hvert segment
    2. start på indeks 0 i dna streng, søk ned i treet, med total = 0
    3. dersom det finnes som barn gå videre, hvis count er noe annet enn 0, så tar du total += count
    4. dersom ikke i children: continue
    5. returner total etter hele dna strengen er iterert gjennom
"""
def string_match(dna, segments):
    root = build_tree(segments) # 1.
    total = 0

    for i in range(len(dna)):
        current_node = root
        j = i

        while (j < len(dna)) and dna[j] in current_node.children:
            current_node = current_node.children[dna[j]]
            total += current_node.count

            j += 1

    return total


def search_tree(root, dna:str):
    current_node = root

    for char in dna:
        if char not in current_node.children:
            return 0
        
        current_node = current_node.children[char]

    return current_node.count


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