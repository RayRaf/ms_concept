from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.project, name='project'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('<int:project_id>/<str:section>', views.docsectionspec, name='docsectionspec'),
    path('<int:project_id>/<str:section>/specprint', views.specprint, name='specprint'),
    path('product/<int:product_id>', views.product_properties, name='product_properties'),
]