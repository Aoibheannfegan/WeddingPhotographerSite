from django.contrib import admin
from .models import User, Client, Calendar, Note, Package

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Calendar)
admin.site.register(Note)
admin.site.register(Package)


