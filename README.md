Role Name
=========

Installs the vpn-server [pritunl](https://pritunl.com/) onto an ubuntu 20.04 (focal) server.

Requirements
------------

Supported servers:
* Ubuntu 20.04

Role Variables
--------------

* `mongodb_connection_string`: The connection string which pritunl will connect to and use as a database connection. Must include authentication & database name. Default value is `mongodb://localhost:27017/test`.
* `server_port`: The port on which pritunl will listen (web server). Default value is `8080`. 

**Remarks**: When the variable `mongodb_connection_string` value changes, the role will update the server (including `server_port`), too.  
Any changes to `server_port` alone, will not trigger an update. 

Dependencies
------------

None.

**Remarks**: Pritunl uses a `mongodb` as database. This role doesn't install `mongodb` on the target server and just tells `pritunl` to connect to one.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - pritunl_install
       mongodb_connection_string: mongodb://localhost:27017/test
       server_port: 8080
```

License
-------

MIT
