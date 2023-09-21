from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.soft_skills, name='soft_skills'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
