from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # Corrected the path for home
    # Changed the URL pattern
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail,
         name='product_detail'),  # Changed the URL pattern
    path('products/<int:pk>/edit/', views.edit_product,
         name='edit_product'),  # Changed the URL pattern
    path('products/<int:pk>/delete/', views.delete_product,
         name='delete_product'),  # Changed the URL pattern
    # Moved to the bottom to avoid conflicts
    path('', include('gallery.urls')),
]

# path('admin/', admin.site.urls),
# path('', include('gallery.urls')),
