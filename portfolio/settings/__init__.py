import os

ENV = os.getenv('PORTFOLIO_ENV', 'dev')

if ENV == 'dev':
    from .dev import *
elif ENV == 'prod':
    from .production import *
