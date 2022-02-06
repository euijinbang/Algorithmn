"""
정렬
selection sort
"""
import sys
sys.stdin = open("BOJ_10825_input.txt")

n = int(input())
students = []

# 각 학생의 정보를 딕셔너리로 저장, 리스트에 담는다. (튜플로도 가능)
for i in range(n):
    student = {}
    info = input().split()
    student['name'] = info[0]
    student['sub1'] = int(info[1])
    student['sub2'] = int(info[2])
    student['sub3'] = int(info[3])

    students.append(student)


sorted_s = sorted(students, key=lambda s: (-s['sub1'], s['sub2'], -s['sub3'], s['name']))
for student in sorted_s:
    print(student['name'])


# 다음 순서로 정렬한다.
# 1. sub1 감소하는 순서로
# 2. sub1 이 같으면 sub2 가 증가하는 순서로
# 3. sub1, sub2가 같으면 sub3가 감소하는 순으로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순으로


def selectionSortBySub1Desc(students, n):

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[min_idx]['sub1'] < students[j]['sub1']:
                min_idx = j

        students[min_idx], students[i] = students[i], students[min_idx]

    # print(students)


selectionSortBySub1Desc(students, n)


def selectionSortBySub2Asc(students, n):

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (students[min_idx]['sub1'] == students[j]['sub1']) and (students[min_idx]['sub2'] > students[j]['sub2']):
                min_idx = j

        students[min_idx], students[i] = students[i], students[min_idx]

    # print(students)


selectionSortBySub2Asc(students, n)


def selectionSortBySub3Desc(students, n):

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (students[min_idx]['sub1'] == students[j]['sub1']) and (students[min_idx]['sub2'] == students[j]['sub2']) \
                    and (students[min_idx]['sub3'] < students[j]['sub3']):
                min_idx = j

        students[min_idx], students[i] = students[i], students[min_idx]

    # print(students)


selectionSortBySub3Desc(students, n)


def selectionSortByNameAsc(students, n):

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (students[min_idx]['sub1'] == students[j]['sub1']) and (students[min_idx]['sub2'] == students[j]['sub2']) \
                    and (students[min_idx]['sub3'] == students[j]['sub3']) and (students[min_idx]['name'] > students[j]['name']):
                min_idx = j

        students[min_idx], students[i] = students[i], students[min_idx]

    # print(students)


selectionSortByNameAsc(students, n)


# for student in students:
#     print(student['name'])



