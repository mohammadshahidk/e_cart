from rest_framework.routers import SimpleRouter

from store import views as store_views


router = SimpleRouter()

router.register(r'product', store_views.ProductView, basename='products')
router.register(r'cart_item', store_views.CartItemView, basename='cart-item')
router.register(r'cart', store_views.CartView, basename='cart')

urlpatterns = router.urls
