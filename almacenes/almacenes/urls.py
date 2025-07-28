from django.conf.urls import include
from django.contrib import admin
from django.urls import path

#Para el Login
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('laboratorio/', include(('apps.laboratorio.urls','apps'), namespace="laboratorio")),
    path('admin/', admin.site.urls),
    path(r'accounts/login/', LoginView.as_view(), {'template_name':'login.html'}, name='login'),

    path(r'logout/', LogoutView.as_view(), name='logout'),
]
