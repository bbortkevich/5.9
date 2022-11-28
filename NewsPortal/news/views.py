from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView,
    DetailView, ListView,
    UpdateView
)

from .models import Post

from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-date')
    paginate_by = 10


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class SearchPosts(ListView):
    paginate_by = 10
    model = Post
    ordering = 'date'
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_filter'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить новость"
        return context


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать новость"
        return context


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить новость"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context