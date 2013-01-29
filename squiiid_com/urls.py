from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^image/(?P<image_id>\d+)/$', 'squiiid.views.image', name='image'),
    url(r'^$', 'squiiid.views.index', name='index'),
    # url(r'^squiiid_com/', include('squiiid_com.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
