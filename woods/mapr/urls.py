from django.conf.urls.defaults import patterns, url

from .views import IndexView

VIEW_PREFIX = 'woods.mapr.views'

urlpatterns = patterns(VIEW_PREFIX,
    url(r'^$', IndexView.as_view(), name='index'),
)
