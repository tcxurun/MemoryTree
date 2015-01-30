# coding:utf-8
from django.db import models
from django.utils.translation import ugettext as _
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    """文章分类"""
    title = models.CharField(u"名称", max_length = 100)     # 分类名称
    slug = models.SlugField(u"URL", max_length = 100, db_index = True)  # 分类别名(用于url 优化)
    sort = models.SmallIntegerField(u"排序")    # 排序
    parent = TreeForeignKey('self', related_name='children', null = True, blank = True)

    def as_tree(self):
        children = list(self.children.all())
        branch = bool(children)
        yield branch, self
        for child in children:
            for next in child.as_tree():
                yield next
        yield branch, None

    class MPTTMeta:
        parent_attr = 'parent'
        order_insertion_by = ['title']

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"
        ordering = ['sort']

    def __unicode__(self):
        return self.title

class Post(models.Model):
    '''文章'''
    title = models.CharField(u"标题", max_length=60)
    categories = models.ManyToManyField(Category, blank = True, null = True, verbose_name = u"分类", related_name = "categories")
    content = models.TextField(
        verbose_name = _(u'内容'),
        help_text = _(u' ')
        )

    publish_date = models.DateTimeField(u"发表时间")
    slug = models.SlugField(
        verbose_name = _(u'URL'),
        help_text = _(u'URL'),
        max_length = 255,
        unique = True
        )

    class Meta:
        app_label = _(u'wiki')
        verbose_name = _(u'文章')
        verbose_name_plural = u"文章"
        ordering = ['-publish_date', ]

    def __unicode__(self):
        return "%s" % (self.title, )
