# -*- coding: UTF-8 -*-

from django.contrib import admin
from vote.models import Vote, VoteLog, Category

class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_title','vote_approve','vote_disapprove','vote_order')
    search_fields = ['vote_title']


class VoteLogAdmin(admin.ModelAdmin):
    list_display = ('vote','vote_ip','vote_date')
    search_fields = ['vote_ip']
    list_filter =('vote',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_order')
    search_fields = ['category_name']

admin.site.register(Vote, VoteAdmin)
admin.site.register(VoteLog, VoteLogAdmin)
admin.site.register(Category, CategoryAdmin)

