from django.urls import path


from . import views
from .views import OrderCreateListView, OrderDetailView
urlpatterns = [
    # path('', HelloOrderView.as_view(), name='hello_order'),
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='oreder_detail'),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_status'),
    path('user/<int:user_id>/orders/', views.UserOrderView.as_view(), name='user_orders'),
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetail.as_view(), name='user_specific_detail')
]
