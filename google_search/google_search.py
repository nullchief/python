"""
Use google to search keyword and get links
"""

from selenium import webdriver

def google_search(keyword,pages):
    """
    Args:
        pages: number of google search pages

    """

    driver=webdriver.Chrome()
    driver.get('https://www.google.com/search?q='+ keyword)
    links=[]
    for i in range(pages):
        for elem_a_link in driver.find_elements_by_xpath("//div[@class='r']/a[1]"):
            links.append(elem_a_link.get_attribute('href'))
        
        elems_a=driver.find_elements_by_class_name('pn')
        if len(elems_a)==1:
            elems_a[0].click()
        else:
            elems_a[1].click()
    return links

