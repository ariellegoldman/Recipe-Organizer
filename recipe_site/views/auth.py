from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from rest_framework import views
from rest_framework import renderers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from recipe_site.renderers.html_renderer import HTMLRenderer


class SessionAuth(views.APIView):
    template_name = "site/login.jinja2"
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        login(request, user)
        if isinstance(request.accepted_renderer, HTMLRenderer):
            return HttpResponseRedirect("/")
        else:
            return Response({})

    def get(self, request, *args, **kwargs):
        return Response({})


class SessionClose(views.APIView):
    template_name = "site/logout.jinja2"
    renderer_classes = (HTMLRenderer, renderers.JSONRenderer)

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            logout(request)

            if isinstance(request.accepted_renderer, HTMLRenderer):
                return HttpResponseRedirect(reverse("home"))
            return Response({})
        else:
            return Response({}, status=status.HTTP_403_FORBIDDEN)
