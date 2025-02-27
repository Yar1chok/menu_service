from dto import ProductDTOandMenuDTO


class DataStorage:
    def __init__(self):
        self.data = None

    def save_data(self, data):
        self.data = data

    def get_data(self) -> ProductDTOandMenuDTO:
        return self.data
