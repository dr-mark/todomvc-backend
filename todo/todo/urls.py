from django.conf.urls import patterns, include, url
from tasks.api import TaskResource

from django.contrib import admin
admin.autodiscover()

task_resource = TaskResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(task_resource.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
