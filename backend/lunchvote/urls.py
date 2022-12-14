from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("api/", include("lunchvote.api.urls")),
    path("admin/", admin.site.urls),
    path("", include("lunchvote.home.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
