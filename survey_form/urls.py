from django.conf.urls import url
from .views import user_data

urlpatterns = [
    url(r'^$', user_data)
    
]