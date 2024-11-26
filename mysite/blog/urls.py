from django.urls import path
from . import views

app_name = 'bloggy'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/<int:month>/<int:year>/<slug:post>/', views.post_detail, name='post_detail'),
] 