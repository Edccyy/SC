from src.projet_a.data import *
from src.projet_a.aliments import ajouter_aliment
from src.projet_a.besoins import ajouter_besoins
from src.projet_a.ilfautunnom import *
from src.projet_a.optimisation import optimisation


def run():
    
    Menu = 0
    besoins_saisie = False
    N_besoins = besoins(O_besoins[0], O_besoins[1], O_besoins[2], O_besoins[3], O_besoins[4], O_besoins[5], O_besoins[6])

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
            if besoins_saisie == False:
                optimisation(N_besoins)
            else:
                optimisation(N_besoins)
            print("Merci d'avoir utilisé le programme !")
            break
        elif(Menu == 4):
            print("Merci d'avoir utilisé le programme !")
            break
        