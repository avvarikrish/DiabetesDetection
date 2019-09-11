from math import log

def entropy(list_of_outcomes):
    final_entropy = 0.0;
    set_of_values = set(list_of_outcomes)
    total_length = len(list_of_outcomes)
    for value in set_of_values:
        prob = list_of_outcomes.count(value)/total_length
        final_entropy += prob/total_length*log(prob , 2)
    return final_entropy*-1.0

def children_weighted_average(children_data: [str], outcome_data: [int]):
    cwa = 0.0;
    children_data_set = set(children_data)
    for child in children_data_set:
        outcome_data_set = [k for j, k in enumerate(outcome_data) if children_data[j] == child]
        data_entropy = entropy(outcome_data_set)
        cwa += (children_data.count(child)/len(children_data))*data_entropy
    return cwa

