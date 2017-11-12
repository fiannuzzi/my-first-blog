from django.conf.urls import url
from . import views

urlpatterns = [
    # Note we are NAMING the URL pattern
    # This is useful if you want to refer to this URL elsewhere in the code
    url(r'^$', views.post_list, name='post_list'),
]
