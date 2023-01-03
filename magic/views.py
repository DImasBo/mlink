from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView, CreateView, DetailView
from django.views.generic.edit import FormMixin

from magic.forms import MagicURLCreateForm
from magic.models import MagicURL

from django.views import View


class MagicURLRedirectView(RedirectView):

    def _check_open_link_in_session(self):
        if not self.request.session.get(f"open-link-{self.kwargs.get('id_path')}"):
            self.request.session[f"open-link-{self.kwargs.get('id_path')}"] = True
            return False
        return True

    def get_redirect_url(self, *args, **kwargs):
        magic_url = MagicURL.objects.get(id_path=kwargs['id_path'])
        if not self._check_open_link_in_session():
            magic_url.add_count_open()

        return magic_url.origin_url


class MagicURLDetailView(DetailView, FormMixin):
    model = MagicURL
    form_class = MagicURLCreateForm
    template_name = "magic/detail.html"

    def _check_obj_in_session(self, magic_origin_url):
        id_path = self.request.session.get(magic_origin_url)
        return id_path

    def get_object(self):
        obj = MagicURL.objects.get(id_path=self.kwargs.get('id_path'))
        if not self._check_obj_in_session(obj.origin_url):
            return None

        return obj


class MagicURLCreateView(CreateView):
    model = MagicURL
    template_name = "magic/base.html"
    form_class = MagicURLCreateForm

    def __create_session_magic_url_ids(self):
        if not self.request.session.session_key:
            self.request.session.create()

    def _save_object_to_session(self, magic_url_obj: MagicURL):
        self.__create_session_magic_url_ids()
        self.request.session[magic_url_obj.origin_url] = magic_url_obj.id_path

    def _valid_replace_url_in_session(self, magic_origin_url):
        self.__create_session_magic_url_ids()
        magic_id_path = self.request.session.get(magic_origin_url)
        if magic_id_path:
            return magic_id_path

    def form_valid(self, form):
        if form.is_valid():
            magic_id_path = self._valid_replace_url_in_session(
                form.cleaned_data['origin_url']
            )
            if magic_id_path:
                obj = MagicURL.objects.get(id_path=magic_id_path)
                return HttpResponseRedirect(obj.get_absolute_url())

        return super().form_valid(form)

    def get_success_url(self):
        self._save_object_to_session(self.object)

        return super().get_success_url()
