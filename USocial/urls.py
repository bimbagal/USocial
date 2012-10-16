from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
	#Se conecta con las url de la aplicacion home para mostrar la pagina inicial
    url(r'^',include('USocial.apps.home.urls')),
    #activar servidor de medios en carpeta media
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
