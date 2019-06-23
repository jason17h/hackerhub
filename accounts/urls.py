from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('view-profile/<username>/', views.view_profile, name='view_profile')

]