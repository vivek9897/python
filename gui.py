# import tkinter as vk
# import sqlite3
#
# root = vk.Tk()
# root.title("management database")
# connection = sqlite3.connect('management.db')
#
# TABLE_NAME = "student_table"
# STUDENT_ID = "student_id"
# STUDENT_NAME = "student_name"
# STUDENT_COLLEGE = "student_college"
# STUDENT_ADDRESS = "student_address"
# STUDENT_PHONE = "student_phone"
#
# connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
#                     " INTEGER PRIMARY KEY AUTOINCREMENT, " +
#                     STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
#                     STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER );")
#
# operational = vk.Label(root, text = "enter the following details")
# operational.pack()
#
# student_name = vk.Label(root, text = "student name")
# student_name.pack()
# student_name_entry = vk.Entry(root)
# student_name_entry.pack()
#
# college_name = vk.Label(root, text = "college name")
# college_name.pack()
# college_name_entry = vk.Entry(root)
# college_name_entry.pack()
#
# address = vk.Label(root, text = "address")
# address.pack()
# address_entry = vk.Entry(root)
# address_entry.pack()
# phone = vk.Label(root, text = "phone no")
# phone.pack()
# phone_entry = vk.Entry(root)
# phone_entry.pack()
# def takevalueinput():
#     name = student_name_entry.get()
#     college = college_name_entry.get()
#     phone = phone_entry.get()
#     address = address_entry.get()
#     connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
#                                              STUDENT_NAME + ", " +
#                                              STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
#                                              ", " + STUDENT_PHONE +
#                                              " ) VALUES ( '"+name+"', '"+college+"', " +
#                                               "'"+address+"', "+phone+" ); ")
#     connection.commit()
#     print("values saved succesfully")
# button = vk.Button(root,text = "save entries",command = lambda : takevalueinput())
# button.pack()
# def fetchDetais():
#     cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
#     for row in cursor:
#         print("student id is:",row[0])
#         print("student name is:",row[1])
#         print("student college is:",row[2])
#         print("student address is:",row[3])
#         print("student phone is:",row[4])
#
# display = vk.Button(root,text= 'display all records' ,command = lambda: fetchDetais())
# display.pack()
# root.mainloop()

