import pyodbc

from models.Student import Student
import pandas as pd
import numpy as np
server = 'DESKTOP-9DCUPJF\SQLEXPRESS'
db = 'Flask_TUT'
tcon = True
uname = 'sa'
pword = '12345'
connection = pyodbc.connect(driver='{SQL Server}',
                            host=server, database=db, trusted_connection=tcon,
                            user=uname, password=pword)


def insert_student(student):
    cursor = connection.cursor()
    query = f"exec insert_student N'{student.name}' , '{student.dateOfBirth}' , N'{student.address}'"
    cursor.execute(query)
    cursor.commit()
    cursor.close()


def get_all_student():
    cursor = connection.cursor()
    query = "exec get_all_student"
    cursor.execute(query)
    list_student = []
    for i in cursor:
        student = Student(name=i[1], dateOfBirth=i[2], address=i[3])
        student.id = i[0]
        list_student.append(student)
    cursor.close()
    return list_student


def read_student_from_excel(file_path):
    # đọc dữ liệu từ file
    data = pd.read_excel(file_path)
    data = np.array(data)
    list_student = []
    for i in data:
        student = Student(name=i[1], dateOfBirth=i[2], address=i[3])
        student.id = i[0]
        list_student.append(student)
    return list_student



def update(student):
    cursor = connection.cursor()
    query = f"exec update_student {student.id},N'{student.name}' , '{student.dateOfBirth}' , N'{student.address}'"
    print(query)
    cursor.execute(query)
    cursor.commit()
    cursor.close()


def get_student_by_id(id_hs):
    cursor = connection.cursor()
    query = f"exec get_student_by_id {id_hs}"
    cursor.execute(query)
    list_student = []
    for i in cursor:
        student = Student(name=i[1], dateOfBirth=i[2], address=i[3])
        student.id = i[0]
        list_student.append(student)
    cursor.close()
    return list_student[0]


def delete(id_hs):
    cursor = connection.cursor()
    query = f"exec delete_student {id_hs}"
    cursor.execute(query)
    cursor.commit()
    cursor.close()

def load_pdf(file):
    data = pd.read_excel('dshocsinh.xlsx')
    data = np.array(data)
