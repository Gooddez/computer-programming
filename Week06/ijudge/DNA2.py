"""DNA"""
def main(dna1, dna2):
    """DNA"""
    output = ''
    character = {'A', 'C', 'T', 'G'}
    if set(dna1 + dna2).issubset(character):
        for i in range(len(dna1)):
            for j in range(i+1,len(dna1)+1):
                current = dna1[i:j]
                if current in dna2:
                    if len(current) > len(output):
                        output = current
                else:
                    break
    else:
        output = 'Error'
    return output if output else None
print(main(input(), input()))
