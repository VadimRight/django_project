from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('soft_skills/', include('soft_skills.urls')),
    path('hard_skills/', include('hard_skills.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

