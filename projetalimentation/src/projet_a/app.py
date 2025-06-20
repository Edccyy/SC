from .data import O_besoins
from .aliments import ajouter_aliment
from .besoins import ajouter_besoins
from .ilfautunnom import besoins, aliment
from .optimisation import optimisation
from .Diagramme2   import plot_kiviat

"""
Ce fichier contient le code principal de l'application.
Il permet de gérer les besoins nutritionnels, d'ajouter des aliments,
et de calculer la liste d'aliments à consommer pour répondre aux besoins.

Appuyer sur "1" pour changer les besoins nutritionnels,
"2" pour ajouter un aliment,
"3" pour calculer la liste d'aliments à consommer,
et "4" pour quitter l'application.


Pour ajouter un aliment, il faut fournir les informations suivantes :
    - Besoins en protéines
    - Besoins en lipides
    - Besoins en glucides
    - Besoins en calories
    - Besoins en fer
    - Besoins en calcium
    - Besoins en fibres
    - Prix de l'aliment
    - Nom de l'aliment

Pour changer les besoins nutritionnels, il faut fournir les informations suivantes :
    - Besoins en protéines
    - Besoins en lipides
    - Besoins en glucides
    - Besoins en calories
    - Besoins en fer
    - Besoins en calcium
    - Besoins en fibres
    - Nombre de jours

Pour lancer le programme, faire tourner le fichier demo.py
"""


def run():
    
    Menu = 0
    besoins_saisie = False
    N_besoins = besoins(O_besoins[0], O_besoins[1], O_besoins[2], O_besoins[3], O_besoins[4], O_besoins[5], O_besoins[6])
    apports_obtenus = besoins(0,0,0,0,0,0,1)

    while(True):
        if(Menu == 0):
            print("Que voulez-vous faire ?")
            print("1 - Changer les besoins")
            print("2 - Ajouter un aliment")
            print("3 - Calculer la liste d'aliments à consommer")
            print("4 - Quitter")

            result = int(input())

            if(1<= result <= 4):
                Menu = result
            else:
                print("Input invalide")
        elif(Menu == 1):
            result = ""
            resultatValide = False
            while(not resultatValide):
                print("Rentrez le besoins en proteine : ")
                P = float(input())
                print("Rentrez le besoins en lipides : ")
                L = float(input())
                print("Rentrez le besoins en glucide : ")
                G = float(input())
                print("Rentrez le besoins en calories : ")
                C = float(input())
                print("Rentrez le besoins en fer : ")
                F = float(input())
                print("Rentrez le besoins en calcium : ")
                Ca = float(input())
                print("Rentrez le besoins en fibres : ")
                Fi = float(input())
                print("Rentrez le nombre de jours : ")
                J = int(input())
                if(P < 0 or L < 0 or G < 0 or C < 0 or F < 0 or Ca < 0 or Fi < 0 or J <= 0):
                    print("Les besoins doivent être positifs et le nombre de jours doit être supérieur à 0 !\n")
                    resultatValide = False
                else:
                    N_besoins = besoins(P, L, G, C, F, Ca, Fi, J)
                    ajouter_besoins(N_besoins)
                    resultatValide = True
                    besoins_saisie = True
            Menu = 0
        elif(Menu == 2):
            result = ""
            resultatValide2 = False
            while(not resultatValide2):
                print("Rentrez le besoins en proteine : ")
                P1 = float(input())
                print("Rentrez le besoins en lipides : ")
                L1 = float(input())
                print("Rentrez le besoins en glucide : ")
                G1 = float(input())
                print("Rentrez le besoins en calories : ")
                C1 = float(input())
                print("Rentrez le besoins en fer : ")
                F1 = float(input())
                print("Rentrez le besoins en calcium : ")
                Ca1 = float(input())
                print("Rentrez le besoins en fibres : ")
                Fi1 = float(input())
                print("Rentrez le prix de l'aliment : ")
                Pr1 = float(input())
                print("Rentrez le nom de l'aliment : ")
                N = str(input())
                if(P1 < 0 or L1 < 0 or G1 < 0 or C1 < 0 or F1 < 0 or Ca1 < 0 or Fi1 < 0 or Pr1 < 0):
                    print("Les besoins doivent être positifs et le prix doit être supérieur à 0 !\n")
                    resultatValide = False
                else:
                    ajouter_aliment(aliment(N,P1, L1, G1, C1, F1, Ca1, Fi1, Pr1))
                    resultatValide2 = True
            Menu = 0
        elif(Menu == 3):
            optimisation(N_besoins)
            afficher_kiviat = input("Voulez-vous afficher le diagramme de Kiviat ? (o/n) : ").strip().lower()
            if afficher_kiviat == "o":
                if besoins_saisie == False:
                    plot_kiviat(N_besoins, apports_obtenus, "Diagramme de Kiviat des besoins de base")
                else:
                    plot_kiviat(N_besoins, apports_obtenus, "Diagramme de Kiviat des besoins répondus")
            print("Merci d'avoir utilisé le programme !")
            break
        elif(Menu == 4):
            print("Merci d'avoir utilisé le programme !")
            break
