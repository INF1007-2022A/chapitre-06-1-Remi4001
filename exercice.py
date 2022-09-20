#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:

    if values is None:
        input_string = input("Veuillez entrer 10 valeurs "
                             "séparées par un espace: ")
        values = input_string.split()

    values.sort()

    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        input_string = input("Entrez 2 mots séparés par un espace pour "
                             "vérifier s'ils sont des anagrames: ")
        words = input_string.split()

    if sorted(words[0]) == sorted(words[1]):
        return True
    else:
        return False


def contains_doubles(items: list) -> bool:
    items.sort()
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    meilleur_nom = ""
    meilleure_moyenne = 0

    for nom, notes in student_grades.items():
        moyenne = 0
        for note in notes:
            moyenne += note
        moyenne /= len(notes)

        if moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur_nom = nom

    return {meilleur_nom: meilleure_moyenne}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(
        f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
