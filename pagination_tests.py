import unittest
from django.core.paginator import Paginator as Pagination

values = ["hello", "world", "programming",
          "language", "python", "c++",
          "language", "python", "c++",
          "language", "python", "c++",
          "language", "python", "c++",
          "language", "python", "c++",
          "language", "python", "c++",
          "language", "python", "c++",
          ]
paginator = Pagination(values, 3)
values = paginator.get_page(3)


class PaginationTest(unittest.TestCase):

    def setUp(self) -> None:
        global values
        p = Pagination(values, per_page=5)
        p.current_page = 2
        self.assertEqual(5, 5)
        p.current_page = 3
        self.assertEqual(10, 10)

    def testPaginationNoRounding(self):
        global values

        values = paginator.get_page(3)
        self.assertEqual(8, values.paginator.num_pages)
        for num in values.paginator.page_range:
            if values.number == num:
                self.assertEqual(3, num)
        self.assertEqual(4, values.next_page_number())

    def testCurrentAndNextAndPrevPage(self):

        global values
        p = Pagination(values, per_page=5)
        for num in values.paginator.page_range:
            if values.number == num:
                self.assertEqual(3, num)
        self.assertEqual(4, values.next_page_number())
        self.assertEqual(2, values.previous_page_number())
        p.current_page = 2
        i = paginator.get_page(2)
        for num in i.paginator.page_range:
            if i.number == num:
                self.assertEqual(2, num)
                self.assertEqual(3, i.next_page_number())
                self.assertEqual(1, i.previous_page_number())
        p.current_page = 3
        self.assertEqual(4, values.next_page_number())
        self.assertEqual(2, values.previous_page_number())
        self.assertEqual(8, values.paginator.num_pages)


if "__name__" == "__main__":
    unittest.main()
