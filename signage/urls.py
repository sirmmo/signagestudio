from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
	url(r'^(?P<user>\w)$', 'views.user_panels'),
	url(r'^(?P<user>\w)/(?P<panel>)$', 'views.user_panel'),
)
