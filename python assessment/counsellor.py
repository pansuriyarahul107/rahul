
dict = {};
def addStudent():
    serial =int(input("Enter a Serial number : "))
    Firstname =  (input("Enter a First Name: "))
    LastName = (input("Enter a Last Name: "))
    Contect = (input("Enter a Contect Number:"))
    subject = (input("Enter a Subject :"))
    marks = int(input("Enter a Marks:"))

    abc = {"std":{"serial":serial,"fname":Firstname,"lname":LastName,"Contect":Contect,"subject":subject,"marks":marks}}
    dict.update(abc)

