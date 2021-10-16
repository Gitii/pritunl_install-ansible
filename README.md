Role Name
=========

Installs the vpn-server [pritunl](https://pritunl.com/) onto an ubuntu 20.04 (focal) server.

Requirements
------------

Supported servers:
* Ubuntu 20.04

Role Variables
--------------

* `mongodb_connection_string`: The connection string which pritunl will connect to and use as a database connection. Must include authentication. Default value is `mongodb://localhost:27017/test`.
* `server_port`: The port on which pritunl will listen (web server). Default value is `8080`. 

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - pritunl
       mongodb_connection_string: mongodb://localhost:27017/test
       server_port: 8080
```

License
-------

MIT
