from django.urls import path
from .views import article_list_view, article_detail_view, article_search_by_tag


urlpatterns = [
	path("", article_list_view, name="article_list_view"),
	path("article/<str:search_query>/<int:key>", article_detail_view, name="article_detail_view"),
	path("article/tag/<str:search_query>", article_search_by_tag, name="article_search_by_tag")
]
