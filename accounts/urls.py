from django.urls import path
from django.urls import include

from rest_framework.routers import SimpleRouter

from accounts import views as user_views
router = SimpleRouter()

router.register(r'user', user_views.UserView, basename='sign-up')


urlpatterns = [
    path('login/', user_views.LoginView.as_view()),
    path('', include(router.urls))
]
