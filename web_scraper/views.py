from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleDetail
from .utils import _get_url_to_fetch_data
from django.http import StreamingHttpResponse, HttpResponse
from .article_list_data import get_url_on_search
import json


@csrf_exempt
def article_list_view_streaming(request):
	if request.method == "POST":
		data = json.loads(request.body)
		# print("DATA", data)
		search_query = data['search_query']
		source_url = _get_url_to_fetch_data(search_query)
		response = get_url_on_search(source_url)
		data = response
		# print(data)
		return StreamingHttpResponse(data, content_type='text/event-stream')


def article_list_view(request):

	return render(request, 'web_scraper/list.html')


def article_detail_view(request):
	url = request.GET.get('blog_url')
	if url is None:
		return HttpResponse('Blog url was not provided', status=400)
	article = ArticleDetail.objects.get(url=url)
	print(article)
	context = {
		'article': article
	}
	return render(request, "web_scraper/detail.html", context)

