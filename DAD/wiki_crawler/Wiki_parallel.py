'''
Created on May 2017

@author: alessio ferrari
'''
from __future__ import division

import getopt
import os
import sys

import requests
import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError


API_URL = 'http://en.wikipedia.org/w/api.php'


def _wiki_request(params):
  '''
  Make a request to the Wikipedia API using the given search parameters.
  Returns a parsed dict of the JSON response.
  '''

  params['format'] = 'json'
  if not 'action' in params:
    params['action'] = 'query'

  r = requests.get(API_URL, params=params)

  return r.json()

class CategoryCrawler(object):
    
    PAGE_COUNTER = 0

    def write_page_text(self, dir, page):
        file_path = dir + "/" + page['title'].replace('/', '') + '.txt'
        if not os.path.isfile(file_path):
            try:
                txt = wikipedia.page(pageid=page['pageid']).content
                txt_file = open(file_path, "w")
                txt_file.write(txt.encode('utf-8'))
                txt_file.close()
                return True
            except AttributeError:
                print 'Error on ' + file_path + " " + str(page['pageid'])
            except PageError:
                print "Document " + str(page['pageid']) + " Not found!"
            except DisambiguationError:
                print "Disambiguation page discarded!"
        return False

    def search_and_store(self, category, subcategory_depth, path):
        '''
        Search the Wikipedia documents associated to category "category" and its subcategories up to depth
        "subcategory_depth" and store the linked documents in a folder named path.
        '''

        if self.PAGE_COUNTER >= 10000:
            quit()

        title = category if category.startswith('Category:') else 'Category:'+category
        search_params = {
            'list': 'categorymembers',
            'cmtype': 'page',
            'cmlimit': 500,
            'cmtitle': title,
        }

        page_results = _wiki_request(search_params)['query']['categorymembers']

        for page_result in page_results:
            if self.write_page_text(path, page_result):
                self.PAGE_COUNTER = self.PAGE_COUNTER + 1
                print str(self.PAGE_COUNTER) + " " + page_result['title']
                if self.PAGE_COUNTER >= 10000:
                    quit()
            else:
                print page_result['title'] + ' SKIPPED'



        if subcategory_depth > 0:
            print '################# LEVEL '+ str(subcategory_depth) + " " + title
            search_params = {
                'list': 'categorymembers',
                'cmtype': 'subcat',
                'cmlimit': 500,
                'cmtitle': title,
            }

            subcat_results = _wiki_request(search_params)['query']['categorymembers']
            #print subcat_results
            for subcat_result in subcat_results:
                self.search_and_store(subcat_result['title'], subcategory_depth-1, path)




# PATH ="../DATASETS/Computer_science_D2"
# if not os.path.exists(PATH):
#     os.makedirs(PATH)
# d = CategoryCrawler()
# d.search_and_store("Computer science", subcategory_depth=2, path=PATH)

PATH = "../DATASETS"

def main():
    portal = sys.argv[1:][0]
    limit = sys.argv[1:][1]
    
    out_path = os.path.join(PATH, portal + "_D_" + str(limit))
    
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    d = CategoryCrawler()
    d.search_and_store(portal, subcategory_depth=2, path=out_path)
 

if __name__ == "__main__":
    main()


