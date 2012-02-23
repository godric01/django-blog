
from django.contrib import admin
from tea.models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name','topic_publisher','topic_email','topic_created','topic_order')    
    search_fields = ['topic_publisher']

admin.site.register(Topic,TopicAdmin)
        
