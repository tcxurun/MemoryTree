# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    """文章分类"""
    title = models.CharField(u"名称", max_length = 100)     # 分类名称
    alias = models.CharField(u"别名", max_length = 100)  # 分类别名(用于url 优化)
    sort = models.SmallIntegerField(u"排序")    # 排序

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"
        ordering = ['sort']

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    """文章标签"""
    tagname = models.CharField(u"标签名", max_length = 60)  # 标签名
    post_ids = models.TextField(editable = False)  # 对应的文章id集合的序列

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = u"标签"

    def __unicode__(self):
        return self.tagname

class Article(models.Model):
    """文章"""
    # 文章发布状态
    CONTENT_STATUS_PUBLISHED = 1
    # 文章草稿箱状态
    CONTENT_STATUS_DRAFT = 2
    # 文章状态选项
    CONTENT_STATUS_CHOICES = (
        (CONTENT_STATUS_PUBLISHED, u"发布"),
        (CONTENT_STATUS_DRAFT, u"草稿箱"),
        )

    categories = models.ManyToManyField(Category, blank = True, verbose_name = u"分类", related_name = "categories")
    title = models.CharField(u"标题", max_length = 100)
    content = RichTextField(u"文章内容")
    publish_date = models.DateTimeField(u"发表时间")
    status = models.IntegerField(u"状态", choices=CONTENT_STATUS_CHOICES, default = CONTENT_STATUS_PUBLISHED)
    comments_count = models.IntegerField(default = 0, editable = False)
    view_count = models.IntegerField(default = 0, editable = False)

    alias = models.CharField(u"别名", max_length=100, blank = True)
    keywords = models.CharField(u"关键字", max_length = 500, blank = True)
    description = models.TextField(u"描述", blank = True)


    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = u"文章"
        ordering = ['publish_date']

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
        return self.title
