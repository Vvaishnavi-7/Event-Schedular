from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # home page
    path('', views.home, name='home'),

    # auth
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # events app
    path('events/', include('events.urls')),
]
