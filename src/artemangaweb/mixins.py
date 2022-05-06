from urllib.parse import urlparse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import resolve_url
from django.urls import reverse_lazy

from cuenta_usuario.enums.opciones import TipoUsuario


class MensajeResultadoFormMixin:
    mensaje_exito = 'Operación realizada con éxito'
    mensaje_error = 'Ha ocurrido un error'

    def form_valid(self, form):
        messages.success(self.request, self.mensaje_exito)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.mensaje_error)
        return super().form_invalid(form)


class TituloPaginaMixin(object):
    def get_page_title(self, context):
        return getattr(self, "titulo_pagina", "Una página sin título")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = self.get_page_title(context)

        return context


class VistaRestringidaMixin(LoginRequiredMixin):
    usuarios_permitidos: list[TipoUsuario] = [TipoUsuario.ADMINISTRADOR]
    login_url = reverse_lazy('login')
    permission_denied_message = 'No tiene permisos para acceder a esta página. ' \
                                'Si crees que deberías, por favor contacta al administrador de sistema.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.tipo_usuario not in self.valores_usuarios_permitidos:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        # If the login url is the same scheme and net location then use the
        # path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )

    @property
    def valores_usuarios_permitidos(self):
        return [tipo.value for tipo in self.usuarios_permitidos]
