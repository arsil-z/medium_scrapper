from django.urls import path
from .views import article_search_by_tag, article_list_view_streaming, article_list_view, article_detail_view


urlpatterns = [
	path("article/", article_list_view_streaming, name="article_list_view_streaming"),
	path("", article_list_view, name="list"),
	path("articles/detail", article_detail_view, name="article_detail_view"),
	# path("article/<str:search_query>/<int:key>", article_detail_view, name="article_detail_view"),
	path("article/tag/<str:search_query>", article_search_by_tag, name="article_search_by_tag")
]
