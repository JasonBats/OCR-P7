import os
import json
import random
from model import Action


def create_actions_objects():
    database_path = os.path.join(os.path.dirname(__file__),
                                 'datas', 'actions.json')
    with open(database_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    actions = []

    for action in data:
        action_object = Action(**action)
        actions.append(action_object)
    return actions


def buy_actions():
    """
    Buys random actions without exceeding the budget
    :return: A list of actions.
    """
    actions = create_actions_objects()
    budget = 500
    wallet = []
    while actions and budget > 0:
        action = random.choice(actions)
        actions.remove(action)
        if action.price < budget:
            budget -= action.price
            wallet.append(action)
    print(wallet)
    print(budget)
    return wallet


def calculate_wallet_profit(wallet):
    profit = 0
    for action in wallet:
        profit += action.calculate_profit()
    return wallet, round(profit, 2)


def get_all_hypothesis():
    hypothesis_dict = {}
    while len(hypothesis_dict) < 1726:  # 1726 = all possible hypothesis
        hypothesis = calculate_wallet_profit(buy_actions())
        hypothesis_dict.setdefault(hypothesis[1], hypothesis[0])
    profit = sorted(hypothesis_dict.items(), reverse=True)[0][0]
    actions = sorted(hypothesis_dict.items(), reverse=True)[0][1]

    best_hypothesis = [profit, actions]

    print(f"Best option : {profit} -> {actions}")
    return best_hypothesis


get_all_hypothesis()
