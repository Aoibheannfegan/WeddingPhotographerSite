from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("packages", views.packages, name="packages"),
    path("gallery", views.gallery, name="gallery"),
    path("appointment", views.appointment, name="appointment"),
    path("clients", views.clients, name="clients"),
    path("clients/<int:client_id>/", views.client, name="client"),
    path('approve_request/<int:client_id>/', views.approve_request, name='approve_request'),
    path('note/<int:client_id>/', views.note, name='note'),
    path('calendar', views.calendar, name='calendar'),
    path('api/unavailable_dates/', views.get_unavailable_dates, name='unavailable_dates'),
    path('api/event_details/<int:event_id>/', views.event_details, name='event_details'),
    path("edit/<int:package_id>/", views.edit_button, name="edit_button"),
    path('api/package_details/<int:package_id>/', views.package_details, name='package_details'),
]