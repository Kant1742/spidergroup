from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token


from .views import ProductViewSet, CategoryViewSet, CompanyViewSet, CompaniesListView, SingleCompanyView

router = SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
# router.register('company', CompanyViewSet, basename='company')
router.register('', ProductViewSet, basename='product')


# urlpatterns = [
#     # path('auth/', include('djoser.urls')),
#     path('auth/token/', obtain_auth_token, name='token'),
# ]

urlpatterns = [
    path('company/<int:pk>/', SingleCompanyView.as_view(), name='single-company'),
    path('company/', CompaniesListView.as_view(), name='companies'),
    path('', include(router.urls)),
]
