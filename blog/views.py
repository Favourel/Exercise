from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("-id")

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    posts = paginator.get_page(page_number)
    if posts.has_other_pages():
        if posts.has_previous():
            print(f"First Page: {posts.paginator.get_page(1)}")
            print(f"Previous page: {posts.previous_page_number()}")
        for num in posts.paginator.page_range:
            if posts.number == num:
                print(num)
            elif int(posts.number - 3) < num < int(posts.number + 3):
                print(num)
        if posts.has_next():
            print(f"Next page: {posts.next_page_number()}")
            print(f"Last page: {posts.paginator.num_pages}")

    return render(request, "blog/index.html", {"posts": posts})
