from datetime import datetime
from uuid import uuid4

post = {}
post['title'] = raw_input('Title: ')
post['slug'] = post['title'].lower().replace(' ', '-')
post['date'] = datetime.now().strftime('%Y-%m-%d')
post['time'] = datetime.now().strftime('%H:%M')

header = """Title: %(title)s
Date: %(date)s %(time)s
Slug: %(slug)s
Categories: 
""" % (post)

out_file = 'content/blog/%s.md' % (post['slug'])

try:
    with open(out_file) as f:
        out_file = 'content/blog/%s.md' % (uuid4())
        print('The specified output file exists. Writing to %s' % out_file)
except:
    pass

with open(out_file, 'w') as f:
    f.write(header)
