# zabbix-supervisor
A zabbix template kit to monitor supervisord

grant permissions to zabbix user

rather than editing sudoers and providing sudo rights, 
create a dedicated unix group
```
groupadd supervisor
usermod -a -G supervisor zabbix
```

change ownership of the socket file in supervisor config

```
[unix_http_server]
file=/var/run//supervisor.sock   ; (the path to the socket file)
chmod=0770
chown=root:supervisor
```
