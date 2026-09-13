from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.registration, name='register'),
    path('get_cars', views.get_cars, name='getcars'),
    path('analyze_review/', views.analyze_review, name='analyze_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
