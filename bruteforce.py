import os
import json
from model import Action
import itertools
import time
import psutil


def create_actions_objects():
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


def get_all_combinations():
    """
    Browse every combination possible of actions, regardless of their prices.
    :return: A list of all combination possible.
    """
    actions = create_actions_objects()
    combinations = []
    for L in range(0, len(actions) + 1):
        for i in itertools.combinations(actions, L):
            combinations.append(i)
    print('Toutes les combinaisons possibles ont été stockées')
    return combinations


def get_combinations_values(combinations, budget):
    """
    Browse every combinations and calculate the cost and the profit
    of each combination.
    :param combinations: Created by get_all_combinations()
    :param budget: specified by user
    :return: a print of the most profitable combination after the budget.
    """
    combinations_with_values = []
    for combination in combinations:
        price = 0
        profit = 0
        for action in combination:
            price += action.price
            profit += action.profit
        combination_with_values = [combination, price, profit]
        if price <= budget:
            combinations_with_values.append(combination_with_values)
    best_combination = sorted(combinations_with_values,
                              key=lambda x: x[-1],
                              reverse=True)[0]
    print(f'Meilleure combinaison :{best_combination}')
    print(f'Prix : :{best_combination[1]}')
    print(f'Profit : :{round(best_combination[2], 2)}')


ping = time.perf_counter()
get_combinations_values(get_all_combinations(), budget=500)
pong = time.perf_counter()
print(f'Temps écoulé : {pong - ping:0.2f} secondes')
