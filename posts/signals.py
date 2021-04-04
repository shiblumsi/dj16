# from django.db.models.signals import post_save
#
# from .models import Post
#
#
# def customer_profile(sender,instance,created,**kwargs):
#     if created:
#
#
#         Post.objects.create(
#             author = instance
#
#         )
#
# post_save.connect(customer_profile,sender=Post)