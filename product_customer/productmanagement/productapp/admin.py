from django.contrib import admin

from productapp.models import Comment, Post, Products


# Register your models here.


# admin.site.register(Products)

# admin.site.register(Post)


                #   Customizing the model display

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','content','published_date')

# admin.site.register(Post,PostAdmin)



            #  Adding Search and Filters:-

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','content','published_date')
#     search_fields = ('title',)
#     list_filter = ('published_date',)

# admin.site.register(Post,PostAdmin)


                # comment

class CommentInLine(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Post,PostAdmin)


