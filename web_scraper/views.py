from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
from .article_list_data import execute

def article_list_view(request):
	response = ""
	if request.method == "POST":
		search_query = request.POST["search_query"]
		source_url = get_url_to_fetch_data(search_query)
		response = execute(source_url)
	context = {
		'response': response
	}
	return render(request, "web_scraper/home.html", context)

def get_url_to_fetch_data(string):
	source = requests.get(f'https://medium.com/search?q={string}').text
	return source

# def article_detail_view(request, id):
# 	get_artilce_detail_page_url_by_id = get_artilce_detail_page_url(id)
# 	p_this = get_blog_detail(get_artilce_detail_page_url_by_id)
# 	print("test", p_this)
# 	return HttpResponse("Done")
