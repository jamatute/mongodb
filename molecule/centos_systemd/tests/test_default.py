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
    assert f.contains('keyFile:')


def test_mongod_can_start(host):
    f = host.file('/var/log/mongodb/mongod.log')
    assert f.exists
    assert f.contains('waiting for connections on port')


def test_mongod_has_replicaset(host):
    members = json.loads(
        host.check_output(
            "echo 'rs.status().members.map(function(a) {return a.name});'" +
            "| mongo --quiet -u admin -p nimda admin"))
    assert len(members) == 3


def test_mongod_has_root_user(host):

    def str2bool(v):
        return str(v).lower() in ("yes", "true", "t", "1")

    is_master = str2bool(host.check_output(
        "echo 'rs.isMaster().ismaster' | mongo --quiet"))

    if is_master:
        has_admin = json.loads(
            host.check_output(
                "echo 'db.system.users.find({user: \"admin\"}).count()' " +
                "| mongo --quiet -u admin -p nimda admin"))
        assert has_admin == 1


def test_mongod_keyfile(host):
    f = host.file('/var/lib/mongo/security.key')
    assert f.exists
    assert f.user == 'mongod'
    assert f.group == 'mongod'
    assert oct(f.mode) == '0600'


def test_template_files_doesnt_exist(host):
    templates = ['/tmp/create_root.js', '/tmp/replicaset.js']
    for filename in templates:
        f = host.file(filename)
        assert not f.exists
