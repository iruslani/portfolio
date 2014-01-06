from django.conf.urls import patterns, include, url
from portfolio.views import hello, home, template, current_datetime, hours_ahead, display_meta, search
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^hello/$', hello),    
    url(r'^template/$', template),
    url(r'^datetime/$', current_datetime),
    url(r'^datetime/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display-meta/$', display_meta),
    url(r'search/$', search),
    url(r'^admin/', include(admin.site.urls)),
)
