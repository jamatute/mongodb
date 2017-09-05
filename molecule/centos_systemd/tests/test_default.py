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
    # assert f.contains('keyFile:')


def test_mongod_can_start(host):
    f = host.file('/var/log/mongodb/mongod.log')
    assert f.exists
    assert f.contains('waiting for connections on port')


def test_mongod_has_replicaset(host):
    members = json.loads(
        host.check_output(
            "echo 'rs.status().members.map(function(a) {return a.name});'" +
            "| mongo --quiet"))
    assert len(members) == 3


def test_mongod_has_root_user(host):

    def str2bool(v):
        return str(v).lower() in ("yes", "true", "t", "1")

    is_master = host.check_output(
        "echo 'rs.isMaster().ismaster' | mongo --quiet")

    raise TypeError(
        'is_master: {}, type: {}'.format(is_master, type(is_master)) +
        'bool: {}, type: {}'.format(bool(is_master), type(bool(is_master))) +
        'b: {}, type: {}'.format(str2bool(is_master),
                                 type(str2bool(is_master)))
    )

    if is_master:
        has_admin = json.loads(
            host.check_output(
                "echo 'db.system.users.find({user: \"admin\"}).count()' " +
                "| mongo --quiet admin"))
        assert has_admin == 1


# def test_mongod_keyfile(host):
#     f = host.file('/var/lib/mongo/security.key')
#     assert f.exists
#     assert f.user == 'mongod'
#     assert f.group == 'mongod'
#     assert oct(f.mode) == '0600'
