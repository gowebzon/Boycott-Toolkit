from django.conf.urls.defaults import patterns

urlpatterns = patterns('geography.views',
    (r'(?P<slug>[\w-]+)$','location_by_name'),
    (r'map/$','map'),
)