from tkinter import *
from PIL import Image,ImageTk
import shutil
import base64
import matplotlib.pyplot as plt

#les messages
def message_succes():
    succ=Tk()
    succ.title("Succes")
    succ.iconbitmap(r"logo.ico")
    succ.geometry("300x50+270+100")
    succes=Label(succ,text="La procedure s'est effectué avec succes").pack()
    succ.after(600, succ.destroy)
    succ.mainloop ()

def message_erreur() :
    err=Tk()
    err.title("ERREUR")
    err.iconbitmap(r"logo.ico")
    err.geometry("300x50+270+100")
    erreur = Label(err, text="le patient n'existe pas ! ").pack()
    err.after(700, err.destroy)
    err.mainloop()

def message_erreur_date():
    erreur = Tk()
    erreur.title("ERREUR")
    erreur.iconbitmap(r"logo.ico")
    erreur.geometry("300x50+270+100")
    erreurmsg = Label(erreur, text="RESPECTER LA FORME DE LA DATE ET HEURE").pack()
    erreur.after(700, erreur.destroy)
    erreur.mainloop()

def message_erreur_rdv():
    erreur = Tk()
    erreur.title("ERREUR")
    erreur.iconbitmap(r"logo.ico")
    erreur.geometry("300x50+270+100")
    erreurmsg = Label(erreur, text="Le patient n'a pas un Rendez-vous ! ").pack()
    erreur.after(700, erreur.destroy)
    erreur.mainloop()

def message_erreur_his():
    erreur = Tk()
    erreur.title("ERREUR")
    erreur.iconbitmap(r"logo.ico")
    erreur.geometry("300x50+270+100")
    erreurmsg = Label(erreur, text="Le patient n'a pas une Historique ! ").pack()
    erreur.after(700, erreur.destroy)
    erreur.mainloop()

def message_erreur_cin():
    erreur = Tk()
    erreur.title("ERREUR")
    erreur.iconbitmap(r"logo.ico")
    erreur.geometry("300x50+270+100")
    erreurmsg = Label(erreur, text="Le cin doit contenir 8 Chiffres ! ").pack()
    erreur.after(700, erreur.destroy)
    erreur.mainloop()

#les verifications
def verifie_date(liste):
    if (len(liste) == 3):
        if len(liste[0]) == 2 and len(liste[1]) == 2 and len(liste[2]) == 4:
            return(True)
    return(False)

def verife_heure(liste1):
    if (len(liste1)==2):
        if len(liste1[0])==2 and len(liste1[1])==2:
            return (True)
        else:
            return (False)
    else :
        return (False)

def verife_cin(cin):
    if len(cin)==8 and cin.isdigit() :
        return (True)
    else:
        return(False)

#les rendez-vous
def changerR():
    patient=cinpatient.get()
    cinpatient.delete(0,END)
    if verife_cin(patient):
        nvdate = nouveau_date.get()
        nvheure = nouveau_heure.get()
        nouveau_date.delete(0, END)
        nouveau_heure.delete(0, END)
        nvdate.strip()
        nvheure.strip()
        liste = nvdate.split("/")
        liste1 = nvheure.split(":")
        if verife_heure(liste1) and verifie_date(liste):
            text = str(nvdate) + ";" + str(nvheure) + ";" + str(patient) + ";"
        else:
            message_erreur_date()
        R = open("rdv.txt", "r")
        ligne = R.readlines()
        existe = False
        for i in range(0, len(ligne)):
            a, b, c, d = ligne[i].split(";")
            if c == patient:
                existe = True
                break
        R1 = open("rdv101.txt", "w+")
        if existe == False:
            message_erreur_rdv()
        else:
            for j in range(0, len(ligne)):
                if j == i:
                    R1.write(text + '\n')
                else:
                    R1.write(ligne[j])
            message_succes()
            R1.close()
            shutil.copyfile("rdv101.txt", "rdv.txt")
        R.close()
    else :
        message_erreur_cin()

def modifier_rdv():
    global root5
    root5 = Tk()
    root5.configure(bg="#FCFCFC")
    root5.geometry("670x600+270+100")
    root5.iconbitmap(r"logo.ico")
    root5.title("Annuler un Rendez-vous")
    textrdz = Label(root5, text="Entrer le CIN du patient qui va changer son Rdv : ").pack()
    global cinpatient,nouveau_date,nouveau_heure
    cinpatient = Entry(root5, width=50)
    cinpatient.pack()
    textnvdate = Label(root5, text="Entrer la nouvelle date sous la forme 00/00/0000 : ").pack()
    nouveau_date = Entry(root5, width=50)
    nouveau_date.pack()
    textnvheure = Label(root5, text="Entrer la nouvelle heure sous la forme 00:00 : ").pack()
    nouveau_heure = Entry(root5, width=50)
    nouveau_heure.pack()
    confirmer = Button(root5, text="Confirmer",command=changerR).pack()
    back = Button(root5, text="Retour à l'Acceuil", command=switchtoaccfromchanger).pack()

def supprimerR():
    patient=entrycin.get()
    entrycin.delete(0,END)
    if verife_cin(patient):
        patient.strip()
        R = open("rdv.txt", "r")
        ligne = R.readlines()
        existe = False
        for i in range(0, len(ligne)):
            a, b, c, d = ligne[i].split(";")
            if c == patient:
                existe = True
                break
        R1 = open("rdv101.txt", "w+")
        if existe == False:
            message_erreur_rdv()
        else:
            for j in range(0, len(ligne)):
                if j == i:
                    continue
                else:
                    R1.write(ligne[j])
            message_succes()
            R1.close()
            shutil.copyfile("rdv101.txt", "rdv.txt")
        R.close()
    else:
        message_erreur_cin()

def annuler_rendez_vous():
    global root4
    root4 = Tk()
    root4.configure(bg="#FCFCFC")
    root4.geometry("670x600+270+100")
    root4.iconbitmap(r"logo.ico")
    root4.title("Annuler un Rendez-vous")
    textrdz = Label(root4, text="Entrer le CIN du patient qui va annuler son Rdv : ").pack()
    global entrycin
    entrycin = Entry(root4, width=50)
    entrycin.pack()
    confirmer = Button(root4, text="Confirmer", command=supprimerR).pack()
    back = Button(root4, text="Retour à l'Acceuil", command=switchtoaccfromannuler).pack()

def enregistrerR() :
    patient=Rdzcin.get()
    Rdzcin.delete(0, END)
    if verife_cin(patient):
        date = entrydate.get()
        heure = entryheure.get()
        entrydate.delete(0, END)
        entryheure.delete(0, END)
        liste = date.split("/")
        liste1 = heure.split(":")
        if verife_heure(liste1) and verifie_date(liste):
            R = open("rdv.txt", "a")
            Rfix = open("copierdv.txt", "a")
            ligneRd = str(date) + ";" + str(heure) + ";" + str(patient) + ";"
            R.write(ligneRd + '\n')
            Rfix.write(ligneRd + '\n')
            R.close()
            Rfix.close()
            message_succes()
        else:
            message_erreur_date()
    else :
        message_erreur_cin()

def rendez_vous ():
    global root3
    root3=Tk()
    root3.configure(bg="#FCFCFC")
    root3.geometry("670x600+270+100")
    root3.iconbitmap(r"logo.ico")
    root3.title("Ajoutez un Rendez-vous")
    textrdz = Label(root3, text="Entrer la date du rendez-vous sous la forme jj/mm/aaaa ").pack()
    global entrydate
    entrydate = Entry(root3, width=50)
    entrydate.pack()
    textrheure = Label(root3, text="Entrer l'heure du rendez-vous sous la forme 00:00 ").pack()
    global entryheure
    entryheure = Entry(root3, width=50)
    entryheure.pack()
    entryheure.config(fg="grey")
    textcin = Label(root3, text="Entrer le cin du patient").pack()
    global Rdzcin
    Rdzcin = Entry(root3, width=50)
    Rdzcin.pack()
    confirmer = Button(root3, text="Confirmer", command=enregistrerR).pack()
    back=Button(root3,text="Retour à l'Acceuil", command=switchtoaccfromrdv).pack()
    root3.mainloop()

def affRdv():
    root0.destroy()
    global racinerdv
    racinerdv = Tk()
    racinerdv.configure(bg="#FCFCFC")
    racinerdv.geometry("670x600+270+100")
    racinerdv.iconbitmap(r"logo.ico")
    racinerdv.title("Liste Des Rendez-vous")
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    for i in range(0, len(ligne)):
        a, b, c, d = ligne[i].split(";")
        text = "date :" + a + "   heure :" + b + "   CIN :" + c
        Labelrdv=Label(racinerdv,text=text).pack()
    R.close()
    back = Button(racinerdv, text="Retour à l'Acceuil", command=switchtoaccfromaffR).pack()

def rdvpage():
    root0.destroy()
    global page
    page=Tk()
    page.configure(bg="#FCFCFC")
    page.title("Gerer les Rendez-vous")
    page.geometry("670x600+270+100")
    page.iconbitmap(r"logo.ico")
    appoint = Button(page, text="ajoutez un rendez-vous", height=3, width=25, background="#F5F5F5",command=switchtorendez).pack()
    annuler_appoint = Button(page, text="annuler un rendez-vous", height=3, width=25, background="#F5F5F5",command=switchtoannuler).pack()
    changer_appoint = Button(page, text="Changer un rendez-vous", height=3, width=25, background="#F5F5F5",command=switchtomodifier).pack()
    back=Button(page,text="retour à l'acceuil ",height=3, width=25, background="#F5F5F5",command=switchtoaccfromrdvpage).pack()
    page.mainloop()

#les patients
def supp ():
    elem = CINPS.get()
    CINPS.delete(0, END)
    if verife_cin(elem):
        P = open("patient.txt", "r")
        ligne = P.readlines()
        existe = False
        for i in range(0, len(ligne)):
            a, b, c, d, e = ligne[i].split(";")
            if a == elem:
                existe = True
                break
        P1 = open("patient101.txt", "w+")
        if existe == False:
            message_erreur()
        else:
            for j in range(0, len(ligne)):
                if j == i:
                    continue
                else:
                    P1.write(ligne[j])
            message_succes()
            P1.close()
            shutil.copyfile("patient101.txt", "patient.txt")
        P.close()
    else:
        message_erreur_cin()

def fenetre_supp():
    root0.destroy()
    i=1
    global root2
    root2 = Tk()
    root2.configure(bg="#FCFCFC")
    root2.geometry("670x600+270+100")
    root2.iconbitmap(r"logo.ico")
    root2.title("Supprimer un Patient")
    global CINPS
    textCINPS=Label(root2,text="Donner le CIN du patient à supprimer").pack()
    CINPS=Entry(root2,width=50)
    CINPS.pack()
    confirmer =Button(root2,text="confirmer",command=supp).pack()
    back = Button(root2, text="Retour à l'Acceuil", command=switchtoaccfromsupp).pack()
    root2.mainloop()

def enregistrerP():
    DPatient = {}
    pat=CIN.get()
    CIN.delete(0, END)
    if verife_cin(pat):
        DPatient["CIN"] = pat
        DPatient["nom"] = nom.get()
        DPatient["prenom"] = prenom.get()
        DPatient["age"] = age.get()
        if v.get() == 0 :
            sex = "Homme"
        else :
            sex = "femme"
        global lignePa
        lignePa = DPatient["CIN"] + ";" + DPatient["nom"] + ";" + DPatient["prenom"] + ";" + sex + ";" + DPatient["age"]
        P = open("patient.txt", "a+")
        P.write(lignePa + '\n')
        P.close()
        nom.delete(0, END)
        prenom.delete(0, END)
        age.delete(0, END)
        message_succes()
    else:
        message_erreur_cin()

def fenetre_ajout():
    global root
    root0.destroy()
    root = Tk()
    root.configure(bg="#FCFCFC")
    root.geometry("670x600+270+100")
    root.iconbitmap(r"logo.ico")
    root.title("Ajouter un Patient")
    global CIN,nom,prenom,age
    textcin=Label(root,text="Entrer votre CIN").pack()
    CIN = Entry(root, width=50)
    CIN.pack()
    textnom = Label(root, text="Entrer votre nom").pack()
    nom = Entry(root, width=50)
    nom.pack()
    textprenom = Label(root, text="Entrer votre prenom").pack()
    prenom = Entry(root, width=50)
    prenom.pack()
    global v
    v = IntVar()
    sex = Radiobutton(root, text="Homme", variable=v, value=0).pack()
    sex1 = Radiobutton(root, text="Femme", variable=v, value=1).pack()
    textage = Label(root, text="Entrer votre age").pack()
    age = Entry(root, width=50)
    age.pack()
    entrer = Button(root, text="Enregistrer le Patient", command=enregistrerP).pack()
    back=Button(root, text="Retour à l'Acceuil", command=switchtoaccfromajout).pack()
    root.mainloop()

def affPatients():
    root0.destroy()
    global racine
    racine=Tk()
    racine.configure(bg="#FCFCFC")
    racine.geometry("670x600+270+100")
    racine.iconbitmap(r"logo.ico")
    racine.title("Liste Des Patients")
    P = open("patient.txt", "r+")
    ligne = P.readlines()
    for i in range(0, len(ligne)):
        a, b, c, d, e = ligne[i].split(";")
        txtcin=Label(racine,text="CIN :"+a+"   Nom :"+b+"   Prenom :"+c+"   Sex :"+d+"   Age :"+e).pack()
    P.close()
    back = Button(racine, text="Retour à l'Acceuil", command=switchtoaccfromaffP).pack()
    racine.mainloop()

#les oradonnance
def enregistrerO():
    nom=nommd.get()
    quantite=quantitemd.get()
    duree=dureemd.get()
    nommd.delete(0,END)
    quantitemd.delete(0,END)
    dureemd.delete(0,END)
    O = open(nom_fichier, "a+")
    ligne2 = nom + " " + quantite + " " + duree + "jrs" + '\n'
    O.write(ligne2)
    O.write("---------------------------------------------------\n")
    O.close()
    message_succes()

def supprimerlerdv(patient):
    global sur
    sur=Tk()
    sur.title("NB")
    rootajouterord.destroy()
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    for i in range(0, len(ligne)):
        a, b, c, d = ligne[i].split(";")
        if c == patient:
            break
    R1 = open("rdv101.txt", "w+")
    for j in range(0, len(ligne)):
        if j == i:
            continue
        else:
            R1.write(ligne[j])
    R1.close()
    shutil.copyfile("rdv101.txt", "rdv.txt")
    R.close()
    supp=Label(sur,text="Le rendez Vous du "+ligne02+" est supprimer").pack()
    retour = Button(sur, text="Retour", command=switchtoordfromsur).pack()
    sur.mainloop()

def creer_ord():
    patient = cinenter.get()
    cinenter.delete(0, END)
    if verife_cin(patient):
        patient.strip()
        rootord.destroy()
        P = open("patient.txt", "r")
        ligne = P.readlines()
        existe1 = False
        existe2 = False
        for i in range(0, len(ligne)):
            a, b, c, d, e = ligne[i].split(";")
            if a == patient:
                existe1 = True
                ligne01 = a + " " + c + " " + b + " "
                global nom_fichier
                nom_fichier = "Historique " + c + " " + b + ".txt"
                break
        R = open("rdv.txt", "r")
        lignes = R.readlines()
        for i in range(0, len(lignes)):
            f, g, h, i = lignes[i].split(";")
            if h == patient:
                existe2 = True
                global ligne02
                ligne02 = f + " " + g
                break
        if existe1 == TRUE and existe2 == TRUE:
            ligne1 = ligne01 + ligne02 + '\n'
            O = open(nom_fichier, "a+")
            O.write(ligne1)
            O.close()
            global rootajouterord
            rootajouterord = Tk()
            rootajouterord.configure(bg="#FCFCFC")
            rootajouterord.geometry("670x600+270+100")
            rootajouterord.iconbitmap(r"logo.ico")
            rootajouterord.title("Ajouter une Ordonnance")
            textpa = Label(rootajouterord, text=ligne01).pack()
            global nommd, quantitemd, dureemd
            med1 = Label(rootajouterord, text="Donner le nom du medicamment").pack()
            nommd = Entry(rootajouterord, width=50)
            nommd.pack()
            med2 = Label(rootajouterord, text="Donner la quantité du medicamment").pack()
            quantitemd = Entry(rootajouterord, width=50)
            quantitemd.pack()
            med3 = Label(rootajouterord, text="Donner la durée de prise de medicamment").pack()
            dureemd = Entry(rootajouterord, width=50)
            dureemd.pack()
            cont = Button(rootajouterord, text="Enregistrer le medicamment", command=enregistrerO).pack()
            finir = Button(rootajouterord, text="finir l'Ordonnance", command=lambda: supprimerlerdv(patient)).pack()
        elif existe2 == False:
            message_erreur_rdv()
            Ord()
        else:
            message_erreur()
            Ord()
    else:
        message_erreur_cin()

def Ord():
    global rootord
    rootord = Tk()
    rootord.configure(bg="#FCFCFC")
    rootord.geometry("670x600+270+100")
    rootord.iconbitmap(r"logo.ico")
    rootord.title("Ajouter une Ordonnance")
    attention = Label(rootord, text="NB : Le patient doit avoir une fiche et un Rendez-vous d'abord ! ").pack()
    global cinenter
    textcin=Label(rootord,text="Donner le CIN du patient").pack()
    cinenter=Entry(rootord,width=50)
    cinenter.pack()
    confirmer = Button(rootord, text="Confirmer", command=creer_ord).pack()
    back = Button(rootord, text="Retour à l'Acceuil", command=switchtoaccfromord).pack()
    rootord.mainloop()

#historique
def histori():
    patient=Cinpatient.get()
    Cinpatient.delete(0,END)
    if verife_cin(patient):
        P = open("patient.txt", "r")
        ligne = P.readlines()
        existe1 = False
        for i in range(0, len(ligne)):
            a, b, c, d, e = ligne[i].split(";")
            if a == patient:
                existe1 = True
                ligne01 = a + " " + c + " " + b + " "
                global nom_fichier
                nom_fichier = "Historique " + c + " " + b + ".txt"
                break
        if existe1 == False:
            message_erreur()
        else:
            try:
                O = open(nom_fichier, "r")
                lignes = O.readlines()
                for i in range(0, len(lignes)):
                    ch = lignes[i].replace("\n", "")
                    texthistorique = Label(hist, text=ch).pack()
            except IOError:
                message_erreur_his()
    else:
        message_erreur_cin()

def afficherHis():
    root0.destroy()
    global hist
    hist=Tk()
    hist.title("Historique")
    hist.configure(bg="#FCFCFC")
    hist.geometry("670x600+270+100")
    hist.iconbitmap(r"logo.ico")
    textpa=Label(hist,text="Donner le CIN du patient").pack()
    global Cinpatient
    Cinpatient=Entry(hist,width=50)
    Cinpatient.pack()
    Confirmer=Button(hist,text="Confirmer",command=histori).pack()
    acc=Button(hist,text="Accueil",command=switchtoaccfromhis).pack()
    hist.mainloop()

#les courbes
def courbe_mois():
    f = open("copierdv.txt", 'r')
    freqMois = [0,0,0,0,0,0,0,0,0,0,0,0]
    L2 = []
    L = f.readlines()
    for i in L:
         L1=i.split(";")
         L2.append(L1[0])
    for l in L2:
        L3=l.split("/")
        freqMois[int(L3[1])-1]+=1
    f.close()
    mois=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
    plt.figure(figsize=(12, 5))
    plt.plot(mois,freqMois)
    plt.show()

def courbe_ans():
    f = open("copierdv.txt", 'r')
    freqAnnée = [0,0,0,0,0,0,0,0,0,0,0,0]
    Année=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
    L2 = []
    L = f.readlines()
    for i in L:
        L1=i.split(";")
        L2.append(L1[0])
    for l in L2:
        L3=l.split("/")
        for j in range(0,len(Année)):
            if L3[2] == Année[j]:
              break
        freqAnnée[j] += 1
    f.close()
    plt.figure(figsize=(12, 5))
    plt.plot(Année,freqAnnée)
    plt.show()

#les switch
def switchtoannuler():
    page.destroy()
    annuler_rendez_vous()

def switchtorendez():
    page.destroy()
    rendez_vous()

def switchtomodifier():
    page.destroy()
    modifier_rdv()

def switchtoaccfromajout():
    root.destroy()
    accueil()

def switchtoaccfromsupp():
    root2.destroy()
    accueil()

def switchtoaccfromrdv():
    root3.destroy()
    accueil()

def switchtoaccfromchanger():
    root5.destroy()
    accueil()

def switchtoaccfromannuler():
    root4.destroy()
    accueil()

def switchtoaccfromrdvpage():
    page.destroy()
    accueil()

def switchtoaccfromaffP():
    racine.destroy()
    accueil()

def switchtoaccfromaffR():
    racinerdv.destroy()
    accueil()

def switchtoaccfromord():
    rootord.destroy()
    accueil()

def switchtoordfromacc():
    root0.destroy()
    Ord()

def switchtoordfromsur():
    sur.destroy()
    Ord()

def switchtoaccfromhis():
    hist.destroy()
    accueil()

def accueil() :
    global root0
    root0=Tk()
    root0.configure(bg="#FCFCFC")
    my_img=ImageTk.PhotoImage(Image.open("patient1.png"))
    my_label=Label(image=my_img)
    my_label.grid(row=0,column=0,rowspan=3)
    my_img2 = ImageTk.PhotoImage(Image.open("patient2.png"))
    my_label2 = Label(image=my_img2)
    my_label2.grid(row=4, column=1, rowspan=3)
    root0.title("Acceuil")
    root0.geometry("670x600+270+100")
    root0.iconbitmap(r"logo.ico")
    ajout=Button(root0,text="Ajouter un Patient",height=3,width=25,background ="#F5F5F5",command=fenetre_ajout)
    ajout.grid(row=0,column=1)
    supprimer=Button(root0,text="Supprimer un Patient",height=3,width=25,command=fenetre_supp)
    supprimer.grid(row=1, column=1)
    rdv=Button (root0,text="Gerer les Rendez-vous : ",height=3,width=25,background ="#F5F5F5",command=rdvpage)
    rdv.grid(row=2,column=1)
    button_afficheP =Button (root0, text="Afficher la liste des Patients",height=5,width=25,background ="#FAF0E6",command=affPatients)
    button_afficheP.grid(row=1, column=2)
    button_afficheR = Button(root0, text="Afficher la liste des Rendez-vous", height=5, width=25, background="#FAF0E6",command=affRdv)
    button_afficheR.grid(row=4, column=2)
    button_historique = Button(root0, text="Afficher l'historique des Patients", height=5, width=25, background="#FAF0E6",command=afficherHis)
    button_historique.grid(row=6, column=2)
    button_ordonnance=Button(root0, text="Entrer une ordonnance", height=3, width=25, background="#F5F5F5",command=switchtoordfromacc)
    button_ordonnance.grid(row=4, column=0)
    button_courbe = Button(root0, text="nbr des consultations par mois", height=3, width=25, background="#F5F5F5",command=courbe_mois)
    button_courbe.grid(row=5, column=0)
    button_courbe2 = Button(root0, text="nbr de consultations par annee", height=3, width=25, background="#F5F5F5",command=courbe_ans)
    button_courbe2.grid(row=6, column=0)
    root0.mainloop()

accueil()