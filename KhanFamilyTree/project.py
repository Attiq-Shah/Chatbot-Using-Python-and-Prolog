
from pyswip import Prolog

prolog = Prolog()
prolog.consult("KhanFamilyTree.pl")


Record = ["Chote Khan",   "ChotiRani", "BarreKhan", "BarriRani", "Salim", "Kausar", "Nadir", 
          "Asad", "Nahid", "Sumra", "Rizwan", "Burhan", "Rashid", "Akram", "Salima", "Sanam", "Rabia"]

def display_khanFamily():
    print("Please Select Any choice To Find Relationship:\n")
    print("Enter 1 for Baap ------------ Enter 2 for Maa")
    print("Enter 3 for Beti ------------ Enter 4 for Beta")
    print("Enter 5 for Dada ------------ Enter 6 for Nana")
    print("Enter 7 for Dadi ------------ Enter 8 for Nani")
    print("Enter 9 for Sala ------------ Enter 10 for Bahu")
    print("Enter 11 for Pota ----------- Enter 12 for Poti")
    print("Enter 13 for Nawasa --------- Enter 14 for Nawasi")
    print("Enter 15 for Sussar --------- Enter 16 for Saas")
    print("Enter 17 for Bapdada -------- Enter 18 for Khala")
    print("Enter 19 for Chachataya ----- Enter 0 for Exit: \n")

def khanFamilyMembers():
    print("Select Any Member of Khan Family: \n")
    print("ChoteKhan,   ChotiRani,  BarreKhan,  BarriRani")
    print("Salim,       Kausar,     Nadir,      Asad")
    print("Nahid,       Sumra,      Rizwan,     Burhan")
    print("Rashid,      Akram,      Salima,     Sanam,")
    print("Rabia")


while True:
    print("***  WELLCOME TO 2 in 1 Chatbot OF KHAN FAMILY  ***\n")
    choice = None
    found = False
    answer = []
    display_khanFamily()
    valid_choices = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"}
    choice = input("Enter your Choice: ")
    if choice in valid_choices:
        choice = choice
    else:
        print("Sorry Invalid Choice\n Try Again: \n")

    if (choice =='1'):
        khanFamilyMembers()
        Y = input("Enter name of person to find his/her Baap: ")
        Y = Y.capitalize()
        if Y in Record:
            for val in prolog.query("baap(X,"+Y+")"):
                answer.append(val["X"])
                found = True
                print("Mr.{0} is the baap of {1}.".format(val["X"], Y))
            if found == False:
                print("Sorry Relationship does't Exist in Our Record :)")
        else:
            print("I think You have Entered Wrong Name\nTry Again :)")
    
    if (choice == '2'):
        khanFamilyMembers()
        Y = input("Enter name of person to Find his/her Maa: ")
        Y = Y.capitalize()
        if Y in Record:
            for val in prolog.query("maa(X,"+Y+")"):
                answer.append(val["X"])
                found = True
                print("Mrs.{0} is the maa of {1}.".format(val["X"], Y))
            if found == False:
                print("Relationship does't Found.")
        else:
            print("I think You have Entered Wrong Name\nTry Again :)")

    if (choice == '3'):
        khanFamilyMembers()
        Y = input("Enter name of Person to find his/her Beti: ")
        Y = Y.capitalize()
        if Y in Record:
            for val in prolog.query("beti(X,"+Y+")"):
                answer.append(val["X"])
                found = True
                print("Mrs.{0} is the beti of {1}.".format(val["X"], Y))
            if found == False:
                print("Relationship does't Found.")
        else:
            print("I think You have Entered Wrong Name\nTry Again :)")

    if (choice == '4'):
        khanFamilyMembers()
        Y = input("Enter Name of person to Find his/her beta: ")
        Y = Y.capitalize()
        if Y in Record:
            for val in prolog.query("beta(X,"+Y+")"):
                answer.append(val["X"])
                found=True
                print("Mr.{0} is the beta of {1}.".format(val["X"], Y))
            if found == False:
                print("Relationship does't Found.")
        else:
            print("I think You have Entered Wrong Name\nTry Again :)")

    if (choice == '5'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Dada: ")
        Y=Y.capitalize()
        for val in prolog.query("dada(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the dada of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if(choice=='6'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Nana: ")
        Y=Y.capitalize()
        for val in prolog.query("nana(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the nana of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '7'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Dadi: ")
        Y=Y.capitalize()
        for val in prolog.query("dadi(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the dadi of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '8'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Nani: ")
        Y=Y.capitalize()
        for val in prolog.query("nani(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the nani of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '9'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Sala: ")
        Y=Y.capitalize()
        for val in prolog.query("sala(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the sala of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '10'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Bahu: ")
        Y=Y.capitalize()
        for val in prolog.query("bahu(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the bahu of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '11'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Pota: ")
        Y=Y.capitalize()
        for val in prolog.query("pota(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the pota of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '12'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Poti: ")
        Y=Y.capitalize()
        for val in prolog.query("poti(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the poti of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")
        

    if (choice == '13'):
        khanFamilyMembers()
        Y=input("Enter name of person  to find His/Her Nawasa: ")
        Y=Y.capitalize()
        for val in prolog.query("nawasa(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the nawasa of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")


    if (choice == '14'):
        khanFamilyMembers()
        Y=input("Enter name of person  to find His/Her Nawasi: ")
        Y=Y.capitalize()
        for val in prolog.query("nawasi(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the nawasi of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '15'):
        khanFamilyMembers()
        Y=input("Enter name of person to find Sussar: ")
        Y=Y.capitalize()
        for val in prolog.query("sussar(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the sussar of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '16'):
        khanFamilyMembers()
        Y=input("Enter name of person to find Saas: ")
        Y=Y.capitalize()
        for val in prolog.query("saas(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the sussar of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '17'):
        khanFamilyMembers()
        Y=input("Enter name of person  to find His/Her baapdada: ")
        Y=Y.capitalize()
        for val in prolog.query("baapdada(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the baapdada of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '18'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Khala:")
        Y=Y.capitalize()
        for val in prolog.query("khala(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mrs.{0} is the khala of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Found.")

    if (choice == '19'):
        khanFamilyMembers()
        Y=input("Enter name of person to find His/Her Chachataya: ")
        Y=Y.capitalize()
        for val in prolog.query("chachataya(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("Mr.{0} is the chachataya of {1}.".format(val["X"], Y))
        if found == False:
            print("Relationship does't Exist in our Record.")

    if (choice == '0'):
        print("Terminating Program... :)")
        break