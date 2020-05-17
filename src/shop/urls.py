from django.urls import path
from .views import SearchView, ListView, DetailView, AdminView, AddItemAdminView

urlpatterns = [
	path('search', SearchView.as_view(), name='search'),
	path('items', ListView.as_view(), name='listview'),
    path('items/by_category=<str:category>', ListView.as_view(), name='listview_category'),
    # url(r'detail/(?P<pk>\d+)', DetailView.as_view(), name='detailview'),
    path('detail/id=<int:id>', DetailView.as_view(), name='detailview'),
    path('administrare', AdminView.as_view(), name='adminview'),
    path('administrare/add_item', AddItemAdminView.as_view(), name='additem'),
]