from django.urls import path
from .views import SearchView, ListView, DetailView

urlpatterns = [
	path('search', SearchView.as_view(), name='search'),
	path('items', ListView.as_view(), name='listview'),
    # url(r'detail/(?P<pk>\d+)', DetailView.as_view(), name='detailview'),
    path('detail/id=<int:id>', DetailView.as_view(), name='detailview'),
]