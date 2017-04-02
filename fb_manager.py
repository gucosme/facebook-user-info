import facebook

graph = facebook.GraphAPI(access_token='184897965351508|kDKK3uVpEzGzF-x-KJnlRNXqxaI', version='2.8')

print graph.get_object(id='100003665253091', fields='gender,name')
