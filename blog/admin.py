from django.contrib import admin
from .models import Gallery, Timeline, About, ContactInfo


admin.site.register(Gallery)
admin.site.register(Timeline)
admin.site.register(About)
admin.site.register(ContactInfo)