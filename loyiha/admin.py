from django.contrib import admin
from .models import Category, Event, Team, Participant, Result, User

admin.site.register((Category, Event, Team, Participant, Result, User))
