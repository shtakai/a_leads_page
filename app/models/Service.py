from system.core.model import Model
import re
import bcrypt
from math import ceil

class Service(Model):
    def __init__(self):
        super(Service, self).__init__()

    def get_all_services(self):
        query = 'select * from services order by updated_at desc'
        services_result = self.db.query_db(query, {})

        print 'service_result', service_result
        return {
                'status': True,
                'result': service_result
                }

    def get_leads(self, req):
        print 'get_leads', req
        errors   = []
        infos    = []
        offset   = req['page_number'] if req.get('page_number') else 1
        per_page = 5
        # NOTE: This case, name connects only first_name
        name = req['name'] if req.get('name')  else ''
        from_date =  req['from_date'] if req.get('from_date') else ''
        to_date   = req['to_date'] if req.get('to_date') else ''
        print 'name_query', name
        print 'from_date', from_date
        print 'to_date', to_date
        query = 'select * from leads where'
        count_query = 'select count(*) as count from leads where'
        if req.get('name'):
            query += ' first_name like :name '
            count_query += ' first_name like :name '
        else:
            query += ' 1 '
            count_query += ' 1 '

        if req.get('from_date'):
            query += ' and created_at >=:from_date'
            count_query += ' and created_at >=:from_date'
        else:
            query += ' and 1 '
            count_query += ' and 1 '

        if req.get('to_date'):
            query += ' and created_at <= :to_date '
            count_query += ' and created_at <= :to_date '
        else:
            query += ' and 1 '
            count_query += ' and 1 '

        query += ' order by id limit :start, :show'
        values = {
                'name'      : '%' + name +'%',
                'from_date' : from_date.replace("/", "-"),
                'to_date'   : to_date,
                'start'     : (int(offset) - 1) * per_page,
                'show'      : per_page
                }
        print 'query', query
        print 'count_query', count_query
        print 'values', values
        leads_result = self.db.query_db(query, values)
        count_result = self.db.query_db(count_query, values)
        pages = int(ceil(count_result[0]['count'] / float(per_page)))
        print 'leads_result', leads_result
        print 'count_result', count_result
        print 'pages', pages
        return {
                'status': True,
                'errors': errors,
                'infos': infos,
                'result': leads_result,
                'pages': pages,
                'page_number': offset,
                'search_form': req
                }
