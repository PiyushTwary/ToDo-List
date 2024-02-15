from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('delete/<str:task>/', views.deleteTask, name='delete'),
    path('update/<str:task>/', views.updateTask, name='update'),
    path('reset', views.reset, name="reset")
]
