# Research paper web scraper
> Here is a simple web scraper program I wrote to scrape PubMed data. You can use it for Google Scholar or any other journal source. You will need to find the CSS elements corresponding to the page you are scraping and add your own header to gain access.


## How to target the title, abstract, or keywords of another page not PubMed

-  Use browser dev tools the find the selectors of the element you are targeting and want to scrape the title
- if targeting CSS directly change this ```response.xpath('//ADD_ELEMENT_NAME HERE_AND _NESTED_PATH/text()').get()```
-  If you want to use ```xpath``` then use dev-tools, right click on element, go to copy, and select ```copy xpath`` place it in the response to target the element.```  ```response.xpath('//ADD_YOU_XPATH_HERE/text()')```
-

# How to run
-  clone or copy project to your desktop-app
-  open project in your IDE ``` I used VS code```
- make sure you are using at least python3.9 interpreter.
- activate virtual environment by running this in a command line terminal ```!!!Do not use bash!!!```  run ```.\venv\Scripts\activate```
- install all packages from ```requirements.txt``` by using a terminal and running this command ```pip install -r requirements.txt.```
- open a terminal in your IDE and run the script ```python getAbstract.py``` or any of the other scripts of your choice.


----------------------------------------------------------------

Feel free to change and add to this project.