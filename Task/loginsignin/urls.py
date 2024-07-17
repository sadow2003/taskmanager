from django.urls import path
from . import views


urlpatterns = [
    path("",views.homepage,name=""),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('user-logout', views.user_logout,name="user-logout"),
    path('adminpass',views.adminpass,name="adminpass"),
    path('adminpass1',views.adminpass1,name="adminpass1"),
    path('admin_dash',views.admin_dash,name="admin_dash"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('create_task',views.create_task,name="create_task"),
    path('view_task',views.view_task,name="view_task"),
    path('update_task/<str:pk>/',views.update_task,name="update_task"),
    path('delete_task/<str:pk>/',views.delete_task,name="delete_task"),
    path('create_user',views.create_user,name="create_user"),
    path('view_user',views.view_user,name="view_user"),
    path('update_user/<int:pk>/',views.update_user,name="update_user"),
    path('delete_user/<int:pk>/',views.delete_user,name="delete_user"),
]








