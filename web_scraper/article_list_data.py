import json
import time

from .utils import _get_soup
from .models import Article, ArticleDetail
from .article_detail_data import get_blog_detail
from django.conf import settings

# Article List Page Data

def _save_article_to_database(article):
	article_image_url = article["article_image_url"]
	article_, created = Article.objects.get_or_create(detail_url=article_image_url)
	article_.title = article['article_title']
	article_.image = article['article_image_url']
	article_.likes = article['article_likes_count']
	article_.responses = article['article_response_count']
	article_.tags = article['tags_list']
	article_.creator = article['creator_name']
	article_.creator_image = article['creator_image_url']
	article_.save()


def _save_article_details_to_database(article):
	detail_url = article["article_details_page_url"]
	article_details_ = get_blog_detail(detail_url)
	article_details, created_ = ArticleDetail.objects.get_or_create(url=detail_url)

	if created_:
		article_details.title = article_details_['blog_title']
		article_details.image = article_details_['blog_image_url']
		article_details.likes = article_details_['blog_claps_count']
		article_details.responses = article_details_['blog_response_count']
		article_details.tags = article_details_['blog_tags_list']
		article_details.paragraph = article_details_['blog_paragraph_list']
		article_details.creator = article_details_['creator_name']
		article_details.creator_image = article_details_['creator_image_url']
		article_details.save()
	# elif ArticleDetail.objects.filter(url=detail_url).exists():
	# 	article_details.title = article_details_['blog_title']
	# 	article_details.image = article_details_['blog_image_url']
	# 	article_details.likes = article_details_['blog_claps_count']
	# 	article_details.responses = article_details_['blog_response_count']
	# 	article_details.tags = article_details_['blog_tags_list']
	# 	article_details.paragraph = article_details_['blog_paragraph_list']
	# 	article_details.creator = article_details_['creator_name']
	# 	article_details.creator_image = article_details_['creator_image_url']
	# 	article_details.save()


def get_url_on_search(url):
	soup = _get_soup(url)
	for article in _get_combined_data(soup):
		time.sleep(settings.SCRAPING_SLEEP_TIME)
		_save_article_to_database(article)
		_save_article_details_to_database(article)
		yield json.dumps(article) + '$'


def _get_creator_name_and_image(article):
	creator_details_flexbox_tag = article.find('div', class_="u-flexCenter")
	creator_name = creator_details_flexbox_tag.find("a", class_="ds-link").text
	creator_image_url = creator_details_flexbox_tag.find('img', class_="avatar-image")['src']
	return creator_name, creator_image_url


def _get_article_like_and_response(article):
	article_likes_and_responses_div_tag = article.find("div", class_="u-paddingTop10")
	# print("DIV", article_likes_and_responses_div_tag.prettify())
	article_likes_div_tag = article_likes_and_responses_div_tag.find("div", class_="u-floatLeft")
	article_likes_inner_div_tag = article_likes_div_tag.find("div", class_="u-flexCenter")
	article_likes_count = article_likes_inner_div_tag.find("span", class_="u-relative").button.text
	# print("Likes", article_likes_count)
	try:
		article_response_count = article_likes_and_responses_div_tag.find("a", class_="u-baseColor--buttonNormal").text
	except:
		article_response_count = "No Response count found for this article"
	return article_likes_count, article_response_count


def _get_article_title_and_image(article):
	article_title_and_image_div_tag = article.find("div", class_="section-inner")
	try:
		article_title = article_title_and_image_div_tag.find("h2", class_="graf--title").text
	except:
		article_title = article_title_and_image_div_tag.find("h3", class_="graf--title").text
	article_image_figure_tag = article_title_and_image_div_tag.find("figure", class_="graf--figure")
	try:
		article_image_div_tag = article_image_figure_tag.find("div", class_="aspectRatioPlaceholder is-locked")
		article_image_url = article_image_div_tag.find("img", class_="graf-image")['src']
	# print("THIS",article_image_url)

	except:
		article_image_div_tag = None
		article_image_url = "Image Not Found"
	return article_title, article_image_url


def _get_article_detail_page_url(article):
	try:
		article_detail_page_div_tag = article.find("div", class_="postArticle-readMore")
		article_detail_page_url = article_detail_page_div_tag.find("a", class_="button--smaller")['href']
	except:
		article_detail_page_url = "Detail Page Does not exits"
	return article_detail_page_url


def _get_tags(soup):
	tags_ul_tag = soup.find("ul", class_="tags tags--postTags tags--light")
	tags_list = []
	for tag in tags_ul_tag.find_all("a", class_="link u-baseColor--link"):
		tags_list.append(tag.text)
	# print(tags_list)
	return tags_list


def _get_combined_data(soup):
	tags = _get_tags(soup)
	count_of_article = 1
	for article in soup.find_all('div', class_="postArticle"):
		creator_details = _get_creator_name_and_image(article)
		article_title_and_image = _get_article_title_and_image(article)
		article_detail_page_url = _get_article_detail_page_url(article)
		article_like_and_response_count = _get_article_like_and_response(article)

		article_dictionary = {
			"key": count_of_article,
			"creator_name": creator_details[0],
			"creator_image_url": creator_details[1],
			"article_title": article_title_and_image[0],
			"article_image_url": article_title_and_image[1],
			"article_details_page_url": article_detail_page_url,
			"article_likes_count": article_like_and_response_count[0],
			"article_response_count": article_like_and_response_count[1],
			"tags_list": tags
		}
		count_of_article += 1
		yield article_dictionary


def _get_article_detail_url(url):
	soup = _get_soup(url)
	article_detail_url_dictionary = {}
	count_of_article = 0
	for article in soup.find_all('div', class_="postArticle"):
		article_detail_page_url = _get_article_detail_page_url(article)
		article_detail_url_dictionary[count_of_article] = article_detail_page_url
		count_of_article += 1
	return article_detail_url_dictionary
