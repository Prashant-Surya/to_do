from django.conf.urls import url, patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'to_do.views.home', name='home'),
    url(r'^lists/', 'to_do.views.lists', name='lists'),
    url(r'^AJAX/save-new-form/', 'to_do.ajax_views.save_new_form',
        name='save_new_form'),
    url(r'^AJAX/update-task/', 'to_do.ajax_views.update_task',
        name='update_task'),
    url(r'^AJAX/delete-task/', 'to_do.ajax_views.delete_task',
        name='delete_task'),
    # url(r'^to_do/', include('to_do.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
