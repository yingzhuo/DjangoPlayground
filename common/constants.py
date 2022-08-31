# JWT签名KEY
from django_sugar.web import jwtalg

JWT_SECRET_KEY = jwtalg.HmacAlgorithm('HS384', key='DjangoPlayground')
