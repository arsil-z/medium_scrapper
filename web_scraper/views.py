from django.shortcuts import render, HttpResponse
from .utils import _get_url_to_fetch_data

# Create your views here.
from .article_list_data import get_url_on_search, _get_article_detail_url
from .article_detail_data import _get_detail_page_url_by_id


def article_list_view(request):
	response = ""
	search_query = ""
	tags = ""
	if request.method == "POST":
		search_query = request.POST["search_query"]
		source_url = _get_url_to_fetch_data(search_query)
		response, tags = get_url_on_search(source_url)
	context = {
		'response': response,
		'search_query': search_query,
		"tags": tags
	}
	return render(request, "web_scraper/home.html", context)


def article_detail_view(request, search_query, key):
	query_url = _get_url_to_fetch_data(search_query)
	blog_detail_dictionary = _get_detail_page_url_by_id(query_url, key)
	context = {
		"blog_detail_dictionary": blog_detail_dictionary
	}
	return render(request, "web_scraper/blog_detail.html", context)


def article_search_by_tag(request, search_query):
	source_url = _get_url_to_fetch_data(search_query)
	response, tags = get_url_on_search(source_url)
	context = {
		'response': response,
		'search_query': search_query,
		"tags": tags
	}
	return render(request, "web_scraper/result_by_tag.html", context)
