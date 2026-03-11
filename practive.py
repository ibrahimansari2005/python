marks = []
for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)
average = sum(marks) / len(marks)
print("Average mark:", average)
arranged_marks = sorted(marks)
print(arranged_marks)
