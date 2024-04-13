from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import index, add_to_cart
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.index, name="home"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)