from system.core.router import routes

routes['default_controller'] = 'Services'
routes['POST']['/search'] = 'Services#search'
