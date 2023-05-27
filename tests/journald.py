
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky", "almalinux"]
    assert host.system_info.arch == 'x86_64' 

def test_installed(host):
    systemd = host.package("systemd")
    assert systemd.is_installed

def test_config(host):
    journald_config = host.file("/etc/systemd/journald.conf")
    assert journald_config.user == "root"
    assert journald_config.group == "root" 
    assert journald_config.mode == 0o644

def test_running_and_enabled(host):
    journald = host.service("systemd-journald")
    assert journald.is_running
    assert journald.is_enabled
