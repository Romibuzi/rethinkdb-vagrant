# RethinkDB using Vagrant

Install [RethinkDB](http://rethinkdb.com) using [Vagrant](http://vagrantup.com).

## Quick Start -- One Liner

```bash
git clone git://github.com/romibuzi/rethinkdb-vagrant.git && cd rethinkdb-vagrant && vagrant up
```

# (optional) Populate some fake users data under `test` database in `users` table
```bash
vagrant ssh && cd rethinkdb && ./load_fake_data.py
```

## RethinkDB Dashboard

By default, you access the dashboard here:
[http://localhost:8080/](http://localhost:8080/)
