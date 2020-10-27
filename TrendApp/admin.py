from django.contrib import admin
from .models import Categories
from .models import Image

# Register your models here.
admin.site.register(Categories)
admin.site.register(Image)
