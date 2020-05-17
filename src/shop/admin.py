from django.contrib import admin
from .models import Item, Image, Category, Review


class PostImageInline(admin.StackedInline):
    '''
    InLine  admin
    '''
    model = Image
    max_num = 15
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    '''
    Admin table for 'blog' posts
    '''
    # prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageInline]
    # formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}



# # Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Image)