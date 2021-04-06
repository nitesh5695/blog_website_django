from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView,newpost

admin.site.register(Author)
admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','author','overview','content']
admin.site.register(Post,PostAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','user','timestamp','content','post']
admin.site.register(Comment,CommentAdmin)
class ViewsAdmin(admin.ModelAdmin):
    list_display=['id','user','post']
admin.site.register(PostView,ViewsAdmin)
# class newPostAdmin(admin.ModelAdmin):
#     list_display=['id','titles','slug','overview']
# admin.site.register(newpost,newPostAdmin)