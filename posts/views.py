from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView , CreateView
from posts.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def PostList(request):
    posts = Post.objects.all()

    context = {
        'objects': posts
    }

    return render(request, 'posts/post_list.html', context)
    
class PostCreate(CreateView):
    model = Post

    fields = ['title','content','Hashtags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def PostDetail(request, title):
    post = get_object_or_404(Post, title = title)

    context = {
        'object': post
    }

    return render(request, 'posts/post_detail.html', context)

@login_required
def BlogPostLike(request, title):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('postdetail', args=[str(title)]))