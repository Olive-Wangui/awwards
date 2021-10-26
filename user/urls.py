from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('project/', views.project, name='project'),
    path('new/profile/', views.new_profile, name='profile'),
    path('search/', views.search_results, name='search_results'),
    path('rating/<int:pk>/', views.rating, name='rating'),
    path('accounts/profile/', LoginView.as_view(template_name='home.html'), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)