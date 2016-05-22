from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re
import settings

class Services(Controller):
    def __init__(self, action):
        super(Services, self).__init__(action)
        self.load_model('Service')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        return self.load_view('/index.html', page_number=1)

    def search(self):
        print 'Services#search', request.form
        leads_result = self.models['Service'].get_leads(request.form)
        print 'leads_result', leads_result
        return self.load_view('/index.html', page_number=leads_result['page_number'], pages=leads_result['pages'], leads=leads_result['result'], search_form=leads_result['search_form'])

        # origin = request.form['from']
        # destination = request.form['dest']
        # data = {
                # 'origin': origin,
                # 'destination': destination
                # }
        # url = "https://maps.googleapis.com/maps/api/directions/json?"+urlencode(data)+"&sensor=false&key=" + settings.env()['KEY']
        # print 'url', url
        # # notice this is 'requests' not 'request'
        # # we are using the request modules, 'get' function to send a request from our controller
        # # then we use ".content" to get the content we are looking for
        # response = requests.get(url).content
        # print 'response', response
        # we then send the response back to our client which sent the initial post request
        # return response
        pass
