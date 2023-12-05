from django.contrib import admin

# Register your models here.

from .models import Client, Payment, Clients_feedback,Clients_compaints,Clients_preference,Clients_General_notes

admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Clients_feedback)
admin.site.register(Clients_compaints)
admin.site.register(Clients_preference)
admin.site.register(Clients_General_notes)

