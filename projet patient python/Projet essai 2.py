import shutil
def ajout_patient():
    DPatient = {}
    DPatient["CIN"] = input("Donner le CIN du patient : ")
    DPatient["nom"] = input("Donner le nom du patient : ")
    DPatient["prenom"] = input("Donner le prenom du patient : ")
    DPatient["age"] = input("Donner l'age du patient : ")
    s = input("Donner le sex du patient H/F : ")
    s.upper()
    #upper ne fonctionne pas !!
    while (s!='H') and (s!='F') :
        s = input("Donner le sex du patient : ")
    if s == 'H':
        sex = "Homme"
    else:
        sex = "femme"
    global lignePa
    lignePa = DPatient["CIN"] + ";" + DPatient["nom"] + ";" + DPatient["prenom"] + ";" + sex + ";" + DPatient["age"]
    print (lignePa)
    P = open("patient.txt", "a+")
    P.write(lignePa + '\n')
    P.close()
    print("Le Patient s'est enregistré avec succée")
    accueil()

def supprime_patient():
    elem = input ("donner le CIN du patient à Supprimer ")
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
        print ("ERREUR LE PATIENT N'EXISTE PAS ")
    else:
        for j in range(0, len(ligne)):
            if j == i:
                continue
            else:
                P1.write(ligne[j])
        print ("Le Patient est Supprimer")
        P1.close()
        shutil.copyfile("patient101.txt", "patient.txt")
    P.close()
    accueil()

def accueil():
    print("********************************************************************")
    print("1-Ajouter Patient ")
    print("2-Supprimer Patient ")
    print("3-Ajoutez Rendez-vous ")
    print("4-Annuler Rendez-vous ")
    print("5-Modifier un Rendez-vous ")
    print("6-Créer une Ordonnance ")
    print("7-Historique Patient ")
    print("8-Tracer la Courbe de nombre des consultations par mois ")
    print("9-Tracer la Courbe de nombre des consultations par année ")
    print("10-Afficher la liste des Patients :")
    print("11-Afficher la liste des Rendez-vous :")
    print("0-Quitter ")
    print("********************************************************************")
    instruction = int(input("Instruction : "))
    work(instruction)

def affiche_patient():
    P = open("patient.txt", "r+")
    ligne = P.readlines()
    print ("La Liste des Patients : ")
    for i in range(0, len(ligne)):
        a, b, c, d, e = ligne[i].split(";")
        text="CIN :" + a + "   Nom :" + b + "   Prenom :" + c + "   Sex :" + d + "   Age :" + e
        print(text)
    P.close()
    accueil()

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
def ajou_rdv():
    date = input("Entrer la date du rendez-vous sous la forme jj/mm/aaaa ")
    heure=input("Entrer l'Heure du Rendez-vous sous la forme 00:00 : ")
    heure.strip()
    date.strip()
    liste = date.split("/")
    liste1=heure.split(":")
    if verife_heure(liste1) and verifie_date(liste):
        id =input ("donner le CIN du patient")
        R = open("rdv.txt", "a")
        ligneRd = str(date) + ";" +str(heure)+";"+ str(id) + ";"
        R.write(ligneRd + '\n')
        R.close()
        print ("Le rendez-vous a ete enregistre ")
    else:
        print ("Erreur Dans la forme de Date 00/00/0000 ! ou d'heure 00:00 !")
    accueil()

def annule_rdv():
    patient = input("donner le CIN du patient qui va annuler : ")
    patient.strip()
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    existe = False
    for i in range(0, len(ligne)):
        a, b, c,d = ligne[i].split(";")
        if c == patient:
            existe = True
            break
    R1 = open("rdv101.txt", "w+")
    if existe == False:
        print("Le patient n'a pas de rendez-vous ")
    else:
        for j in range(0, len(ligne)):
            if j == i:
                continue
            else:
                R1.write(ligne[j])
        print ("le rendez-vous a ete annuler")
        R1.close()
        shutil.copyfile("rdv101.txt", "rdv.txt")
    R.close()
    accueil()

def modif_rdv():
    patient=input("donner le CIN du patient qui va modifier :")
    patient.strip()
    valide=False
    while valide == False:
        rdv = input("donner la nouvelle date sous la forme 00/00/0000: ")
        rdv.strip()
        heure = input("Entrer l'Heure du Rendez-vous sous la forme 00:00 : ")
        heure.strip()
        liste = rdv.split("/")
        liste1 = heure.split(":")
        if verife_heure(liste1) and verifie_date(liste):
            valide = True
            text = str(rdv) + ";" +str(heure)+";"+ str(patient) + ";"
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    existe = False
    for i in range(0, len(ligne)):
        a, b, c,d = ligne[i].split(";")
        if c == patient:
            existe = True
            break
    R1 = open("rdv101.txt", "w+")
    if existe == False:
        print("Le patient n'a pas de rendez-vous ")
    else:
        for j in range(0, len(ligne)):
            if j == i:
                R1.write(text+'\n')
            else:
                R1.write(ligne[j])
        print("le rendez-vous a ete Modifier")
        R1.close()
        shutil.copyfile("rdv101.txt", "rdv.txt")
    R.close()
    accueil()

def afficher_rdv():
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    print("La Liste des Rendez-vous : ")
    for i in range(0, len(ligne)):
        a, b, c,d = ligne[i].split(";")
        text = "date :" + a + "   heure :" + b+ "   CIN :" + c
        print(text)
    R.close()
    accueil()

def supprimer_rdv(patient):
    R = open("rdv.txt", "r")
    ligne = R.readlines()
    for i in range(0, len(ligne)):
        a, b, c, d = ligne[i].split(";")
        if c == patient:
            print ("ok")
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

def creer_ordo():
    patient=input("donner le CIN du patient à qui appartient l'Ordonnance : ")
    patient.strip()
    P = open("patient.txt", "r")
    ligne = P.readlines()
    existe = False
    for i in range(0, len(ligne)):
        a, b, c, d, e = ligne[i].split(";")
        if a == patient:
            existe = True
            ligne01=a + " " + c + " " + b +" "
            print (ligne01)
            nom_fichier="Historique "+c+" "+b+".txt"
            break
    R = open("rdv.txt", "r")
    lignes = R.readlines()
    for i in range(0, len(lignes)):
        f, g, h, i = lignes[i].split(";")
        if h == patient:
            existe = True
            ligne02=f + " " + g
            print (ligne02)
            break
    nbr_medicamment=int(input("donner le nbr de medicamment : "))
    if existe == False:
        print("ERREUR le Patient n'a pas de Rendez-vous et/ou de fiche ! ")
    else:
        ligne1 = ligne01 + ligne02 + '\n'
        O=open(nom_fichier, "a+")
        print (ligne1)
        O.write(ligne1)
        for i in range (0,nbr_medicamment):
            print ("------Medicamment ",i+1,"-------------")
            nom=input("donner le nom du medicamment : ")
            quantite=input("donner la quantite : ")
            dure=input("donner la duréé de traitement : ")
            ligne2=nom+" "+quantite+" "+dure+"jrs"+'\n'
            O.write(ligne2)
        O.write("---------------------------------------------------\n")
        O.close()
        print("L'ordonnance a éte enregistré")
    supprimer_rdv(patient)
    #Il ya un probleme de suppression lorsque c'est le dernier element
    ajouter=input("Voulez-vous ajouter la date du prochain Rendez-vous O/N : ")
    ajouter.upper()
    if ajouter=='O':
        ajou_rdv()
    accueil()

def histo_patient():
    patient = input("donner le CIN du patient à qui appartient l'Ordonnance : ")
    patient.strip()
    P = open("patient.txt", "r")
    ligne = P.readlines()
    existe = False
    for i in range(0, len(ligne)):
        a, b, c, d, e = ligne[i].split(";")
        if a == patient:
            existe = True
            nom_fichier = "Historique " + c + " " + b + ".txt"
            break
    O = open(nom_fichier, "r")
    lignes = O.readlines()
    for i in range(0, len(ligne)+1):
        ch=lignes[i].replace("\n","")
        print(ch)
    print ("")
    accueil()

def courbe_mois():
    print("working...")
def courbe_annee():
    print("working...")

def work(instruction):
    while instruction != 0:
        if instruction == 1:
            ajout_patient()
        elif instruction == 2:
            supprime_patient()
        elif instruction == 3:
            ajou_rdv()
        elif instruction == 4:
            annule_rdv()
        elif instruction == 5:
            modif_rdv()
        elif instruction == 6:
            creer_ordo()
        elif instruction == 7:
            histo_patient()
        elif instruction == 8:
            courbe_mois()
        elif instruction == 9:
            courbe_annee()
        elif instruction == 10:
            affiche_patient()
        elif instruction == 11:
            afficher_rdv()

accueil()

