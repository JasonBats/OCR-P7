import os
import json
import csv
from model import Action


def create_actions_objects_json():
    database_path = os.path.join(os.path.dirname(__file__),
                                 'datas', 'actions.json')
    with open(database_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    actions = []

    for action in data:
        action_object = Action(**action)
        actions.append(action_object)
    return actions

def create_actions_objects_csv():
    database_path = os.path.join(os.path.dirname(__file__),
                                 'datas', 'actions.csv')
    with open(database_path, 'r') as csv_file:
        data = csv.reader(csv_file, delimiter=";")

        actions = []

        for action in data:
            action_object = Action(name=action[0], price=float(action[1]), benefit=float(action[2]))
            actions.append(action_object)
    csv_file.close()
    return actions


def dynamic_wallet(capacite, actions):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, capacite + 1):
            if actions[i-1].price <= w:
                matrice[i][w] = max(actions[i-1].profit + matrice[i-1][w-actions[i-1].price], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = capacite
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        a = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-a.price] + a.profit:
            actions_selection.append(a)
            w -= a.price

        n -= 1

    print(actions_selection)
    return matrice[-1][-1], actions_selection


# dynamic_wallet(capacite=500, actions=create_actions_objects_json())
dynamic_wallet(capacite=500, actions=create_actions_objects_csv())
