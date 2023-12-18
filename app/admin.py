from django.contrib import admin
from app.models import MyUser
from django.contrib.sessions.models import Session


admin.site.register(MyUser)
admin.site.register(Session)


