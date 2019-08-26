from django.contrib import admin
from django.conf.urls import url , include
from Details import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^Play/',include ('Play.urls')),
    url(r'^data/', include('Details.urls'))

]  

