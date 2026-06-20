from duckduckgo_search import DDGS

def search_web(query):
    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=3)

            for r in search_results:
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "content": r.get("body", "")
                })

    except Exception as e:
        return f"Web search error: {str(e)}"

    return results