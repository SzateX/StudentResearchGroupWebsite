from django.shortcuts import render
from django.views.generic import *
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin, \
    LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from db.models import *


login_url = '/dashboard/login'


class StrippedDashboardListView(LoginRequiredMixin, PermissionListMixin,
                                ListView):
    login_url = login_url

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.lower()

    def get_template_names(self):
        name = "dashboardapp/%ss/list.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower() + "s"


class PermittedDashboardListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.lower()

    def get_template_names(self):
        name = "dashboardapp/%ss/list.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower() + "s"


class PermittedDashboardDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.view_' + self.model.__name__.lower()

    def get_template_names(self):
        name = "dashboardapp/%ss/detail.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower()


class PermittedDashboardCreateView(LoginRequiredMixin, CreateView):
    login_url = login_url

    def get_template_names(self):
        name = "dashboardapp/%ss/create.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower()


class PermittedDashboardUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.change_' + self.model.__name__.lower()

    def get_template_names(self):
        name = "dashboardapp/%ss/update.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower()


class PermittedDashboardDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = login_url
    raise_exception = True

    def get_required_permissions(self, request=None):
        return 'db.delete_' + self.model.__name__.lower()

    def get_template_names(self):
        name = "dashboardapp/%ss/delete.html" % self.model.__name__.lower()
        return [name]

    def get_context_object_name(self, object_list):
        return self.model.__name__.lower()


class DashboardLoginView(LoginView):
    template_name = 'dashboardapp/login.html'

    def get_redirect_url(self):
        redirect_url = super(DashboardLoginView, self).get_redirect_url()
        if redirect_url == '':
            return '/dashboard/'
        return redirect_url


class DashboardLogoutView(LoginRequiredMixin, LogoutView):
    login_url = login_url
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
    fields = '__all__'
    success_url = '/dashboard/articles'


class ArticleUpdateView(PermittedDashboardUpdateView):
    model = Article
    fields = '__all__'
    success_url = '/dashboard/articles'


class ArticleDeleteView(PermittedDashboardDeleteView):
    model = Article


class HardwareListView(PermittedDashboardListView):
    model = Hardware


class HardwareCreateView(PermittedDashboardCreateView):
    model = Hardware
    fields = '__all__'
    success_url = '/dashboard/hardware'


class HardwareUpdateView(PermittedDashboardUpdateView):
    model = Hardware
    fields = '__all__'
    success_url = '/dashboard/hardware'


class HardwareDeleteView(PermittedDashboardDeleteView):
    model = Hardware


class ProjectListView(StrippedDashboardListView):
    model = Project


class ProjectDetailView(PermittedDashboardDetailView):
    model = Project


class ProjectCreateView(PermittedDashboardCreateView):
    model = Project
    fields = '__all__'
    success_url = '/dashboard/projects'


class ProjectUpdateView(PermittedDashboardUpdateView):
    model = Project
    fields = '__all__'
    success_url = '/dashboard/projects'


class ProjectDeleteView(PermittedDashboardDeleteView):
    model = Project


class SectionListView(StrippedDashboardListView):
    model = Section


class SectionDetailView(PermittedDashboardDetailView):
    model = Section


class SectionCreateView(PermittedDashboardCreateView):
    model = Section
    fields = '__all__'
    success_url = '/dashboard/sections'


class SectionUpdateView(PermittedDashboardUpdateView):
    model = Section
    fields = '__all__'
    success_url = '/dashboard/sections'


class SectionDeleteView(PermittedDashboardDeleteView):
    model = Section
    
    
class GalleryListView(StrippedDashboardListView):
    model = Gallery


class GalleryDetailView(PermittedDashboardDetailView):
    model = Gallery


class GalleryCreateView(PermittedDashboardCreateView):
    model = Gallery
    fields = '__all__'
    success_url = '/dashboard/gallery'


class GalleryUpdateView(PermittedDashboardUpdateView):
    model = Gallery
    fields = '__all__'
    success_url = '/dashboard/gallery'


class GalleryDeleteView(PermittedDashboardDeleteView):
    model = Gallery
