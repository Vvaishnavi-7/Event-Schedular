from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'events'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Auth URL 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Event URLs
    path('list/', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),

    
    path('events/', RedirectView.as_view(url='/list/', permanent=False)),
]
