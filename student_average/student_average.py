if __name__ == '__main__':
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]

    if query_name in student_marks.keys():
        average: float = sum(marks) / len(marks)
    else:
        print("Invalid student name")

    print(f"{average:.2f}")