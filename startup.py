from setup import setup_data
from calculations import entropy, children_weighted_average
from collections import defaultdict
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from feature import Feature

X_train, X_test, y_train, y_test = setup_data()

PARENT_ENTROPY = entropy(y_train)

THRESHOLDS = {"Pregnancies": [6], "Glucose": [180], "BloodPressure": [80], "SkinThickness": [30], "Insulin": [200, 400], "BMI": [18.5, 25, 30], "DiabetesPedigreeFunction": [1], "Age": [40]}

def information_gain(cwa):
    return PARENT_ENTROPY - cwa


def compare_info_gain(data_dict, outcome_dict):
    return sorted((data_dict), key=lambda x: -information_gain(children_weighted_average(data_dict[x], outcome_dict)))

"loop through the different {feature: features_data}, get the highest info_gain, and place the results in a tree?"


def match(threshold, data):
    true = []
    false = []
    for value in data:
        if value >= threshold:
            true.append(value)
        else:
            false.append(value)
    return true, false


# def myclassifier():



def skclassifier():
    clf = DecisionTreeClassifier(min_samples_split=40)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(accuracy_score(y_pred, y_test))


def check_data():
    print(X_train)


if __name__ == '__main__':
    # print(X_test)
    skclassifier()
#     check_data()
#     print(len(X_train))
#     myclassifier()