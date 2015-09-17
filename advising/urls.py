from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from advising import views

urlpatterns = [
    url(r'^$', views.api_root),

    url(r'^advisors/$',
        views.AdvisorList.as_view(),
        name='advisor-list'),
    url(r'^advisors/(?P<username>[a-zA-Z ]*)/$',
        views.AdvisorDetail.as_view(),
        name='advisor-detail'),
    url(r'^advisors/(?P<username>[a-zA-Z ]*)/students/$',
        views.AdvisorStudentsList.as_view(),
        name='advisor-students-list'),

    url(r'^students/$',
        views.StudentList.as_view(),
        name='student-list'),
    url(r'^students/(?P<username>[a-zA-Z ]*)/$',
        views.StudentDetail.as_view(),
        name='student-detail'),
    url(r'^students/(?P<username>[a-zA-Z ]*)/advisors/$',
        views.StudentAdvisorsList.as_view(),
        name='student-advisors-list'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)