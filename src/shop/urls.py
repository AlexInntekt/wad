from django.urls import path
from .views import SearchView, ListView, DetailView, AdminView, AddItemAdminView, AddCategoryAdminView, EditCategoryAdminView, EditItemAdminView

urlpatterns = [
	path('search', SearchView.as_view(), name='search'),
	path('items', ListView.as_view(), name='listview'),
    path('items/by_category=<str:category>', ListView.as_view(), name='listview_category'),
    # url(r'detail/(?P<pk>\d+)', DetailView.as_view(), name='detailview'),
    path('detail/id=<int:id>', DetailView.as_view(), name='detailview'),
    path('administrare', AdminView.as_view(), name='adminview'),
    path('administrare/add_item', AddItemAdminView.as_view(), name='additem'),
    path('administrare/add_category', AddCategoryAdminView.as_view(), name='addcategory'),
    path('administrare/edit_category/id=<int:id>', EditCategoryAdminView.as_view(), name='editcategory'),
    path('administrare/edit_item/id=<int:id>', EditItemAdminView.as_view(), name='edititem'),
]