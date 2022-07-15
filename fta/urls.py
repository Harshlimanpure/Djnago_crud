from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete_data'),
    path('<int:id>/',views.update,name='update_data'),
]