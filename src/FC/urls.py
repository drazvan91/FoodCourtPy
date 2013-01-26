from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^login/', 'FC.controllers.account.login'),
        url(r'^logout/', 'FC.controllers.account.logout'),
        url(r'^home/', 'FC.controllers.account.home'),
        url(r'^populate/$', 'FC.controllers.mock.populateDatabase'),

    )
