from django.urls import path
from .views import article_list_view_streaming, article_list_view, article_detail_view


urlpatterns = [
	path("articles/", article_list_view_streaming, name="article_list_view_streaming"),
	path("", article_list_view, name="list"),
	path("articles/detail", article_detail_view, name="article_detail_view"),
]
