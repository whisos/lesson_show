from django.shortcuts import render, redirect
from forum.models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
#from forum.forms import TaskAdd, CommentForm, TaskFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.mixins import *


class Forum_Themes_View(ListView):
    model = Forum_Theme
    context_object_name = "tasks"
    template_name = "forum/themes_list.html"
    

class Posts_View(LoginRequiredMixin, ListView):
    model = Forum_post
    template_name = "forum/posts_page.html"
    context_object_name = "post"
    

class Post_Detail_View(LoginRequiredMixin, DetailView):
    model = Forum_post
    template_name = "forum/post_detail.html"
    context_object_name = "post"
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['comment_form'] = CommentForm()  
    #    return context
#
    #def post(self, request, *args, **kwargs):
    #    comment_form = CommentForm(request.POST, request.FILES)
    #    if comment_form.is_valid():
    #        comment = comment_form.save(commit=False)
    #        comment.author = request.user
    #        comment.task = self.get_object()
    #        comment.save()
    #        return redirect('tasktrack:task_detail', pk=comment.task.pk)

class CommentLikeToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comment.objects.get(pk=comment_id)
        user = request.user
        like, created = Like.objects.get_or_create(comment=comment, user=user)
        if not created:
           
            like.delete()

       
        return redirect('tasktrack:task_detail', pk=comment.task.id)

        


    #def get_context_data(self, **kwargs)
    #    context = super().get_context_data(**kwargs)
    #    context ["comments"] = Comment.objects.filter(task=self.get_object())
    #    return context

class PostAddView(LoginRequiredMixin, CreateView):
    model = Forum_post
    template_name = "forum/post_add.html"
    #form_class = TaskAdd
    success_url = "/"

class PostAddView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Forum_post
    template_name = "forum/post_update.html"
    #form_class = TaskAdd
    success_url = "/"

class PostDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Forum_post
    template_name = "forum/post_delete.html"
    success_url = "/"

class CommentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/comment_add.html"
    #form_class = CommentForm
    success_url = "/"