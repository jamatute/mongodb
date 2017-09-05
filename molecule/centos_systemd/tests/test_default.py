import os
import json
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mongod_conf(host):
    f = host.file('/etc/mongod.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_mongod_can_start(host):
    f = host.file('/var/log/mongodb/mongod.log')
    assert f.exists
    assert f.contains('waiting for connections on port')


def test_mongod_has_replicaset(host):
    out = json.loads(
        host.check_output(
            "echo 'rs.status().members.map(function(a) {return a.name});'" +
            "| mongo --quiet"))
    assert len(out) == 3
