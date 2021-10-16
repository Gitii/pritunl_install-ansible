import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_pritunl_installed(host):
    package_docker = host.package('pritunl')

    assert package_docker.is_installed


def test_pritunl_running_and_enabled(host):
    pritunl = host.service("pritunl")
    assert pritunl.is_running
    assert pritunl.is_enabled


def test_pritunl_etc_pritunl(host):
    pritunl = host.file("/etc/pritunl")
    assert pritunl.exists

    assert pritunl.contains("mongodb://")
