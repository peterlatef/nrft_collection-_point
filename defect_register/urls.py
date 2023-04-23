from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.defect_form, name='defect_insert'), 
    path('<int:id>/',views.defect_form, name='defect_update'),
    path('list/', views.defects_list, name='defects_list')
]
