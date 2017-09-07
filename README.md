# mongodb

Install mongodb with replicasets

## Requirements

If you don't specify the admin password for mongodb you'll need `passlib`
installed.

```bash
pip install passlib
```

## Role Variables

* `mongod`: Dictionary with information of mongo
  * `version`: (Default: 3.4)
  * `db_path`: (Default: "/var/lib/mongo")
  * `log_path`: (Default: "/var/log/mongodb/mongod.log")
  * `pid_file`: (Default: "/var/run/mongodb/mongod.pid")
  * `journal`: (Default: 'true')
  * `port`: (Default: 27017)
  * `keyfile`: (Default: )/data/security.key)
  * `admin_user`: **Please change this** (Default: admin)
  * `admin_password`: **Please change this** (Default: nimda)

## Dependencies

Not yet

## Example playbook

```yaml
- hosts: all
  roles:
    - mongodb
```

## License

GPLv2

## Author Information
jamatute (jamatute@paradigmadigital.com)
