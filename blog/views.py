from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm
def index(request):
    posts = PostModel.objects.all()
    form = PostModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
        else:
            form = PostModelForm(required = False)
    context = {
        'posts' : posts,
        'form' : form
    }
    return render(request,'blog/index.html',context)

# Create your views here.
