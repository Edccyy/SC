from data import Al, A
from aliments import ajouter_aliment
from besoins import ajouter_besoins
from __class__ import *

def run():
    
    Menu = 0
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
                P = int(input())
                print("Rentrez le besoins en lipides : ")
                L = int(input())
                print("Rentrez le besoins en glucide : ")
                G = int(input())
                print("Rentrez le besoins en calories : ")
                C = int(input())
                print("Rentrez le besoins en fer : ")
                F = int(input())
                print("Rentrez le besoins en calcium : ")
                Ca = int(input())
                print("Rentrez le besoins en fibres : ")
                Fi = int(input())
                print("Rentrez le nombre de jours : ")
                J = int(input())
                if(P < 0 or L < 0 or G < 0 or C < 0 or F < 0 or Ca < 0 or Fi < 0 or J <= 0):
                    print("Les besoins doivent être positifs et le nombre de jours doit être supérieur à 0 !\n")
                    resultatValide = False
                else:
                    ajouter_besoins(besoins(P, L, G, C, F, Ca, Fi, J))
                    resultatValide = True
            Menu = 0
        elif(Menu == 2):
            result = ""
            resultatValide2 = False
            while(not resultatValide2):
                print("Rentrez le besoins en proteine : ")
                P = int(input())
                print("Rentrez le besoins en lipides : ")
                L = int(input())
                print("Rentrez le besoins en glucide : ")
                G = int(input())
                print("Rentrez le besoins en calories : ")
                C = int(input())
                print("Rentrez le besoins en fer : ")
                F = int(input())
                print("Rentrez le besoins en calcium : ")
                Ca = int(input())
                print("Rentrez le besoins en fibres : ")
                Fi = int(input())
                print("Rentrez le nom de l'aliment : ")
                N = int(input())
                if(P < 0 or L < 0 or G < 0 or C < 0 or F < 0 or Ca < 0 or Fi < 0):
                    print("Les besoins doivent être positifs et le nombre de jours doit être supérieur à 0 !\n")
                    resultatValide = False
                else:
                    ajouter_aliment(aliment(N,P, L, G, C, F, Ca, Fi))
                    resultatValide2 = True
            Menu = 0
        elif(Menu == 3):
            if resultatValide == False:
                optimisation(B_besoins)
            else:
                optimisation(N_besoins)
            print("Merci d'avoir utilisé le programme !")
        elif(Menu == 4):
            print("Merci d'avoir utilisé le programme !")
            break
        