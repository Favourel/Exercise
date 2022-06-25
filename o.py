data = [
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": False
    },
    {
        "userId": 1,
        "id": 5,
        "title": "laborio provident illum",
        "completed": False
    },
    {
        "userId": 1,
        "id": 6,
        "title": "laboipisci quia provident illum",
        "completed": False
    },

    {
        "userId": 1,
        "id": 7,
        "title": "illum",
        "completed": False
    },

]

step = 2
hashmap = {}
for i in range(len(data)):
    if i == 0:
        hashmap[i] = data[0:step]
    else:
        startIndex = step * i
        EndIndex = ((i + 1) * step)
        sample = data[startIndex:EndIndex]
        hashmap[i] = sample

print(hashmap[2])


def paginator(objects, total_pages):
    total_objects = len(objects)
    if 0 < total_pages < total_objects:
        obj_per_page = total_objects // total_pages
        reminder_objects = total_objects - (obj_per_page * total_pages)
        first_page = True
        i = 0
        page_number = 1
        while total_objects > 0:
            current_page_total_objects = obj_per_page
            if first_page and reminder_objects > 0:
                current_page_total_objects = obj_per_page + reminder_objects
            print(f'this is page {page_number} have object {objects[i:i + current_page_total_objects]}')
            page_number += 1
            first_page = False
            i += current_page_total_objects
            total_objects -= current_page_total_objects
    elif total_objects <= total_pages:
        for i in objects:
            print(f'this is page {i} have object [{i}]')
    else:
        print(objects)


ar = [1, 2, 3, 4, 5]
page_number = 2
paginator(ar, page_number)
