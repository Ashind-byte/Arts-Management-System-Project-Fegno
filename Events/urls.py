from django.urls import path

from Events import views

urlpatterns = [
    path("results", views.pub_results, name="pubresults"),
    path("upcoming_events", views.upcoming_events, name="upcoming-events"),
    path("ongoign_events", views.current_events, name="ongoing-events"),
    path("event_details/<int:pk>/", views.CurrentEventDetailView.as_view(), name='event-details'),
    path("scoreboard", views.scoreboard, name='score-board'),
]


