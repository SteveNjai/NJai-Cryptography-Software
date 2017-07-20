from tkinter import *
from cryptography.fernet import Fernet
import tkinter.messagebox

#configure main window
root=Tk()
root.title("Njai Cryptography Software")
root.configure(bg="#A9A9A9")

#configure top frame

frame1=Frame(root, height=200,  bg="#A9A9A9", bd=10, relief=SUNKEN)
frame1.pack(side=TOP, fill=X)

#create right frame label title: CRYPTOTEXT
labelB=Label(root, text="Cryptotext", bg="#A9A9A9", width=30)
labelB.pack(anchor=E)
labelB.configure(font=("agency-fb", '15', "bold", "underline"))

#create left frame label title: PLAINTEXT
labelA=Label(root, text="Plaintext", bg="#A9A9A9", width=30)
labelA.pack(anchor=W)
labelA.configure(font=("agency-fb", '15', "bold", "underline"))

#configure left frame for plaintext

frame2=Frame(root, height=400, width=500, bg="#DCDCDC", bd=10, relief=RAISED)
frame2.pack(side=LEFT)

#configure right frame for cryptotext

frame3=Frame(root, height=400, width=500, bg="#DCDCDC", bd=10, relief=RAISED)
frame3.pack(side=RIGHT)

#configure middle frame used for the buttons.

frame4=Frame(root, height=450, width=350, bg="#696969", bd=10, relief=RAISED)
frame4.pack(side=TOP)

#create title label

label1_1=Label(frame1, text="NJAI CRYPTOGRAPHY SOFTWARE", fg="black",  bg="#A9A9A9")
label1_1.pack(anchor=W)
label1_1.configure(font=("agency-fb", '30', 'bold'))

#create description label

label1_2=Label(frame1,  text="Use it for educational purposes only. Intended for general use.",bg="#A9A9A9")
label1_2.pack(anchor=W)
label1_2.configure(font=("agency-fb", '20', 'bold'))

#create bottom description label

label1_3=Label(frame1,  text="""It uses cryptography fernet module. it uses symmetric key encryption algorithm meaning same key is used
for both encryption and decryption. Do not change the cryptotext else it will not decrypt. Cryptotext must remain as it was encrypted.
 COPYRIGHT 2017. STEPHEN NJAI. ALL RIGHTS RESERVED.""",bg="#A9A9A9")
label1_3.pack(anchor=W)
label1_3.configure(font=("agency-fb", '13'))

#create symmetric key

key = Fernet.generate_key()
f= Fernet(key)

#create encrypt function

def encrypt():

    textvarA=textfieldA.get(1.0, END)    #gets user input from text field A.
    b=textvarA.encode()                  #converts the string to bytes.
    token = f.encrypt(b)                 #encrypts the bytes.
    textfieldB.insert(END, token)        #inputs the encrypted text into text field B
    keyvar=str(key)
    keyvar2=str(f)
    tkinter.messagebox._show("Symetric key.", "symmetric key used is: "+keyvar)

#create decrypt function
def decrypt():
    textvarB=textfieldB.get(1.0, END)    #gets the crypto text from input field B
    c=textvarB.encode()                  #converts the string to bytes.
    try:
        g= f.decrypt(c)                      #decrypts using same key used to encrypt.
        textfieldA.insert(END, g)            #inputs the decrypted text into text field A
    except:
        tkinter.messagebox.showerror("ERROR: Unable to decrypt", """The cryptotext you entered is invalid.
        Make sure it matches the original plaintext""") #if the cryptotext is invalid, then display a warning.


#delete textfield
def deleteAll():
    answer=tkinter.messagebox.askyesno("Delete all!", " do you want to delete all input text.") #show a confirm box.
    if answer==YES:                           #if user said yes, then delete
        textfieldB.delete(1.0, END)           #deletes the contents of text field A
        textfieldA.delete(1.0, END)           #deletes the contents of text field B

#create a source code  top level window
def sourceCode():
    top=Toplevel(bg="grey") #defines the top level window
    top.title("source code")  # gives the window a title.

    # create a scrollbar

    scrollbartext = Scrollbar(top, orient=VERTICAL, troughcolor="grey")
    scrollbartext.pack(side=RIGHT, fill=Y)

    #create a text widget to hold the code

    text2=Text(top, bg="black", fg="green",  yscrollcommand=scrollbartext.set, wrap=WORD, bd=20, relief=SUNKEN)
    text2.insert(INSERT, """



from tkinter import *
from cryptography.fernet import Fernet
import tkinter.messagebox

#configure main window
root=Tk()
root.title("Njai Cryptography Software")
root.configure(bg="#696969")

#configure top frame

frame1=Frame(root, height=200,  bg="#A9A9A9", bd=10, relief=SUNKEN)
frame1.pack(side=TOP, fill=X)

#create right frame label title: CRYPTOTEXT
labelB=Label(root, text="Cryptotext", bg="#696969", width=30)
labelB.pack(side=TOP,anchor=E)
labelB.configure(font=("agency-fb", '15', "bold", "underline"))

#create left frame label title: PLAINTEXT
labelA=Label(root, text="Plaintext", bg="#696969", width=30)
labelA.pack( side=TOP,anchor=W)
labelA.configure(font=("agency-fb", '15', "bold", "underline"))

#configure left frame for plaintext

frame2=Frame(root, height=400, width=500, bg="#DCDCDC", bd=10, relief=RAISED)
frame2.pack(side=LEFT)

#configure right frame for cryptotext

frame3=Frame(root, height=400, width=500, bg="#DCDCDC", bd=10, relief=RAISED)
frame3.pack(side=RIGHT)

#configure middle frame used for the buttons.

frame4=Frame(root, height=450, width=350, bg="#696969", bd=10, relief=RAISED)
frame4.pack(side=TOP)

#create title label

label1_1=Label(frame1, text="NJAI CRYPTOGRAPHY SOFTWARE", fg="black",  bg="#A9A9A9")
label1_1.pack(anchor=W)
label1_1.configure(font=("agency-fb", '30', 'bold'))

#create description label

label1_2=Label(frame1,  text="Use it for educational purposes only. Intended for general use.",bg="#A9A9A9")
label1_2.pack(anchor=W)
label1_2.configure(font=("agency-fb", '20', 'bold'))

#create bottom description label

label1_3=Label(frame1,  text="It uses cryptography fernet module. it uses symmetric key encryption algorithm meaning same key is used\nfor both encryption and decryption. Do not change the cryptotext else it will not decrypt. Cryptotext must remain as it was encrypted.\n# COPYRIGHT 2017. STEPHEN NJAI. ALL RIGHTS RESERVED.",bg="#A9A9A9")
label1_3.pack(anchor=W)
label1_3.configure(font=("agency-fb", '13'))

#create symmetric key

key = Fernet.generate_key()
f= Fernet(key)

#create encrypt function

def encrypt():

    textvarA=textfieldA.get(1.0, END)    #gets user input from text field A.
    b=textvarA.encode()                  #converts the string to bytes.
    token = f.encrypt(b)                 #encrypts the bytes.
    textfieldB.insert(END, token)        #inputs the encrypted text into text field B

#create decrypt function
def decrypt():
    textvarB=textfieldB.get(1.0, END)    #gets the crypto text from input field B
    c=textvarB.encode()                  #converts the string to bytes.
    try:
        g= f.decrypt(c)                      #decrypts using same key used to encrypt.
        textfieldA.insert(END, g)            #inputs the decrypted text into text field A
    except:
        tkinter.messagebox.showerror("ERROR: Unable to decrypt", "The cryptotext you entered is invalid.\nMake sure it matches the original plaintext") #if the cryptotext is invalid, then display a warning.

#delete textfield
def deleteAll():
    answer=tkinter.messagebox.askyesno("Delete all!", " do you want to delete all input text.") #show a confirm box.
    if answer==YES:                           #if user said yes, then delete
        textfieldB.delete(1.0, END)           #deletes the contents of text field A
        textfieldA.delete(1.0, END)           #deletes the contents of text field B

#create a source code  top level window
def sourceCode():
    top=Toplevel(bg="grey") #defines the top level window
    top.title("source code")  # gives the window a title.

    # create a scrollbar

    scrollbartext = Scrollbar(top, orient=VERTICAL, troughcolor="grey")
    scrollbartext.pack(side=RIGHT, fill=Y)

    #create a text widget to hold the code

    text2=Text(top, bg="black", fg="green",  yscrollcommand=scrollbartext.set, wrap=WORD, bd=20, relief=SUNKEN)
    text2.insert(INSERT, """ """) #inserts the code
    text2.pack(fill=BOTH, expand=YES)

    #connect scrollbar to text widget
    scrollbartext.config(command=text2.yview)


#create exit function
def exitApp():
    answer=tkinter.messagebox.askquestion("Confirm", "Do you want to Exit application?")  #shows the pop up box.
    if answer == 'yes':  #if user clicks yes, then exit application
        root.quit()

#create the encrypt button
butt1=Button(frame4, text="encrypt", command=encrypt, width=30, pady=10, bd=5)
butt1.pack(anchor=N)

#create decrypt button
butt2=Button(frame4, text="Decrypt", command=decrypt, width=30, pady=10, bd=5)
butt2.pack()

#create delete button
butt3=Button(frame4, text="Delete all", command=deleteAll, width=30, pady=10, bd=5)
butt3.pack(anchor=S)

#create scrollbar for text field A
scrollbarA=Scrollbar(frame2, orient=VERTICAL, bd=3)
scrollbarA.pack(side=RIGHT, fill=Y)

#create scrollbar for text filed B
scrollbarB=Scrollbar(frame3, orient=VERTICAL, bd=3)
scrollbarB.pack(side=RIGHT, fill=Y)

#create text field A
textfieldA=Text(frame2, bg="#DCDCDC", height=20, width=70, yscrollcommand=scrollbarA.set, fg="green", selectbackground="grey")
textfieldA.pack()

#create text field B
textfieldB=Text(frame3, bg="#DCDCDC",height=20, width=70, yscrollcommand=scrollbarB.set, fg="green", selectbackground="red")
textfieldB.pack()

#connect scrollbarA to textfieldA
scrollbarA.config(command=textfieldA.yview)

#connect scrollbarB to textfieldB
scrollbarB.config(command=textfieldB.yview)

#create exit button
butt5=Button(frame4, text="Exit", command=exitApp)
butt5.pack(side=BOTTOM)

#create source code button
butt4=Button(frame4, text="view source code", command=sourceCode)
butt4.pack(side=BOTTOM)



root.mainloop()


# COPYRIGHT 2017. STEPHEN NJAI. ALL RIGHTS RESERVED.













     """) #inserts the code
    text2.pack(fill=BOTH, expand=YES)

    #connect scrollbar to text widget
    scrollbartext.config(command=text2.yview)


#create exit function
def exitApp():
    answer=tkinter.messagebox.askquestion("Confirm", "Do you want to Exit application?")  #shows the pop up box.
    if answer == 'yes':  #if user clicks yes, then exit application
        root.quit()

#create the encrypt button
butt1=Button(frame4, text="encrypt", command=encrypt, width=30, pady=10, bd=5)
butt1.pack(anchor=N)

#create decrypt button
butt2=Button(frame4, text="Decrypt", command=decrypt, width=30, pady=10, bd=5)
butt2.pack()

#create delete button
butt3=Button(frame4, text="Delete all", command=deleteAll, width=30, pady=10, bd=5)
butt3.pack(anchor=S)

#create scrollbar for text field A
scrollbarA=Scrollbar(frame2, orient=VERTICAL, bd=3)
scrollbarA.pack(side=RIGHT, fill=Y)

#create scrollbar for text filed B
scrollbarB=Scrollbar(frame3, orient=VERTICAL, bd=3)
scrollbarB.pack(side=RIGHT, fill=Y)

#create text field A
textfieldA=Text(frame2, bg="#DCDCDC", height=20, width=70, yscrollcommand=scrollbarA.set, fg="green", selectbackground="grey")
textfieldA.pack()

#create text field B
textfieldB=Text(frame3, bg="#DCDCDC",height=20, width=70, yscrollcommand=scrollbarB.set, fg="green", selectbackground="red")
textfieldB.pack()

#connect scrollbarA to textfieldA
scrollbarA.config(command=textfieldA.yview)

#connect scrollbarB to textfieldB
scrollbarB.config(command=textfieldB.yview)

#create exit button
butt5=Button(frame4, text="Exit", command=exitApp)
butt5.pack(side=BOTTOM)

#create source code button
butt4=Button(frame4, text="view source code", command=sourceCode)
butt4.pack(side=BOTTOM)



root.mainloop()

# COPYRIGHT 2017. STEPHEN NJAI. ALL RIGHTS RESERVED.