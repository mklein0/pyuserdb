#

from cassandra.cluster import Cluster
cluster = Cluster(
    contact_points=['127.0.0.1'],
    load_balancing_policy= TokenAwarePolicy(DCAwareRoundRobinPolicy(local_dc='datacenter1')),
    default_retry_policy=RetryPolicy(),
)
session = cluster.connect('demo')

session.execute("""

insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')

""")


result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age

session.execute("update users set age = 36 where lastname = 'Jones'")
result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age

session.execute("delete from users where lastname = 'Jones'")
result = session.execute("select * from users")
for x in result: print x.age
