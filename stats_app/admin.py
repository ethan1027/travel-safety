from django.contrib import admin

# Register your models here.
from .models import Gunshot
from .models import State
from .models import City
admin.site.register(Gunshot)
admin.site.register(State)
admin.site.register(City)