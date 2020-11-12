from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    nombre = "Nelson"
    contexto ={'posts': posts,
                'nombre': nombre}
    return render(request, 'blog/post_list.html', contexto)


# Create your views here.
def blog(request):
    lista= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    nombre_carrera= request.GET.get('titulo_post')
 
    if 'btn-titulo-post' in request.GET:
        if nombre_carrera:
            lista= Post.objects.filter(title__icontains=nombre_carrera)

    data = {
        'posts': lista
    }
    return render(request, 'blog/post_list_ext.html', data)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, "blog/post_edit.html", {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def borrar_post(request, pk):
    instancia = Post.objects.get(pk=pk)
    instancia.delete()
    return redirect('post_list_ext')