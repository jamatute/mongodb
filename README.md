# mongodb

Install mongodb with replicasets

## Requirements

None

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

To install the dependencies run:

```bash
ansible-galaxy install -r requirements.yml
```

## Example playbook

```yaml
- hosts: all
  roles:
    - mongodb
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/).

```bash
molecule test --all
```

## License

GPLv2

## Author Information
jamatute (jamatute@paradigmadigital.com)
