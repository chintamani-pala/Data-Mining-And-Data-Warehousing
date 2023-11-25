from collections import defaultdict
transactions = [
    ['M', 'O', 'N', 'K', 'E', 'Y'],
    ['D', 'O', 'N', 'K', 'E', 'Y'],
    ['M', 'A', 'K', 'E'],
    ['M', 'U', 'C', 'K', 'Y'],
    ['C', 'O', 'O', 'K', 'I', 'E']
]

#finding frequent items
min_support = 3

item_counts = defaultdict(int)
for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1

frequent_1_itemsets = {item: count for item, count in item_counts.items() if count >= min_support}

frequent_itemsets = [list(frequent_1_itemsets.keys())]

k = 2  # Start with 2-itemsets
while True:
    candidate_itemsets = []
    for i in range(len(frequent_itemsets[-1])):
        for j in range(i + 1, len(frequent_itemsets[-1])):
            itemset1 = frequent_itemsets[-1][i]
            itemset2 = frequent_itemsets[-1][j]
            candidate = sorted(list(set(itemset1) | set(itemset2)))
            if len(candidate) == k and candidate not in candidate_itemsets:
                candidate_itemsets.append(candidate)

    
    candidate_counts = defaultdict(int)
    for transaction in transactions:
        for candidate in candidate_itemsets:
            if set(candidate).issubset(set(transaction)):
                candidate_counts[tuple(candidate)] += 1

    
    frequent_k_itemsets = [list(candidate) for candidate, count in candidate_counts.items() if count >= min_support]

    if not frequent_k_itemsets:
        break

    frequent_itemsets.append(frequent_k_itemsets)
    k += 1
frequent_itemsets=frequent_itemsets[len(frequent_itemsets)-1]

#finding association rules
import itertools
def generate_association_rules(frequent_itemsets, min_confidence):
    association_rules = []
    
    for itemset in frequent_itemsets:
        if len(itemset) >= 2:
           
            for i in range(1, len(itemset)):
                antecedent_combinations = itertools.combinations(itemset, i)
                for antecedent in antecedent_combinations:
                    consequent = tuple(item for item in itemset if item not in antecedent)
                    
                    itemset_support = sum(1 for transaction in transactions if set(itemset).issubset(set(transaction)))
                    
                    antecedent_support = sum(1 for transaction in transactions if set(antecedent).issubset(set(transaction)))
                    
                    confidence = itemset_support / antecedent_support if antecedent_support != 0 else 0
                    
                    if confidence >= min_confidence:
                        association_rules.append((antecedent, consequent, confidence))
    
    return association_rules

association_rules = generate_association_rules(frequent_itemsets, 0.8)
print("\nStrong Association Rules:")
for rule in association_rules:
    antecedent = ", ".join(rule[0])
    consequent = ", ".join(rule[1])
    confidence = rule[2]
    print(f"Rule: ({antecedent}) => ({consequent}), Confidence: {confidence:.2f}")
