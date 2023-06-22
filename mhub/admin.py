from django.contrib import admin

# Register your models here.
from .models import Contact,Roadmap,Text,TimeLeft,SmartContract

admin.site.register(Contact)
admin.site.register(Roadmap)
admin.site.register(Text)
admin.site.register(TimeLeft)
admin.site.register(SmartContract)