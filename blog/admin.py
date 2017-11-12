from django.contrib import admin

# Register your models here.
# . is for relative import (for files within the module)
from .models import Post

admin.site.register(Post)
