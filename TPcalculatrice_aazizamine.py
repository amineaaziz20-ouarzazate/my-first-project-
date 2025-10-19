# calculatrice_aaziz.py
import math

# ----------------------
# Fonctions de calcul
# ----------------------
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Erreur: division par zéro impossible")
    return a / b

def puissance(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Erreur: modulo par zéro impossible")
    return a % b

def racine_carre(a):
    if a < 0:
        raise ValueError("Erreur: impossible de calculer la racine carrée d'un nombre négatif")
    return math.sqrt(a)

# ----------------------
# Dictionnaire des opérations
# ----------------------
OPERATIONS = {
    "+": {"func": addition, "type": "binaire"},
    "-": {"func": soustraction, "type": "binaire"},
    "*": {"func": multiplication, "type": "binaire"},
    "/": {"func": division, "type": "binaire"},
    "^": {"func": puissance, "type": "binaire"},
    "%": {"func": modulo, "type": "binaire"},
    "sqrt": {"func": racine_carre, "type": "unaire"}
}

# ----------------------
# Fonctions utilitaires
# ----------------------
def lire_nombre(message):
    while True:
        try:
            return float(input(message).replace(",", "."))
        except ValueError:
            print("Saisie invalide, veuillez entrer un nombre.")

def lire_entier(message):
    while True:
        val = input(message)
        if val.isdigit():
            return int(val)
        print("Saisie invalide, veuillez entrer un entier positif.")

def afficher_menu():
    print("\n=== CALCULATRICE AAZIZ ===")
    for symbole, info in OPERATIONS.items():
        print(f"{symbole} ({info['type']})")
    print("h (Historique)")
    print("e (Exporter historique)")
    print("s (Série d'opérations)")
    print("q (Quitter)")

def calculer(op, a, b=None):
    info = OPERATIONS[op]
    if info["type"] == "binaire":
        return info["func"](a, b)
    else:
        return info["func"](a)

# ----------------------
# Exporter l'historique
# ----------------------
def exporter_historique(historique):
    if not historique:
        print("Aucune opération à exporter.")
        return
    nom_fichier = input("Nom du fichier pour exporter l'historique: ")
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for ligne in historique:
            f.write(ligne + "\n")
    print(f"Historique exporté dans {nom_fichier}")

# ----------------------
# Calculer une série d'opérations
# ----------------------
def calculer_serie(historique, nb_decimales):
    print("=== Série d'opérations ===")
    resultat = lire_nombre("Premier nombre: ")
    while True:
        op = input("Opération suivante (ou 'fin'): ").lower()
        if op == "fin":
            print(f"Résultat final: {resultat:.{nb_decimales}f}")
            historique.append(f"Série finale = {resultat:.{nb_decimales}f}")
            break
        if op not in OPERATIONS:
            print("Opération invalide.")
            continue
        if OPERATIONS[op]["type"] == "binaire":
            b = lire_nombre("Second nombre: ")
            resultat = calculer(op, resultat, b)
            ligne = f"{resultat:.{nb_decimales}f} (après {op} {b})"
        else:
            resultat = calculer(op, resultat)
            ligne = f"{resultat:.{nb_decimales}f} (après {op})"
        print(f"Résultat intermédiaire: {ligne}")
        historique.append(ligne)

# ----------------------
# Programme principal
# ----------------------
def main():
    historique = []
    print("Bienvenue dans la calculatrice Aaziz !")
    nb_decimales = lire_entier("Nombre de décimales à afficher: ")

    while True:
        afficher_menu()
        choix = input("Votre choix: ").lower()

        if choix in ("q", "quit", "exit"):
            print("Au revoir !")
            break
        elif choix == "h":
            print("\n--- Historique ---")
            if historique:
                for ligne in historique:
                    print(ligne)
            else:
                print("Aucune opération.")
            continue
        elif choix == "e":
            exporter_historique(historique)
            continue
        elif choix == "s":
            calculer_serie(historique, nb_decimales)
            continue
        elif choix not in OPERATIONS:
            print("Choix invalide.")
            continue

        # Lecture des nombres
        a = lire_nombre("Premier nombre: ")
        b = None
        if OPERATIONS[choix]["type"] == "binaire":
            b = lire_nombre("Second nombre: ")

        # Calcul et affichage
        try:
            resultat = calculer(choix, a, b)
            if OPERATIONS[choix]["type"] == "unaire":
                ligne = f"{choix}({a}) = {resultat:.{nb_decimales}f}"
            else:
                ligne = f"{a} {choix} {b} = {resultat:.{nb_decimales}f}"
            print(f"Résultat: {ligne}")
            historique.append(ligne)
        except (ZeroDivisionError, ValueError) as e:
            print(e)
        except Exception as e:
            print(f"Erreur inattendue: {e}")

        cont = input("Continuer ? (o/n): ").lower()
        if cont not in ("o", "oui", "y", ""):
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
