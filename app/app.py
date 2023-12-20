import pickle


class App:
    def __init__(self, value=0):
        self.value = value
        self.data = [
            [0, "John", "Doe"],
            [1, "Jane", "Doe"],
            [2, "John", "Smith"],
            [3, "Jane", "Smith"],
            [4, "John", "Wayne"],
            [5, "Jane", "Wayne"],
        ]

    @staticmethod
    def load(path: str):
        with open(path, "rb") as f:
            data = pickle.load(f)
            print(data)
            return App(data["value"])

    def save(self, path: str):
        with open(path, "wb") as f:
            print(self.value)
            pickle.dump({"value": self.value}, f)