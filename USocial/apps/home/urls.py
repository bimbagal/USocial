from django.conf.urls import patterns, include, url

urlpatterns = patterns('USocial.apps.home.views',
	url(r'^','index_view', name='vista_inicial'),
	)