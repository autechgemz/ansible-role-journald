# Ansible Role: journald

## Description

Manage system service collects and stores logging data service.

## Requirements

None

## Dependencies

None

## OS Platforms

- RHEL-7/CentOS-7 or higher
- Ubuntu-18.04 or higher

## Example Playbook

```
- hosts: all
  roles:
    - journald
```

## Role Variables

### journald_debug: (bool)

```
journald_debug: false
```

### journald_service_ensure: (string)

```
journald_service_ensure: 'started'
```

### journald_service_enable: (bool)

```
journald_service_enable: true
```

### journald_config_options: (dict)

```
journald_config_options: {}
```

## Example vars

```
journald_config_options:
  Storage: 'auto'
  Compress: 'yes'
  ForwardToConsole: 'no' 
  ForwardToSyslog: 'no'
  MaxRetentionSec: '1month'
  RateLimitBurst: '10000'
  RateLimitIntervalSec: '30s'
  SyncIntervalSec: '1s'
  SystemMaxUse: '8G'
  SystemKeepFree: '20%'
  SystemMaxFileSize: '10'
```

### pytest

example:
```
$ py.test -v --hosts=all --ansible-inventory=hosts --connection=ansible  tests/journald.py 
```