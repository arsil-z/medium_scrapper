import requests
from bs4 import BeautifulSoup
from .utils import _get_soup
from .article_list_data import _get_article_detail_page_url
# Article Detail Page Data


def get_creator_details(blog_detail_main_div_tag):
	blog_heading_and_creator_div_tag = blog_detail_main_div_tag.div
	blog_heading_tag = blog_heading_and_creator_div_tag.h1
	blog_heading = blog_heading_tag.text  #
	print(blog_heading)
	blog_creator_div_tag = blog_heading_and_creator_div_tag.find("div", class_="o n")
	print(blog_creator_div_tag)
	blog_creator_image_tag = blog_creator_div_tag.find("div")
	blog_creator_image_url = blog_creator_image_tag.find("img")["src"]  #
	blog_creator_name = blog_creator_image_tag.find("img")["alt"]  #
	return blog_heading, blog_creator_image_url, blog_creator_name


def get_blog_image_and_paragraphs(blog_detail_figure_tag):
	blog_image_url = blog_detail_figure_tag.find("img")["src"]
	b = blog_detail_figure_tag.parent.next_sibling
	blog_image_p_tags = b.find_all("p")
	blog_description_data = []  #
	for p in blog_image_p_tags:
		blog_description_data.append(p.text)
	return blog_image_url, blog_description_data


def get_blog_tags_claps_and_response_count(soup):
	blog_tags_main_div_tag = soup.find("article").next_sibling.next_sibling.next_sibling
	blog_tags_ul_tag = blog_tags_main_div_tag.find("ul")
	blog_tags_li_tags = blog_tags_ul_tag.find_all("li")
	blog_tags_list = []  #
	for tag in blog_tags_li_tags:
		blog_tags_list.append(tag.text)
	te = soup.find_all("h4")
	blog_claps_count = te[1].text
	blog_response_count = te[2].text
	# print(blog_claps_count, blog_response_count)
	return blog_tags_list, blog_claps_count, blog_response_count


def get_blog_detail_data(soup, blog_detail_main_div_tag, blog_detail_figure_tag):
	blog_creator_details = get_creator_details(blog_detail_main_div_tag)
	blog_image_and_paragraph = get_blog_image_and_paragraphs(blog_detail_figure_tag)
	blog_tags_claps_response = get_blog_tags_claps_and_response_count(soup)
	dictionary = {
		"blog_title": blog_creator_details[0],
		"creator_image_url": blog_creator_details[1],
		"creator_name": blog_creator_details[2],
		"blog_image_url": blog_image_and_paragraph[0],
		"blog_paragraph_list": blog_image_and_paragraph[1],
		"blog_tags_list": blog_tags_claps_response[0],
		"blog_claps_count": blog_tags_claps_response[1],
		"blog_response_count": blog_tags_claps_response[2]
	}
	# print(dictionary)
	return dictionary


def get_blog_detail(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, "lxml")
	blog_detail_main_div_tag = soup.find("h1").parent.parent
	blog_detail_figure_tag = soup.find("figure")
	result_dictionary = get_blog_detail_data(soup, blog_detail_main_div_tag, blog_detail_figure_tag)
	return result_dictionary


def _get_id_of_article_url_page(url):
	soup = _get_soup(url)
	article_detail_url_dictionary = {}
	count_of_article = 0
	for article in soup.find_all('div', class_="postArticle"):
		article_detail_page_url = _get_article_detail_page_url(article)
		article_detail_url_dictionary[count_of_article] = article_detail_page_url
		count_of_article += 1
	return article_detail_url_dictionary


def _get_detail_page_url_by_id(url, id):
	detail_page_urls = _get_id_of_article_url_page(url)
	detail_url = detail_page_urls[id]
	blog_detail_dictionary = get_blog_detail(detail_url)
	return blog_detail_dictionary
