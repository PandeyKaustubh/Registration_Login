from django.conf.urls import url
from .views import myfunc

urlpatterns = [
    url(r'^$', myfunc)
    
]



