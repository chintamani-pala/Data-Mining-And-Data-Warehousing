import numpy as np
import pandas as pd
import math

# Read the dataset, update the file path as needed
df = pd.read_csv("/content/play_tennis.csv")

# Check the number of rows and columns
print(f'Rows: {df.shape[0]}, Columns: {df.shape[1]}')
print(df.columns)

# Information about the DataFrame
df.info()
df.describe()

def find_entropy(df):
    target = df.keys()[-1]
    entropy = 0
    values = df[target].unique()
    for value in values:
        fraction = df[target].value_counts()[value] / len(df[target])
        entropy += -fraction * np.log2(fraction)
    return entropy

def average_information(df, attribute):
    target = df.keys()[-1]
    target_variables = df[target].unique()
    variables = df[attribute].unique()

    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[target] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            eps = 1e-10
            fraction = num / (den + eps)
            entropy += -fraction * math.log(fraction + eps)

        fraction2 = den / len(df)
        entropy2 += -fraction2 * entropy

    return abs(entropy2)

def find_winner(df):
    IG = []
    for key in df.keys()[:-1]:
        IG.append(find_entropy(df) - average_information(df, key))
    return df.keys()[:-1][np.argmax(IG)]

def get_subtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)

def build_tree(df, tree=None):
    target = df.keys()[-1]
    node = find_winner(df)
    attValue = np.unique(df[node])

    if tree is None:
        tree = {}
        tree[node] = {}

    for value in attValue:
        subtable = get_subtable(df, node, value)
        clValue, counts = np.unique(subtable[target], return_counts=True)

        if len(counts) == 1:
            tree[node][value] = clValue[0]
        else:
            tree[node][value] = build_tree(subtable)

    return tree

# Build the decision tree
tree = build_tree(df)

import pprint
pprint.pprint(tree)￼Enter
