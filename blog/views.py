from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #here we can make changes like re order the blog based on date or sorting using 'order_by(-date_) [:5] etc..'
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog} )
