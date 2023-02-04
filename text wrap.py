
def wrap(string, max_width):
    string_2 = []
    for i in range(0, len(string), max_width):
        string_2.append(string[i:i + max_width])
    return '\n'.join(string_2)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)