'''
Created on genn 2017

@author: beatrice donati
'''
from __future__ import division

import os
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
                #self.logger.exception("Document " + str(pageid) + " Not found!")
                print "Document " + str(page['pageid']) + " Not found!"
            except DisambiguationError:
                #self.logger.exception("Disambiguation page discarded!")
                print "Disambiguation page discarded!"
        return False

    def search_and_store(self, category, subcategory_depth, path):
        '''
        Search the Wikipedia documents associated to category "category" and its subcategories up to depth
        "subcategory_depth" and store the linked documents in a folder named path.
        '''

        title = category if category.startswith('Category:') else 'Category:'+category
        search_params = {
            'list': 'categorymembers',
            'cmtype': 'page',
            'cmtitle': title,
        }

        page_results = _wiki_request(search_params)['query']['categorymembers']
        
        for page_result in page_results:
            if self.write_page_text(path, page_result):
                print page_result['title']
            else:
                print page_result['title'] + ' SKIPPED'



        if subcategory_depth > 0:
            print '################# LEVEL '+ str(subcategory_depth)
            search_params = {
                'list': 'categorymembers',
                'cmtype': 'subcat',
                'cmtitle': title,
            }

            subcat_results = _wiki_request(search_params)['query']['categorymembers']
            for subcat_result in subcat_results:
                self.search_and_store(subcat_result['title'], subcategory_depth-1, path)




PATH ="../DATASETS/Medicine"
if not os.path.exists(PATH):
    os.makedirs(PATH)
d = CategoryCrawler()
d.search_and_store("Medicine", subcategory_depth=5, path=PATH)