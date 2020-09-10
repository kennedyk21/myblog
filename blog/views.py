from django.shortcuts import render, get_object_or_404
from django.template import context, loader
from blog.models import Post, Comment
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import SuggestionForm, CommentForm
from . import forms
# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 3)
    try: list_page = request.GET.get("list_page",'1')
    except ValueError: list_page = 1
    post_list = paginator.page(list_page)
    context={
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)
def post_page(request, post_id):
    post_page = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post_page)
    form = forms.CommentForm(request.POST)
    return render(request, 'blog/post.html', {'post_page': post_page, 'comments':comments,'form': form})
def suggestion_view(request):
    form = SuggestionForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['kennedykm31@gmail.com']
        if cc_myself:
            recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/')        
    return render(request, 'blog/suggestion.html',{'form': form})
def comments(request, post_id):
    comment = get_object_or_404(models.Post, pk=post_id)
    form = forms.CommentForm()
    if request.method == 'POST':
        forms = forms.CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit = False)
            com.comment = comment
            com.save()
            return HttpResponseRedirect(Post.get_absolute_url())
    return render(request,'blog/comment.html',{'form': form})


def add_comment(request, comment_id):
    form = forms.CommentForm()
    if request.method == 'POST':
        print('okay')
        forms = forms.CommentForm(request.POST)
        if form.is_valid():
            print('good')
            a = Comment.objects.get(pk=comment_id)
            f = CommentForm(request.POST, instance=a)
            f.save()
    print('bad')
    return HttpResponseRedirect(reverse('blog:post',args=[comment_id]))


