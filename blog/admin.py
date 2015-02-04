# coding:utf-8
from django.contrib import admin
from blog.models import Article, Category
from django.db import models
from ckeditor.widgets import CKEditorWidget


class ArticleAdmin(admin.ModelAdmin):
    content = {
        models.TextField: {'widget': CKEditorWidget},
    }

    list_display = ('title', 'publish_date', 'status')  # 列表显示的字段
    search_fields = ('title', )  # 列表包含根据指定字段搜索
    list_filter = ('publish_date', )  # 右侧过滤选项
    fieldsets = (
        (u"基本信息",
            {
                'fields': ('title', 'content', 'publish_date', 'status', 'categories')
            }),
        ('Meta Data',
            {
                'fields': ('alias', 'keywords', 'description')
            }),
    )

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

