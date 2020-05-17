from django.contrib import admin
from .models import Item, Image, Category, Review, CategoryImage


class PostImageInline(admin.StackedInline):
    '''
    InLine  admin
    '''
    model = Image
    max_num = 15
    extra = 0

class PostImageCategoryInline(admin.StackedInline):
    '''
    InLine  admin
    '''
    model = CategoryImage
    max_num = 15
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    '''
    Admin table for 'blog' posts
    '''
    # prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageInline]
    # formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class CategoryAdmin(admin.ModelAdmin):
    '''
    Admin table for 'blog' posts
    '''
    # prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageCategoryInline]
    # formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}



# # Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(CategoryImage)