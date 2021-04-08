from django.views import generic
from .models import Post
from .forms import PostForm
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def dodajpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #zwraca słownik
            title = cd.get("title")
            slug = cd.get("slug")
            author = cd.get("author")
            updated_on = cd.get("updated_on")
            content = cd.get("content")
            created_on = cd.get("created_on")
            status = cd.get("status")
            Post.objects.create(title=title, slug=slug, author=author, updated_on=updated_on, content=content, created_on=created_on, status=status)
    form = PostForm()
    return render(request, 'add_post.html', {'form':form})
