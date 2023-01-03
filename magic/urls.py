from django.urls import path
from magic.views import MagicURLRedirectView, MagicURLCreateView, MagicURLDetailView

urlpatterns = [
    path('info/<str:id_path>', MagicURLDetailView.as_view(), name="detail_link"),
    path('<str:id_path>', MagicURLRedirectView.as_view(), name="redirect_link"),
    path('', MagicURLCreateView.as_view(), name='index_create_link'),
]
