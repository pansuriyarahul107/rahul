import counsellor

def counseller():

        print('''
                1. Add student
                2. Remove student
                3. View all student
                4. view specific student
        ''')

        choice = int(input("Enter a choice by counseller :")) 
        if choice==1:
                counsellor.addStudent()


def faculty():
        print("faculty calling")

def student():
        print("student calling")