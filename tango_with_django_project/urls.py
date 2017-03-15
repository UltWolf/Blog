


from django.conf.urls import url
from django.contrib import admin
from rango import urls
from django.conf.urls import include
from tango_with_django_project import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import registration.backends.simple.urls
from registration.backends.simple.views import RegistrationView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rango/', include(urls)),
    url(r'^accounts/', include(registration.backends.simple.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()