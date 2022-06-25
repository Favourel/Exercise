from django.core.paginator import Paginator


posts = ["hello", "world", "programming",
         "language", "python", "c++",
         "language", "python", "c++",
         "language", "python", "c++",
         "language", "python", "c++",
         "language", "python", "c++",
         "language", "python", "c++",
         "language", "python", "c++",
         ]

paginator = Paginator(posts, 3)

while True:
    input_number = input("Enter page(int) request: ")
    try:
        val = int(input_number)

        posts = paginator.get_page(val)
        if posts.has_other_pages():
            if posts.has_previous():
                print(f"First Page: {posts.paginator.get_page(1).object_list}")
                print(f"Previous page: {posts.previous_page_number()}")
            for num in posts.paginator.page_range:
                if posts.number == num:
                    print(f"Current page: {num}")
                elif int(posts.number - 3) < num < int(posts.number + 3):
                    print(num)
            if posts.has_next():
                print(f"Next page: {posts.next_page_number()}")
                print(f"Last page: {posts.paginator.num_pages}")
        break
    except ValueError:
        try:
            val = float(input_number)
            print("Error! Value is a float number.")
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")
