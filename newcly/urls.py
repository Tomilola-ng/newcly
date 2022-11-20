from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from users.views import register as registerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication Views
    path('dashboard/', include('users.urls')),
    path('register/', registerView, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Posts Views
    path('posts/', include('posts.urls')),

    # Redirect View
    path('', RedirectView.as_view(url='posts/'))

]
