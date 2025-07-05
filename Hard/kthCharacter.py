# Alice and Bob are playing a game. Initially, Alice has a string word = "a".

# You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

# Now Bob will ask Alice to perform all operations in sequence:

# If operations[i] == 0, append a copy of word to itself.
# If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "aczn".
# Return the value of the kth character in word after performing all the operations.

# Note that the character 'z' can be changed to 'a' in the second type of operation.

def kthCharacter(k, operations):
    word = 'a'

    for opp in operations:
        if opp == 0:
            word += word
        elif opp == 1:
            word += ''.join(chr(x+1) if x != 122 else 'a' for x in [ord(y) for y in word])
        
    return word[k-1]
    
print(kthCharacter(10,[0,1,0,1]))