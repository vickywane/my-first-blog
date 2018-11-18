from django.contrib import admin
from .models import Post 
from .models import  Event 



#admin control
# Changing The Admin Page
admin.site.site_title = 'Page Administration'
admin.site.site_header = 'Patfin Admin Page'

#registering models
admin.site.register(Post)
admin.site.register(Event)
