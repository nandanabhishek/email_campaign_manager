from django.urls import path
from . import views

urlpatterns = [
    path('add_subscriber/', views.add_subscriber, name='add_subscriber'),
    path('add_campaign/', views.add_campaign, name='add_campaign'),
    path('subscriber_list/', views.subscriber_list, name='subscriber_list'),
    path('campaign_list/', views.campaign_list, name='campaign_list'),
    path('unsubscribe/<int:subscriber_id>/', views.unsubscribe, name='unsubscribe'),
]
