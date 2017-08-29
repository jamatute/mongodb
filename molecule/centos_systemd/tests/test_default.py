import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mongod_db_path(host):
    f = host.file('/data/mongod/')
    assert f.exists
    assert f.user == 'mongod'
    assert f.group == 'mongod'
    assert oct(f.mode) == '0770'


def test_mongod_conf(host):
    f = host.file('/etc/mongod.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0660'


def test_mongod_can_start(host):
    f = host.file('/var/log/mongodb/mongod.log')
    assert f.exists
    assert f.contains('[initandlisten] waiting for connections on port')
