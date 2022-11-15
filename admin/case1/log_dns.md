[source](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-ubuntu-18-04-ru)


```
sudo apt install bind9

sudo ufw allow Bind9
sudo nano /etc/default/bind9
```

```
OPTIONS="-u bind -4"
```

```
sudo systemctl restart bind9

sudo nano /etc/bind/named.conf.options
```