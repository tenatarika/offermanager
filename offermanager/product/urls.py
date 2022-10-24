from rest_framework import routers

from product import views

router = routers.DefaultRouter()
router.register('Bank', views.BankViewSet, 'Bank')
router.register('Location', views.LocationViewSet, 'Location')
router.register('Waybill', views.WaybillViewSet, 'Waybill')
router.register('Category', views.CategoryViewSet, 'Category')
router.register('Product', views.ProductViewSet, 'Product')
urlpatterns = router.urls
