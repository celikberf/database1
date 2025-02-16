
class Student:
    def __init__(self,studentNumber,name,surname,birthdate,gender,studentId,classId):
        self.id = studentId if studentId is not None else 0
        self.studentNumber = studentNumber
    
        self.studentNumber = studentNumber
        if len(name) > 45:
            raise Exception("name için max 45 karakter girmelisiniz")
        self.name= name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classId =  classId

    @staticmethod
    def CreateStudent(obj):
        student_list = []

        if isinstance(obj,tuple):
            student_list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                student_list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return student_list