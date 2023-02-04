def split_and_join(line):
    line_2 = ""
    for i in line:
        if i == " ":
            line_2 = line_2 + '-'
        else:
            line_2 = line_2 + i
    return line_2

line = input()
result = split_and_join(line)
print(result)