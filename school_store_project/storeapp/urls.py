from .  import views
from django.urls import path,include

urlpatterns = [

    #path('', views.home, name='home'),
    path('', views.index, name='index.html'),
    path('login', views.login, name='login.html'),
    path('register', views.register, name='register.html'),
    path('new_page', views.new_page, name='new_page.html'),
    path('form_page', views.form_page, name='form_page'),
    path('confirm', views.confirm, name='confirm.html'),
    path('logout', views.logout, name='logout'),

]
