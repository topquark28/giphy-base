#!/usr/bin/env python

import json
import jinja2
import logging
import webapp2

from google.appengine.api import urlfetch


class MainHandler(webapp2.RequestHandler):

    def get(self):
      """Respond to HTML GET requests"""
      logging.info("===== %s.get()" % self.__class__.__name__)

      template = jinja_env.get_template('images.html')
      gifs = self.fetch_gifs()
      variables = {
        'image_urls': gifs
      }

      self.response.write(template.render(variables))

    def fetch_gifs(self):
      """Use the Giphy API to fetch several image URLs."""
      logging.info("===== %s.get()" % self.__class__.__name__)

      data_source = urlfetch.fetch("http://api.giphy.com/v1/gifs/search?q=sunset&api_key=dc6zaTOxFJmzC&limit=10")

      results = json.loads(data_source.content)
      gifs = [
        results['data'][0]['images']['original']['url'],
        results['data'][1]['images']['original']['url'],
        results['data'][2]['images']['original']['url'],
      ]
      return gifs


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', MainHandler),
]
app = webapp2.WSGIApplication(routes, debug=True)
