"""
Web search tool using DuckDuckGo
"""
from duckduckgo_search import DDGS


def web_search(query: str, num_results: int = 5) -> dict:
    """
    Search the web using DuckDuckGo

    Args:
        query: Search query string
        num_results: Number of results to return

    Returns:
        Dict with query and list of results
    """
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=num_results):
                results.append({
                    "title": r.get("title", ""),
                    "snippet": r.get("body", ""),
                    "url": r.get("href", "")
                })

        return {
            "query": query,
            "results": results
        }

    except Exception as e:
        return {
            "query": query,
            "results": [],
            "error": str(e)
        }