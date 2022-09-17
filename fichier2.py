#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
#cd AppData\Local\Programs\Python\Python39
#python -m pip install mysql-connector-python




def Ajouter():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere  = txtmatiere.get()
    note  = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO note (code, nom, prenom, sexe, classe, matiere, notes) VALUES (%s, %s, %s,%s, %s, %s, %s) "
        val = (matricule, nom,prenom, sexe,classe, matiere ,note )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note ajouter")
        root.destroy()
        call(["python", "Chambre2.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


def Modifer():
    matricule = txtNumero.get()
    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere  = txtmatiere.get()
    note  = txtnote.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "update note set  nom=%s,prenom= %s,sexe= %s,classe=%s,matiere= %s,notes= %s where code= %s "
        val = (nom,prenom, sexe,classe, matiere ,note, matricule )
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note modifier")
        root.destroy()
        call(["python", "Chambre2.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()



def Supprimer():
    matricule = txtNumero.get()

    maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
    meConnect = maBase.cursor()

    try:
        sql = "delete from note where code= %s "
        val = ( matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information", "Note Supprimer")
        root.destroy()
        call(["python", "Chambre.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()




#Ma fenetre
root  = Tk()

root.title("MENUE PRINCIPALE")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "GESTION NOTES DES ETUDIANTS", font = ("Sans Serif", 25), background = "#2F4F4F", fg="#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Detail des eleves

#Matricule
lblNumero = Label(root, text="MATRICULE", font=("Arial", 18), bg="#153c77", fg="white")
lblNumero.place(x=70, y=150, width=150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=250,y=150,width=150)

#Nom
lblnom = Label(root, text="NOM", font=("Arial", 18), bg="#153c77", fg="white")
lblnom.place(x=70, y=200, width=150)
txtnom = Entry(root,bd=4, font=("Arial", 14))
txtnom.place(x=250,y=200,width=300)
#Prenom
lblprenom = Label(root, text="PRENOM", font=("Arial", 18), bg="#153c77", fg="white")
lblprenom.place(x=70, y=250, width=150, )
txtprenom = Entry(root,bd=4, font=("Arial", 14))
txtprenom.place(x=250,y=250,width=300)

#sexe

valeurSexe = StringVar()

lblSexeMasculin = Radiobutton(root, text="MASCULIN", value="M",variable=valeurSexe, indicatoron=0, font=("Arial", 14), bg="#153c77", fg="#696969")
lblSexeMasculin.place(x=250, y=300, width=130)
txtSexeFeminin = Radiobutton(root,text="FEMININ",value="F", variable=valeurSexe, indicatoron=0,font=("Arial", 14), bg="#153c77", fg="#696969")
txtSexeFeminin.place(x=420,y=300,width=130)

#Classe
lblClasse = Label(root, text="CLASSE", font=("Arial", 18), bg="#153c77", fg="white")
lblClasse.place(x=70, y=350, width=150, )

comboClasse = ttk.Combobox(root,font=("Arial", 14))
comboClasse['values'] = ['CP ', 'CE1', 'CE2', 'CM1 ', 'CM2 ', '6e', '5e ', '4e ', '3e']
comboClasse.place(x=250, y=350, width=130)

#Matiere
lblmatiere = Label(root, text="MATIERE", font=("Arial", 18), bg="#153c77", fg="white")
lblmatiere.place(x=70, y=400, width=150, )
txtmatiere = Entry(root,bd=4, font=("Arial", 14))
txtmatiere.place(x=250,y=400,width=300)

#note
lblnote = Label(root, text="NOTE", font=("Arial", 18), bg="#153c77", fg="white")
lblnote.place(x=70, y=450, width=150, )
txtnote = Entry(root,bd=4, font=("Arial", 14))
txtnote.place(x=250,y=450,width=200)


#Enregistrer
btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#003aff", fg = "white", command=Ajouter)
btnenregistrer.place(x=250, y= 500, width=200)

#modifier
btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#003aff", fg = "white", command=Modifer)
btnmodofier.place(x=250, y= 550, width=200)

#Supprimer
btnSupprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "#003aff", fg = "white", command=Supprimer)
btnSupprimer.place(x=250, y= 600, width=200)

#Table
table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6, 7), height = 5, show = "headings")
table.place(x = 560,y = 150, width = 790, height = 450)

#Entete
table.heading(1 , text = "MAT")
table.heading(2 , text = "NOM")
table.heading(3 , text = "PRENOM")
table.heading(4 , text = "SEXE")
table.heading(5 , text = "CLASSE")
table.heading(6 , text = "MATIERE")
table.heading(7 , text = "NOTE")

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 150)
table.column(3,width = 150)
table.column(4,width = 100)
table.column(5,width = 50)
table.column(6,width = 100)
table.column(7,width = 50)


# afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root",password="", database="note_eleve")
meConnect = maBase.cursor()
meConnect.execute("select * from note")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

#Execution
root.mainloop()