import requests
from bs4 import BeautifulSoup


# Article Detail Page Data

#
# source = requests.get("https://medium.com/hackernoon/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f").text
# soup = BeautifulSoup(source, "lxml")
# blog_detail_main_div_tag = soup.find("h1").parent.parent



def get_creator_details(blog_detail_main_div_tag):
	blog_heading_and_creator_div_tag = blog_detail_main_div_tag.div
	blog_heading_tag = blog_heading_and_creator_div_tag.h1
	blog_heading = blog_heading_tag.text  #
	blog_creator_div_tag = blog_heading_and_creator_div_tag.find("div", class_="o n")
	# print(blog_creator_div_tag)
	blog_creator_image_tag = blog_creator_div_tag.find("div")
	blog_creator_image_url = blog_creator_image_tag.find("img")["src"]  #
	blog_creator_name = blog_creator_image_tag.find("img")["alt"]  #
	return blog_heading, blog_creator_image_url, blog_creator_name


# print(blog_creator_image_tag.prettify())
# print(blog_creator_name)

def get_blog_image_and_paragraphs(blog_detail_main_div_tag):
	blog_image_figure_tag = blog_detail_main_div_tag.find("figure")
	try:
		blog_image_url = blog_image_figure_tag.find("img")["src"]  #
	except:
		blog_image_url = None
	print(blog_image_url)
	blog_image_p_tags = blog_detail_main_div_tag.find_all("p")
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
	# blog_claps_and_response_div_tag = blog_tags_ul_tag.parent.next_sibling
	# blog_claps_count = blog_claps_and_response_div_tag.button.text  #
	# # blog_response_h4_tag = blog_claps_and_response_div_tag.find("div", class_="r ei pr my ps na pt nc pu pv pw px").h4
	# try:
	# 	blog_response_h4_tag = blog_claps_and_response_div_tag.find("div",
	# 																class_="r ei pr my ps na pt nc pu pv pw px").h4
	# except:
	# 	blog_response_h4_tag = None
	# try:
	# 	blog_response_count = blog_response_h4_tag.text  #
	# except:
	# 	blog_response_count = None  #
	# te = soup.find("article").next_sibling
	# tes = te.find("div", class_="vi")
	# print(te)
	te = soup.find_all("h4")
	blog_claps_count = te[1].text
	blog_response_count = te[2].text
	print(blog_claps_count, blog_response_count)
	return blog_tags_list, blog_claps_count, blog_response_count


def get_blog_detail_data(soup, blog_detail_main_div_tag):
	blog_creator_details = get_creator_details(blog_detail_main_div_tag)
	blog_image_and_tags = get_blog_image_and_paragraphs(blog_detail_main_div_tag)
	blog_tags_claps_response = get_blog_tags_claps_and_response_count(soup)
	dictionary = {
		"blog_creator_details": blog_creator_details,
		"blog_image_and_tags": blog_image_and_tags,
		"blog_tags_claps_response": blog_tags_claps_response
	}
	# print(dictionary)
	return dictionary


def get_blog_detail(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, "lxml")
	blog_detail_main_div_tag = soup.find("h1").parent.parent
	result_dictionary = get_blog_detail_data(soup, blog_detail_main_div_tag)
	# print(result_dictionary)
	return result_dictionary
# get_blog_detail_data(soup, blog_detail_main_div_tag)
# get_blog_detail("https://medium.com/hackernoon/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f")
get_blog_detail("https://medium.com/free-code-camp/a-study-plan-to-cure-javascript-fatigue-8ad3a54f2eb1")
