# google_search.py  WRITE-UP
## Prerequisites (For Noob)
* using selenium locate element by xpath with specific attribute: 
`` driver.find_element_by_xpath(""//div[@class='r']") `` 
* if you want to find the sub element, don't forget to there may be multiple sub elements, so need to choose one: (index starts from 1)
`` driver.find_element_by_xpath("//div[@class='r']/a[1]") `` 
* about google search:
    * ``soup<'cite'>`` will output all the results' links, but without http://
    * **the reason why I don't use bs4 and requests** is because the next page link doesn't work, so if you use bs4 and request, you can only extract the first search page's result links,  **what i think, it's because the real next page link is created by js**
* bs4
    * `.string` to extract text
    * `print(soup.prettify())`  to take a clear look at the source code
    * find tag with specific attribute: `soup(href='xxx')`
* `pprint.pprint(xxx)` is useful to output clearly
## Code Explanation
```python
"""Use google to search keyword and get results' links.

The initial reason why i want to write this program is because I want to
get all the high schools' websites in China, so I can import these links
to Acunetix to pentest.

Example:
    import google_search,pprint
    links=google_search.google_search("高中 网站",5)
    pprint.pprint(links)

Todo:
    * get rid of those famous websites
"""

from selenium import webdriver

def google_search(keyword,pages):
    """
    Args:
        pages: number of google search pages.

    Returns:
        list: a list of results' links.
    """

    driver=webdriver.Chrome()
    driver.get('https://www.google.com/search?q='+ keyword)
    links=[]
    for i in range(pages):
        for elem_a_link in driver.find_elements_by_xpath("//div[@class='r']/a[1]"):
            links.append(elem_a_link.get_attribute('href'))
        
        elems_a=driver.find_elements_by_class_name('pn')
        #the previous page link and next page link are all class 'pn'
        #so it needs this if...else... 
        if len(elems_a)==1:
            elems_a[0].click()
        else:
            elems_a[1].click()
    return links

```
