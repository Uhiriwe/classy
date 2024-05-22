from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

   path("",views.index, name="index"),
   path("new_design/",views.new_design, name="new_fashion"),
   path("talk_to_us/",views.talk_to_us, name="talk_to_us"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
             