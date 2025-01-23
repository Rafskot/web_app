from django.urls import path
from . import views

urlpatterns = [
    path('', views.tran_home, name='tran_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TranDetailView.as_view(), name='tran-detail'),
    path('<int:pk>/update', views.TranUpdateView.as_view(), name='tran-update'),
    path('<int:pk>/delete', views.TranDeleteView.as_view(), name='tran-delete'),
]