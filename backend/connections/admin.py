from django.contrib import admin
from .models import User, Profile, Experience, Education, Post, Comment

# Register your models here.


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(Like)
