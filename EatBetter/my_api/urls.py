from django.urls import path, include
from .views import ListAlimentsView, ListFoodView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'aliments', ListAlimentsView)
router.register(r'foods', ListFoodView)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]