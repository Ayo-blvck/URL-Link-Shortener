import pyshorteners

def shorten_link(link):
    s = pyshorteners.Shortener()
    try:
        return s.tinyurl.short(link)
    except Exception as e:
        return f"Error: {str(e)}"
