from django.shortcuts import render
from django.views.generic import *
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin, \
    LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from db.models import *


login_url = ''


class StrippedDashboardListView(PermissionListMixin, ListView):
    login_url = login_url

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/list.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower() + "s"


class PermittedDashboardListView(PermissionRequiredMixin, ListView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/list.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower() + "s"


class PermittedDashboardDetailView(PermissionRequiredMixin, DetailView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/detail.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower()


class PermittedDashboardCreateView(PermissionRequiredMixin, CreateView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.add_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/create.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower()


class PermittedDashboardUpdateView(PermissionRequiredMixin, UpdateView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.change_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/update.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower()


class PermittedDashboardDeleteView(PermissionRequiredMixin, DeleteView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.delete_' + self.model.__name__.tolower()

    def get_template_names(self):
        name = "dashboardapp/%ss/delete.html" % self.model.__name__.tolower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.tolower()


class DashboardLoginView(LoginView):
    template_name = 'dashboardapp/login.html'


class DashboardLogoutView(LoginView):
    template_name = 'dashboardapp/logout.html'


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboardapp/dashboard.html'
    login_url = login_url


class ArticleListView(StrippedDashboardListView):
    model = Article


class ArticleDetailView(PermittedDashboardDetailView):
    model = Article


class ArticleCreateView(PermittedDashboardCreateView):
    model = Article


class ArticleUpdateView(PermittedDashboardUpdateView):
    model = Article


class ArticleDeleteView(PermittedDashboardDeleteView):
    model = Article


class HardwareListView(PermittedDashboardListView):
    model = Hardware


class HardwareCreateView(PermittedDashboardCreateView):
    model = Hardware


class HardwareUpdateView(PermittedDashboardUpdateView):
    model = Hardware


class HardwareDeleteView(PermittedDashboardDeleteView):
    model = Hardware


class ProjectListView(StrippedDashboardListView):
    model = Project


class ProjectDetailView(PermittedDashboardDetailView):
    model = Project


class ProjectCreateView(PermittedDashboardCreateView):
    model = Project


class ProjectUpdateView(PermittedDashboardUpdateView):
    model = Project


class ProjectDeleteView(PermittedDashboardDeleteView):
    model = Project


class SectionListView(StrippedDashboardListView):
    model = Section


class SectionDetailView(PermittedDashboardDetailView):
    model = Section


class SectionCreateView(PermittedDashboardCreateView):
    model = Section


class SectionUpdateView(PermittedDashboardUpdateView):
    model = Section


class SectionDeleteView(PermittedDashboardDeleteView):
    model = Section
    
    
class GalleryListView(StrippedDashboardListView):
    model = Gallery


class GalleryDetailView(PermittedDashboardDetailView):
    model = Gallery


class GalleryCreateView(PermittedDashboardCreateView):
    model = Gallery


class GalleryUpdateView(PermittedDashboardUpdateView):
    model = Gallery


class GalleryDeleteView(PermittedDashboardDeleteView):
    model = Gallery
