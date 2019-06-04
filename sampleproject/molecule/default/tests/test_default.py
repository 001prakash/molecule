
def test_clamav_is_installed(host):
    clamav = host.package("clamav")
    assert clamav.is_installed

def test_config_file(host):
    config_file = host.file("/etc/clamd.d/scan.conf")
    assert config_file.is_file

def test_log_file(host):
    log_file = host.file("/var/log/freshclam.log")
    assert log_file.is_file

def test_ssh_listening(host):
    host.service('ssh').is_enabled
    host.service('ssh').is_running

def test_system_info(host):
    assert host.system_info.type == 'linux'
    assert host.system_info.distribution == 'centos'
    assert host.system_info.release == '7'




