import wikipedia
from yake import KeywordExtractor


# build a function the retrieves a list of possible pages from wikipedia
def get_wiki_pages(search_term):
    """Get a list of possible pages from wikipedia."""
    return wikipedia.search(search_term)


# build a function that retrieves the summary of a page from wikipedia
def get_wiki_summary(page):
    """Get the summary of a page from wikipedia."""
    return wikipedia.summary(page)


# build a function that retrieves the content of a page from wikipedia
def get_wiki_content(page):
    """Get the content of a page from wikipedia."""
    return wikipedia.page(page).content


# return the top 10 keywords from the content of a page
def get_wiki_keywords(page):
    """Get the top 10 keywords from the content of a page."""
    content = get_wiki_content(page)
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    # return a dictionary of the top 10 keywords
    return {keyword: score for keyword, score in keywords[:10]}
