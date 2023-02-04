def mutate_string(string, position, character):
    list_input = list(string)
    list_input[position] = character
    string = ''.join(list_input)
    return string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)