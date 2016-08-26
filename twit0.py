from TwitterAPI import TwitterAPI
consumer_key = ''
consumer_secret = ''
api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
response= api.request( 'users/show', {'screen_name':'tiger'} )
print( "status", response.status_code )
print( "headers", response.headers )
import json
print( json.dumps(response.json(), indent=2) )

