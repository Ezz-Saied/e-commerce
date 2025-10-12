from django.urls import path
from . import views
urlpatterns = [
    path("", views.Check_OutView.as_view(), name="check_out"),
]
