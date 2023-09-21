#!/usr/bin/env python
# coding: utf-8

# In[29]:

# import pyperclip
from serpapi import GoogleSearch
from urllib.parse import urlparse
import pandas as pd

# In[30]:

# Function to extract domain name from a URL
def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# In[31]:

# Function to fetch and copy organic search result links to csv file from multiple pages
def copy_organic_links_to_clipboard(query, api_key, num_pages=3):
    all_links = []

    for page in range(num_pages):
        start = page * 10  # 10 results per page
        query_params = {
            "q": query,
            "output": "json",
            "start": start,
            "api_key": api_key,
        }

        agent = GoogleSearch(query_params)
        results = agent.get_dict()

        if 'organic_results' in results:
            organic_results = results['organic_results']
            links = [result['link'] for result in organic_results if 'link' in result]
            all_links.extend(links)

    if all_links:
        # Join all the links into a single string with newlines
        links_text = "\n".join(all_links)
        # pyperclip.copy(links_text)  # Copy the links to the clipboard
        return links_text
    else:
        return "No organic search results found."

# In[32]:

# Function to compare and flag URLs based on domain name
def compare_and_flag_urls(provider_signature, dealer_urls_list, api_key):
    query = provider_signature
    copied_links = copy_organic_links_to_clipboard(query, api_key, num_pages=3)
    
    user_provided_urls = set(dealer_urls_list.split(","))
    copied_urls_from_clipboard = set(copied_links.split("\n"))
    print("User provided URLs\n")
    print(user_provided_urls)
    print(copied_urls_from_clipboard)

    # Extract domains from user provided URLs and copied URLs
    user_provided_domains = {get_domain(url) for url in user_provided_urls}
    copied_domains = {get_domain(url) for url in copied_urls_from_clipboard}
    
    urls_not_in_user_list = copied_domains - user_provided_domains
    urls_not_in_user_list1 = list(urls_not_in_user_list)

    if copied_links:
        print("\nURLs scraped from google search results:")
        print(copied_links)
    
    if urls_not_in_user_list:
        # dictionary of lists
        dict1 = {'Domain': urls_not_in_user_list1}  
        df = pd.DataFrame(dict1)
        # saving the dataframe
        df.to_csv('export_dataframe.csv', index=False)
    
    if not copied_links and not urls_not_in_user_list:
        print("\nNo URLs found or flagged.")

    return dict1
        
if __name__ == "__main__":
    compare_and_flag_urls("Copyright © 2023 by DealerOn", "https://www.demontrondchevy.com/,https://www.chandlercadillac.com/,https://www.hondacarsofaiken.com/,https://www.applevalleyford.com/,https://www.courtesymotor.net/,https://www.royalmooregmc.com/,https://www.wallacevolkswagenofkingsport.com/,https://www.applefordshakopee.com/,https://www.seacoastmazda.com/,https://www.dealeron.com/", '0b5e4f897c36375d506674c99f52907ce86b43fcaab576e0ff9f69371ad3125f')
