# coding:utf-8
from django.contrib import admin
from wiki.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'publish_date')  # 列表显示的字段
    search_fields = ('title', 'content')  # 列表包含根据指定字段搜索
    list_filter = ('categories', )  # 右侧过滤选项
    fieldsets = (
        (u"基本信息",
            {
                'fields': ('title', 'slug', 'publish_date', 'content', 'categories')
            }),
        ('Meta Data',
            {
                'fields': ('slug')
            }),
    )

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
