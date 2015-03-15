#!/usr/bin/env python

from faker import Factory
import rethinkdb as r


RETHINK_HOST = 'localhost'
RETHINK_PORT = 28015


def load_fake_data(records_number):
    conn = r.connect(host=RETHINK_HOST, port=RETHINK_PORT)

    db_list = r.db_list().run(conn)
    if 'test' not in db_list:
        r.db_create('test').run(conn)

    table_list = r.db('test').table_list().run(conn)
    if 'users' not in table_list:
        r.db('test').table_create('users').run(conn)

    fake = Factory.create('fr_FR')
    for _ in range(0, records_number):
        record = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'country': fake.country(),
            'birth_date': fake.date_time().strftime('%Y-%m-%d'),
        }
        r.db('test').table('users').insert(record).run(conn)

    print('done : %d fake users inserted' % records_number)

if __name__ == '__main__':
    # Create 500 users by default
    load_fake_data(500)
