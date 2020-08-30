#[문제]
#반을 만들고
# - 반에 학생을 추가할 수 있는 함수
# - 반에 학생의 리스트를 반환하는 함수
# - 특정 아이디를 가지고 그 아이디의 학생을 반환하는 함수

class Class :
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def return_students(self):
        return self.students

    def return_student_only(self, id):
        for student in self.students :
            if student['id'] == id :
                return student['name']

        return None

result = Class()
result.add_student({
    'id' : 1,
    'name' : '김기영'
})

result.add_student({
    'id' : 2,
    'name' : '양민열'
})

print(result.return_students())
print(result.return_student_only(1))
print(result.return_student_only(2))
