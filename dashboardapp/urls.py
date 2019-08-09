from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^$", DashboardHomeView.as_view(), name="dashboard_home"),
    url(r'^login/$', DashboardLoginView.as_view(), name='login'),
    url(r'^logout/$', DashboardLogoutView.as_view(), name='logout'),
    url(r'^articles/$', ArticleListView.as_view(), name='article_list'),
    url(r'^articles/(?P<pk>\d+)$', ArticleDetailView.as_view(),
        name='article_detail'),
    url(r'^articles/create$', ArticleCreateView.as_view(),
        name='article_create'),
    url(r'^articles/(?P<pk>\d+)/edit$', ArticleUpdateView.as_view(),
        name='article_edit'),
    url(r'^articles/(?P<pk>\d+)/delete$', ArticleDeleteView.as_view(),
        name='article_delete'),
    url(r'^hardware/$', HardwareListView.as_view(), name='hardware_list'),
    url(r'^hardware/create$', HardwareCreateView.as_view(),
        name='hardware_create'),
    url(r'^hardware/(?P<pk>\d+)/edit$', HardwareUpdateView.as_view(),
        name='hardware_edit'),
    url(r'^hardware/(?P<pk>\d+)/delete$', HardwareDeleteView.as_view(),
        name='hardware_delete'),
    url(r'^projects/$', ProjectListView.as_view(), name='project_list'),
    url(r'^projects/(?P<pk>\d+)$', ProjectDetailView.as_view(),
        name='project_detail'),
    url(r'^projects/create$', ProjectCreateView.as_view(),
        name='project_create'),
    url(r'^projects/(?P<pk>\d+)/edit$', ProjectUpdateView.as_view(),
        name='project_edit'),
    url(r'^projects/(?P<pk>\d+)/delete$', ProjectDeleteView.as_view(),
        name='project_delete'),
    url(r'^sections/$', SectionListView.as_view(), name='section_list'),
    url(r'^sections/(?P<pk>\d+)$', SectionDetailView.as_view(),
        name='section_detail'),
    url(r'^sections/create$', SectionCreateView.as_view(),
        name='section_create'),
    url(r'^sections/(?P<pk>\d+)/edit$', SectionUpdateView.as_view(),
        name='section_edit'),
    url(r'^sections/(?P<pk>\d+)/delete$', SectionDeleteView.as_view(),
        name='section_delete'),
    url(r'^gallery/$', GalleryListView.as_view(), name='gallery_list'),
    url(r'^gallery/(?P<pk>\d+)$', GalleryDetailView.as_view(),
        name='gallery_detail'),
    url(r'^gallery/create$', GalleryCreateView.as_view(),
        name='gallery_create'),
    url(r'^gallery/(?P<pk>\d+)/edit$', GalleryUpdateView.as_view(),
        name='gallery_edit'),
    url(r'^gallery/(?P<pk>\d+)/delete$', GalleryDeleteView.as_view(),
        name='gallery_delete'),
]