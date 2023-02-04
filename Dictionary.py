def Average(lst):
    return sum(lst) / len(lst)
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average = Average(student_marks[query_name])
print("%.2f" % average)
