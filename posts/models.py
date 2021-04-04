from django.db import models
from django.contrib.auth.models import User
class Person(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )


    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)
    relagion = models.CharField(max_length=20,null=True)
    blood = models.CharField(max_length=10,null=True)
    profile_pic = models.ImageField(default='download.png',null=True)


    def __str__(self):
        return str(self.user)





class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Person,null=True,on_delete=models.CASCADE)
    text_aria = models.CharField(max_length=500,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(null=True,blank=True)
    like = models.ManyToManyField(User,related_name='like_post')
    view = models.ManyToManyField(User,related_name='view_post')




    def __str__(self):
        return str(self.title)

    def total_like(self):
        return self.like.count()

    def total_view(self):
        return self.view.count()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    r_text = models.ForeignKey('self',null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username + ": " + self.text[0:10]


class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    for_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply_text = models.TextField()
    replayed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.for_comment.text[0:10] + ": "+ self.reply_text[0:10]



