import os
import csv
from model import Action
import itertools
from decorator import perfs_decorator


def create_actions_objects():
    """
    Create action objects from a json file.
    :return: Actions objects.
    """
    database_path = os.path.join(os.path.dirname(__file__),
                                 'datas', 'actions.csv')  # actions.csv / memtest.csv / dataset1.csv / dataset2.csv
    with open(database_path, 'r') as csv_file:
        data = csv.reader(csv_file, delimiter=",")

        actions = []

        for action in data:
            action_object = Action(name=action[0],
                                   price=int(float(action[1])),
                                   benefit=int(float(action[2])))
            if action_object.price > 0:
                actions.append(action_object)
    csv_file.close()
    return actions


def get_all_combinations():
    """
    Browse every combination possible of actions, regardless of their prices.
    :return: A list of all combination possible.
    """
    actions = create_actions_objects()
    combinations = []
    for L in range(len(actions)):
        for i in itertools.combinations(actions, L):
            combinations.append(i)
    print('Toutes les combinaisons possibles ont été stockées')
    return combinations


def custom_itertools_combinations(iterable, r):  # Detailed itertools.combinations
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


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


@perfs_decorator
def run_program():
    """
    Run the program and watches time and hardware use.
    :return: Print out the results of the program.
    """
    get_combinations_values(get_all_combinations(), budget=500)


run_program()  # TODO : Flake-8 sur le projet
