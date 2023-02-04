def count_substring(string, sub_srting):
    count = 0

    for i in range(0, len(string)-len(sub_srting)+1):
        if string[i: len(sub_srting)+i] == sub_string:
            count = count+1
    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)