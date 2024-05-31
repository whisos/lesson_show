from django.shortcuts import render, redirect, get_object_or_404
from forum.models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from forum.forms import PostAdd, CommentForm, ThemeAdd
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.mixins import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy


class Forum_Themes_View(ListView):
    model = Forum_Theme
    context_object_name = "themes"
    template_name = "forum/themes_list.html"
    paginate_by = 5
    

class Posts_View(LoginRequiredMixin, ListView):
    model = Forum_post
    template_name = "forum/posts_list.html"
    context_object_name = "post"
    paginate_by = 4
    
    def get_queryset(self):
        theme_pk = self.kwargs.get('pk')
        theme = get_object_or_404(Forum_Theme, pk=theme_pk)
        posts = Forum_post.objects.filter(theme=theme)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme'] = get_object_or_404(Forum_Theme, pk=self.kwargs.get('pk'))
        return context

class Post_Detail_View(LoginRequiredMixin, DetailView):
    model = Forum_post
    template_name = "forum/post_detail.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = self.get_object()
            comment.save()
            return redirect('forum:post_detail', pk=comment.post.pk)

class CommentLikeToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comment.objects.get(pk=comment_id)
        user = request.user
        like, created = Like.objects.get_or_create(comment=comment, user=user)
        if not created:
           
            like.delete()

       
        return redirect('forum:post_detail', pk=comment.post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["comments"] = Comment.objects.filter(post=self.get_object())
        return context

class ThemeAddView(LoginRequiredMixin, CreateView):
    model = Forum_Theme
    template_name = "forum/theme_add.html"
    form_class = ThemeAdd
    success_url = reverse_lazy("themes_list")

class ThemeUpdateView(LoginRequiredMixin, UpdateView):
    model = Forum_Theme
    template_name = "forum/theme_update.html"
    form_class = ThemeAdd
    success_url = reverse_lazy("themes_list")

class PostAddView(LoginRequiredMixin, CreateView):
    model = Forum_post
    template_name = "forum/post_add.html"
    form_class = PostAdd
    success_url = reverse_lazy("themes_list")

    def get_initial(self):
        initial = super().get_initial()
        theme_pk = self.request.GET.get('theme')
        initial['theme'] = get_object_or_404(Forum_Theme, pk=theme_pk)
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum:posts_list', kwargs={'pk': self.object.theme.pk})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Forum_post
    template_name = "forum/post_update.html"
    form_class = PostAdd
    success_url = reverse_lazy("themes_list")

class PostDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Forum_post
    template_name = "forum/post_delete.html"
    success_url = reverse_lazy("themes_list")

class CommentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/comment_add.html"
    form_class = CommentForm
    success_url = reverse_lazy("themes_list")
