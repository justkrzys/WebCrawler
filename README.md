# Web Crawler
Searches the internet for e-mail addresses for the defined amount of websites.

## Usage
To use this program, the user will call the crawl() function with a starting URL and an integer limit, respectively. The program will go through the website, collecting all URLS and e-mails present in the website's HTML. The program will visit the first URL found in the HTML and continue to collect e-mails and URLS until it has visited all possible websites reachable from the sites it has visited or until it has searched <limit> number of websites.
