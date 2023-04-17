from tkinter import *

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

    
root = Tk()
root.title('Khan Family Tree')
root.geometry('400x300')
root.config(bg='#0f4b6e')

name_tf = Entry(root)

name_lbl = Label(
    root,
    text='Enter Your Choice',
    bg='#0f4b6e',
    fg='white'
)


name_lbl.pack()
name_tf.pack()

btn = Button(
    root,
    text='Enter',
    relief=SOLID,
    command=khanFamilyMembers()
)
btn.pack(pady=10)

disp_tf = Entry(
    root,
    width=38,
    font=('Arial', 14)
    )

disp_tf.pack(pady=5)


root.mainloop()