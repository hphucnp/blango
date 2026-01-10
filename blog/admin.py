from django.contrib import admin

from blog.models import Tag, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ("modified_at", "slug")

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
