from django.urls import path
from . import views
from .views import Category_Offer,Category_Offer_Create,Category_Offer_Update,Brand_Offer,Brand_Offer_Update,Category_Offer_Delete,Brand_Offer_Delete,Brand_Offer_Create
app_name = 'offer_app'

urlpatterns =[
    path('category_offer',Category_Offer.as_view(),name="category_offer"),
    path('category_status,<int:id>',views.category_status,name="category_status"),
    path('category_offer/create',Category_Offer_Create.as_view(),name="category_offer_create"),
    path('category_offer/update/<int:pk>',Category_Offer_Update.as_view(),name="category_offer_update"),
    path('category_offer/delete/<int:pk>',Category_Offer_Delete.as_view(),name="category_offer_Delete"),
    
    path('brand_offer',Brand_Offer.as_view(),name="brand_offer"),
    path('brand_status,<int:id>',views.brand_status,name="brand_status"),
    path('brand_offer/create',Brand_Offer_Create.as_view(),name="brand_offer_create"),
    path('brand_offer/update/<int:pk>',Brand_Offer_Update.as_view(),name="brand_offer_update"),
    path('brand_offer/delete/<int:pk>',Brand_Offer_Delete.as_view(),name="brand_offer_Delete"),
]