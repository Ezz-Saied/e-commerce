from django.urls import path
from . import views
urlpatterns = [
    path("", views.Check_OutView.as_view(), name="check_out"),
    path("success", views.SuccessView.as_view(), name="success"),
    path("orders", views.OrderView.as_view(), name="orders-list"),
    path("order/<int:pk>", views.Order_DetailView.as_view(), name="order-detail")
]
