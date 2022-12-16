from django.urls import path
from . import views

app_name = 'appsch'

urlpatterns = [
    path('', views.AllItems.as_view(), name='all_items'),
    path('additem/', views.AddItem.as_view(), name='add_item'),
    path('item/<int:itemid>', views.ShowItem.as_view(), name='show_item'),
]


