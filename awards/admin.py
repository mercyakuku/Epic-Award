from django.contrib import admin
from .models import Collection,Comment,CommentsLikes,Location,PostLikes,Profile,Post,Rating,Followers,Tags,Technologies
# Register your models here.

admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Followers)
admin.site.register(Tags)
admin.site.register(Technologies)
admin.site.register(Comment)
admin.site.register(Collection)
admin.site.register(PostLikes)
admin.site.register(CommentsLikes)


