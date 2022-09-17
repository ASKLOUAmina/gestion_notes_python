#Les Bibliotheque a importer
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox


#Fonction Connecter
def Seconnecter():
    surnom = txtnomUtilisateur.get()
    mdp = txtmdp.get()
    if (surnom == "" and mdp == ""):
        messagebox.showerror("", "il faut rentrer les Données")
        txtmdp.delete("0", "end")
        txtnomUtilisateur.delete("0", "end")
    elif (surnom == "admin" and mdp == "admin"):
        messagebox.showinfo("", "Bienvenue")
        txtnomUtilisateur.delete("0", "end")
        txtmdp.delete("0", "end")
        root.destroy()
        call(["python", "fichier2.py"])

    else:
        messagebox.showwarning("", "Erreur de Connexion")
        txtmdp.delete("0", "end")
        txtnomUtilisateur.delete("0", "end")




#Ma fenetre
root  = Tk()

root.title("FENTRE DE CONNECTION")
root.geometry("400x300+450+200")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter le titre
lbltitre = Label(root,borderwidth = 3, relief = SUNKEN
                 , text = "Formulaire de connexion", font = ("Sans Serif", 25), background = "#091821", foreground="white")
lbltitre.place(x = 0, y = 0, width = 400)

lblnomUtilisateur = Label (root, text="Nom Utilisateur :", font=("Arial", 14),bg="#091821", fg="white")
lblnomUtilisateur.place(x = 5, y = 100,width = 150 )
txtnomUtilisateur = Entry(root,bd=4, font=("Arial", 13))
txtnomUtilisateur.place(x=150,y=100,width=200,height=30)

lblmdp = Label (root, text="Mot de Passe :", font=("Arial", 14),bg="#091821", fg="white")
lblmdp.place(x = 5, y = 150,width = 150 )
txtmdp = Entry(root,show="*",bd=4, font=("Arial", 13))
txtmdp.place(x=150,y=150,width=200,height=30)

#Bouton Connecter
btnenregistrer = Button(root, text = "Connexion", font = ("Arial", 16),bg ="#003aff", fg = "white", command=Seconnecter)
btnenregistrer.place(x=150, y= 200, width=200)



#Execution
root.mainloop()