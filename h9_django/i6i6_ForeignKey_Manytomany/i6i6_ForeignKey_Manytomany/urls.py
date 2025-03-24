from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'Наша админка'
admin.site.index_title = 'Наша под админка'


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('app_movie.urls')),
] + debug_toolbar_urls()