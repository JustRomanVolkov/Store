from django.urls import path
from rest_framework.routers import DefaultRouter
from service import views

router = DefaultRouter()

router.register('', views.ItemViewSet, 'item')

urlpatterns = router.urls


urlpatterns += [
    path('buy/<int:id>/', views.CreateCheckoutSessionAPI.as_view(), name='api_create_checkout_session'),
]
