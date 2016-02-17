#
import os

os.putenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT', 'true')

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Users(Model):
  firstname = columns.Text()
  age = columns.Integer()
  city = columns.Text()
  email = columns.Text()
  lastname = columns.Text(primary_key=True)

  def __repr__(self):
    return '%s %d' % (self.firstname, self.age)


from cassandra.cqlengine import connection

# Connect to the demo keyspace on our cluster running at 127.0.0.1
connection.setup(['127.0.0.1'], "demo",  protocol_version=3)

from cassandra.cqlengine.management import sync_table

# Sync your model with your cql table
sync_table(Users)

# Create a row of user info for Bob
Users.create(firstname='Bob', age=35, city='Austin', email='bob@example.com', lastname='Jones')

# Read Bob's information back and print
q=Users.get(lastname='Jones')

import ipdb; ipdb.set_trace()
print str(q)
print repr(q)

# Update Bob's age and then print to show the change
q.update(age=36)

# Delete Bob, then try to print all rows to show the user is gone
q.delete()

q=Users.objects()

for i in q: print i
