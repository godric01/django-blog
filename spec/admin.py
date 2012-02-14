# -*- coding: UTF-8 -*-

from django.contrib import admin
from spec.models import Category, Specification

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_order')
    search_fields = ['category_name']

class SpecAdmin(admin.ModelAdmin):
    list_display = ('spec_name','spec_category','spec_blog_url','spec_order')
    list_filter =('spec_category',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Specification, SpecAdmin)

