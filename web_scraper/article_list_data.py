from .utils import _get_soup


# Article List Page Data


def get_url_on_search(url):
	soup = _get_soup(url)
	combined_data_dictionary = _get_combined_data(soup)
	tags = _get_tags(soup)
	return combined_data_dictionary, tags


def _get_creator_name_and_image(article):
	creator_details_flexbox_tag = article.find('div', class_="u-flexCenter")
	creator_name = creator_details_flexbox_tag.find("a", class_="ds-link").text
	creator_image_url = creator_details_flexbox_tag.find('img', class_="avatar-image")['src']
	return creator_name, creator_image_url


def _get_article_like_and_response(article):
	article_likes_and_responses_div_tag = article.find("div", class_="u-paddingTop10")
	article_likes_div_tag = article_likes_and_responses_div_tag.find("div", class_="u-floatLeft")
	article_likes_inner_div_tag = article_likes_div_tag.find("div", class_="u-flexCenter")
	article_likes_count = article_likes_inner_div_tag.find("span", class_="u-relative").button.text
	article_response_count = article_likes_and_responses_div_tag.find("a", class_="u-baseColor--buttonNormal").text
	return article_likes_count, article_response_count


def _get_article_title_and_image(article):
	article_title_and_image_div_tag = article.find("div", class_="section-inner")
	try:
		article_title = article_title_and_image_div_tag.find("h2", class_="graf--title").text
	except:
		article_title = article_title_and_image_div_tag.find("h3", class_="graf--title").text
	article_image_figure_tag = article_title_and_image_div_tag.find("figure", class_="graf--figure")
	article_image_div_tag = article_image_figure_tag.find("div", class_="aspectRatioPlaceholder is-locked")
	article_image_url = article_image_div_tag.find("img", class_="graf-image")['src']
	return article_title, article_image_url


def _get_article_detail_page_url(article):
	article_detail_page_div_tag = article.find("div", class_="postArticle-readMore")
	article_detail_page_url = article_detail_page_div_tag.find("a", class_="button--smaller")['href']
	return article_detail_page_url


def _get_combined_data(soup):
	article_data = {}
	count_of_article = 0
	for article in soup.find_all('div', class_="postArticle"):
		creator_details = _get_creator_name_and_image(article)
		article_title_and_image = _get_article_title_and_image(article)
		article_detail_page_url = _get_article_detail_page_url(article)
		article_like_and_response_count = _get_article_like_and_response(article)

		article_dictionary = {
			"creator_name": creator_details[0],
			"creator_image_url": creator_details[1],
			"article_title": article_title_and_image[0],
			"article_image_url": article_title_and_image[1],
			"article_details_page_url": article_detail_page_url,
			"article_likes_count": article_like_and_response_count[0],
			"article_response_count": article_like_and_response_count[1]
		}
		article_data[count_of_article] = article_dictionary
		count_of_article += 1
	return article_data


def _get_tags(soup):
	tags_ul_tag = soup.find("ul", class_="tags tags--postTags tags--light")
	tags_list = []
	for tag in tags_ul_tag.find_all("a", class_="link u-baseColor--link"):
		tags_list.append(tag.text)
	# print(tags_list)
	return tags_list


def _get_article_detail_url(url):
	soup = _get_soup(url)
	article_detail_url_dictionary = {}
	count_of_article = 0
	for article in soup.find_all('div', class_="postArticle"):
		article_detail_page_url = _get_article_detail_page_url(article)
		article_detail_url_dictionary[count_of_article] = article_detail_page_url
		count_of_article += 1
	return article_detail_url_dictionary
