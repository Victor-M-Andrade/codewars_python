"""
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

"""

def remove_url_anchor(url):
    find = url.find('#')
    if find == -1:
        return url
    else:
        new_url = url[:find]
        return new_url