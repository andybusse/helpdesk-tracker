from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tracker/', include('tracker.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^viewissue/(\d+)$', 'tracker.track.views.view_issue'),
    (r'^$', 'tracker.track.views.list_open_issues'),
    (r'^updateissue$', 'tracker.track.views.update_issue'),
    (r'^createissue$', 'tracker.track.views.create_issue'),
    (r'^createissueform$', 'tracker.track.views.create_issue_echoer'),
    (r'^allissues$', 'tracker.track.views.allissues'),
    (r'^issuejson/(\d+)/$', 'tracker.track.views.get_issue_json'),
)
