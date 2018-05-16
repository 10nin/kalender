# coding=utf-8
from main.query import Query


class Controller:
    def __init__(self):
        self.db = Query(db_path="")

    def call_get_all_groups(self):
        return self.db.get_all_groups()


if __name__ == "__main__":
    c = Controller()
    print(c.call_get_all_groups())