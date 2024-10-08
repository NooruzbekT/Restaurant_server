from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
                  # path('admin/logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path('admin/', admin.site.urls),
                  path('rg/', include('rg.urls')),
                  path('page/', include('page.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  # Optional UI:
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
                  # path(r'^_nested_admin/', include('nested_admin.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
