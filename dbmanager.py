import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select  * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj  = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata',err)

    def getStudentClassById(self,classid):
        sql = "select  * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj  = self.cursor.fetchall()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata',err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s, %s, %s, %s, %s, %s)"
        
        # Tarih formatını kontrol et ve düzelt
        if isinstance(student.birthdate, str):
            student.birthdate = datetime.strptime(student.birthdate, "%Y-%m-%d").date()
        
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classId)
        
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata:', err)


        
    def editStudent(self,student: Student):
        from datetime import datetime
import mysql.connector

def editStudent(self, student):
    """
    Öğrenci bilgilerini günceller.
    """
    
    sql = """
        UPDATE student 
        SET studentnumber = %s, name = %s, surname = %s, birthdate = %s, gender = %s, classId = %s 
        WHERE id = %s
    """

    # 🔍 Doğum tarihi formatını kontrol et ve gerekirse dönüştür
    if isinstance(student.birthdate, str):
        try:
            student.birthdate = datetime.strptime(student.birthdate, "%Y-%m-%d").date()
        except ValueError:
            print(f"❌ Hata: Geçersiz doğum tarihi formatı -> {student.birthdate}")
            return  # Hatalı tarihi güncelleme işlemi yapmayalım

    # 🔍 Verilerin doğru sırada olduğundan emin olun
    value = (
        student.studentNumber, 
        student.name, 
        student.surname, 
        student.birthdate, 
        student.gender, 
        student.classId, 
        student.id
    )

    try:
        self.cursor.execute(sql, value)
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print(f"✅ {self.cursor.rowcount} öğrenci kaydı güncellendi.")
        else:
            print(f"⚠️ Güncellenecek öğrenci bulunamadı (id: {student.id}).")
    
    except mysql.connector.Error as err:
        print(f"❌ MySQL Hatası: {err}")


    
    def addTeacher(self,teacher: Teacher):
        pass
    
    def editTeacher(self,teacher: Teacher):
        pass
    

db = DbManager()

student = db.getStudentById(7)
student[0].name = "Berf"

#db.addStudent(student[0])
db.editStudent(student[0])

print(student[0].name)
print(student[0].surname)


# student = db.getStudentClassById(1)
# print(student[0].name)
