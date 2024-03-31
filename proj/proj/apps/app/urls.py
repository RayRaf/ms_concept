from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.project, name='project'),
    path('sendmail/', views.sendmail, name='sendmail'),
]