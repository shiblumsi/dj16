from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .templates import tag



def home(request):
    return render(request,'home.html')


def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form is not None:
            form.save()

            data = Person()
            data.user = form.instance
            data.save()
            
            return redirect('login')
    context = {
        'form':form
    }
    return render(request,'signup.html',context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('posts')
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def posts(request):
    post = Post.objects.all()

    context ={
        'posts':post
    }
    return render(request,'post.html',context)

def create_post(request):

    form = Create_Post()
    if request.method == "POST":
        form = Create_Post(request.POST,request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.author = request.user.person
            obj.save()




        # title = request.POST.get('title')
        # text = request.POST.get('text')
        #
        # data = Post()
        # data.title = title
        # data.text_aria=text
        # data.author = request.user.person
        # data.save()


        # if form.is_valid():
        #     data = Post()
        #     data.author = request.user.person
        #     aa = data.author
        #     aa.save()
        #
        #     form.save()
        return redirect('posts')
    context = {
        "form":form
    }
    return render(request,'create_post.html',context)


def about_me(request):
    posts = request.user.person.post_set.all()
    create_form = Create_Person(instance=request.user.person)
    if request.method == 'POST':
        create_form = Create_Person(request.POST,request.FILES)
        if create_form.is_valid():
            create_form.save()
    context = {
        'posts':posts,
        'create_form':create_form
    }
    return render(request,'about_me.html',context)


def like_post(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)

        if post.like.filter(id= request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





#
# def detail(request,pk):
#     post = get_object_or_404(Post,id=pk)
#     t_like = post.total_like()
#
#
#
#     context = {
#         'post':post,
#         't_like':t_like
#
#     }
#
#     return render(request,'post_detail.html',context)

def like_post(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)

        if post.like.filter(id= request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def add_comment(request,pk):
    if request.method == 'POST':
        comment = request.POST['comment']

        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        comments = Comment(post=post,user=request.user,text=comment)
        comments.save()



    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_reply(request,pk):
    if request.method == "POST":
        reply = request.POST['reply']
        comment_id = request.POST['comment_id']
        comment = Comment.objects.get(id=comment_id)
        replies = Reply(user=request.user,for_comment=comment,reply_text=reply)
        replies.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# class DetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#
#     def get_context_data(self,*args,**kwargs):
#
#         self.object.view.add(self.request.user)
#
#
#         liked =False
#         if  self.object.like.filter(id=self.request.user.id).exists():
#             liked = True
#         context = super().get_context_data(*args,**kwargs)
#         for_comment = context.get('object')
#         comment = Comment.objects.filter(post=post.id)
#
#         replies = Reply.objects.filter(for_comment=for_comment.id)
#
#
#         context['post'] = context.get('object')
#         context['liked'] = liked
#         context['comment'] = comment
#         context['replies'] = replies
#
#
#         return context


def detail(request,pk):
    post = get_object_or_404(Post,id=pk)
    post.view.add(request.user)

    liked = False
    if post.like.filter(id=request.user.id).exists():
        liked = True

    comments = Comment.objects.filter(post=post)







    context = {
        'post':post,
        'liked':liked,
        'comments':comments,


    }

    return render(request,'post_detail.html',context)