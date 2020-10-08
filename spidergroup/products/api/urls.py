from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token


from .views import ProductViewSet, CategoryViewSet, CompanyViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('company', CompanyViewSet, basename='company')
router.register('', ProductViewSet, basename='product')


# urlpatterns = [
#     # path('auth/', include('djoser.urls')),
#     path('auth/token/', obtain_auth_token, name='token'),
# ]

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
