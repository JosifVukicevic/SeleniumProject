from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.prikazi_tendere, name='prikazi_tendere'),
    path('update_keywords/', views.update_keywords, name='update_keywords'),
    # path('', views.pretraga_i_spremanje_tendera, name='pretraga_i_spremanje_tendera'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
