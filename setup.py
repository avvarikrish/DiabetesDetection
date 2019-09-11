import pandas as pd
from sklearn.model_selection import train_test_split

FILE_NAME = "diabetes.csv"
LAST_ROW = "Outcome"

def setup_data():
    dataset = pd.read_csv(FILE_NAME)
    X = dataset.drop(LAST_ROW, axis = 1)
    y = dataset[LAST_ROW]
    total = train_test_split(X, y, test_size=0.2)
    # print(total[2].to_dict())
    # print(total[0].to_dict())
    return total[0], total[1], total[2], total[3]
    # return convert_to_dictlist(total[0].to_dict()), convert_to_dictlist(total[1].to_dict()), convert_to_list(total[2].to_dict()), convert_to_list(total[3].to_dict())

def convert_to_dictlist(data):
    return {key : [v for k, v in value.items()] for key, value in data.items()}

def convert_to_list(data):
    return [v for k, v in data.items()]



setup_data()