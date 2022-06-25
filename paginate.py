class Paginate:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if self.item_count() % self.items_per_page == 0:
            return self.item_count() / self.items_per_page
        else:
            return self.item_count() // self.items_per_page + 1

    def pass_item_count(self, page_index):
        if page_index >= self.page_count():
            return - 1
        elif page_index == self.page_count() - 1:
            return self.item_count() - self.items_per_page * page_index
        else:
            return self.items_per_page

    def page_index(self, item_index):
        if item_index in range(self.item_count()):
            return item_index // self.items_per_page
        else:
            return - 1


list = Paginate(["hello", "world", "programming",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 "language", "python", "c++",
                 ], 3)
