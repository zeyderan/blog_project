from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy # rediret için kullanılır
from .models import Post

# Create your views here.
# sınıf bazlı view listview ı extend eder
class BlogListWiev(ListView):
    # gönderilecek model
    model = Post

    # gönderilecek template
    template_name = 'home.html'

    # model takma ismi html içerisinde kullanılacak isim
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    # template e gönderilecek veririn ismi
    context_object_name = 'post_detail'

class BlogCreateView(CreateView):
    #gelecek fieldlar bu model içerisidekiler ile eşleşmeli-hepsi olmak zorunda değil
    model = Post

    template_name = 'post_new.html'

    #post modelinin içerisindeki fieldları alır
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    # kullanılacak model
    model = Post
    # kullanılacak template
    template_name = 'post_edit.html'
    # template üzeride kullanılacak fieldlar
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post

    template_name = 'post_delete.html'

    success_url = reverse_lazy('home')

