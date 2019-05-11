from django.urls import path
from .views import AppViewIdx, AppViewPage01

app_name = 'app_name_01'

urlpatterns = [
    path('ns_idx/', AppViewIdx.as_view(), name='name_idx'),
    path('ns_pg01/', AppViewPage01.as_view(), name='name_pg01'),
]
