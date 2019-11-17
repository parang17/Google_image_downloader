# https://stackoverflow.com/questions/40555930/selenium-chromedriver-executable-needs-to-be-in-path

from selenium import webdriver
import json
import os
import requests
cwd = os.getcwd()



def google_image_scroller(img_search_name):

    searchterm = img_search_name # will also be the name of the folder
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    browser = webdriver.Chrome(executable_path="/home/youngjun/Documents/devel/chromedriver")
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
    counter = 0
    succounter = 0

    download_dir = "data"
    img_dir = download_dir + '/' + searchterm.replace(" ", "")

    #Create download folder
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Make a folder
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    for _ in range(5000):
        browser.execute_script("window.scrollBy(0,10000)")

    for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):

        file_name = searchterm + '_' + str(counter)

        counter = counter + 1
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)
        print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
        try:
            file = img_dir + '/' + searchterm.replace(" ", "") + '_{0:04}'.format(counter) + '.jpg'
            # url = img
            img_data = requests.get(img).content
            with open(file, 'wb') as handler:
                handler.write(img_data)
        except:
                print("can't get img")

    print(succounter, "pictures succesfully downloaded")
    browser.close()

if __name__ == '__main__':

    names = ["elephant"]

    for name_i in names:
        print('Search name: ' + name_i)
        google_image_scroller(name_i)
