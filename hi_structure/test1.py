def create_twitter_search_url(query):
    # 使用 urllib.parse.quote_plus 来确保字符串被正确编码为 URL 格式
    from urllib.parse import quote_plus

    base_url = "https://twitter.com/search?f=top&q="
    encoded_query = quote_plus(query)  # 对输入字符串进行URL编码
    url = f"{base_url}{encoded_query}{{}}{{}}&src=typed_query"

    return url


# 测试函数
query = "thanks chatgpt and ai"
url = create_twitter_search_url(query)
print(url)
