class Feature:
    def __init__(self, name, thresholds, data, outcomes):
        self._name = name
        self._thresholds = thresholds
        self._data = data
        self._outcomes = outcomes

    def name(self):
        return self._name

    def thresholds(self):
        return self._thresholds

    def data(self):
        return self._data

    def outcomes(self):
        return self._outcomes