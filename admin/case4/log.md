[source](https://blog.sedicomm.com/2019/10/21/kak-ustanovit-server-openldap-dlya-tsentralizovannoj-autentifikatsii/)

```
sudo apt install slapd ldap-utils
[password=caseadmin]

sudo systemctl status slapd

sudo ufw allow ldap
sudo dpkg-reconfigure slapd

sudo tree /etc/ldap/slapd.d/
```