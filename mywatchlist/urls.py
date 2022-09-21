from django.urls import path
from mywatchlist.views import show_watchlist, show_json, show_html, show_watchlist_index, show_xml

app_name ="mywatchlist"
urlpatterns = [
    path('', show_watchlist_index, name="show_watchlist_index"),
    path('json', show_json, name="show_json"),
    path('xml', show_xml, name="show_xml"),
    path('html', show_watchlist,name="show_html"),
]