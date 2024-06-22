

import operation

print('''  Student Management System
      
      Press 1 for counseller
      press 2 for Faculty
      press 3 for Student


''')

Role = int(input("Enter a role id :"))

if Role==1:

    operation.counseller()

elif Role==2:
    operation.faculty()
elif Role ==3:
    operation.student()
else:
    print("Invalid choice !!!")