# coding:utf-8
from django import template

register = template.Library()

@register.inclusion_tag("category_tree_part.html")
def category_tree(cate):
    return {
        'cates': cate.cates.all()
    }
