import os
import json
from model import Action
import time


def create_actions_objects_json():
    """
    Create action objects from a json file.
    :return: Actions objects.
    """
    database_path = os.path.join(os.path.dirname(__file__),
                                 'datas', 'actions.json')
    with open(database_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    actions = []

    for action in data:
        action_object = Action(**action)
        actions.append(action_object)
    return actions


def dynamic_wallet(capacite, actions):
    """
    Knapsack algorithm.
    Creates a matrix where rows represent available actions and columns
    different possible capacities of the wallet, from 0 to 'capacity'.
    After filling out the matrix, the function traces back the selected actions
    to maximize the profit.
    :param capacite: The maximum capacity of the wallet, expressed in cents.
    :param actions: A list of 'Action' objects, each having a 'price',
    and a 'profit'.
    :return: A tuple containing the best set of actions to buy
    within a given budget.
    """
    ping = time.perf_counter()
    matrix = [[0 for x in range(capacite + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, capacite + 1):
            if actions[i-1].price <= w:
                matrix[i][w] = max(actions[i-1].profit + matrix[i-1][w-actions[i-1].price], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]

    w = capacite
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        a = actions[n-1]
        if matrix[n][w] == matrix[n-1][w-a.price] + a.profit:
            actions_selection.append(a)
            w -= a.price

        n -= 1

    budget = 0
    benefit = 0
    for action in actions_selection:
        budget += action.price
        benefit += action.profit
    pong = time.perf_counter()
    print(f"Actions sélectionnées : {actions_selection}")
    print(f"Coût total : {budget}")
    print(f"Bénéfices : {benefit}")
    print(f"Temps d'exécution : {pong - ping:0.2f} secondes")
    return matrix[-1][-1], actions_selection


dynamic_wallet(capacite=500, actions=create_actions_objects_json())
