[source](https://www.linuxfordevices.com/tutorials/ubuntu/dhcp-server-on-ubuntu)

```
sudo apt install isc-dhcp-server
```

conf: /etc/dhcp/dhcpd.conf

backup:
```
sudo mv /etc/dhcp/dhcpd.conf{,.backup}
```

create and edit
```
sudo nano /etc/dhcp/dhcpd.conf
```

```apacheconf
# a simple /etc/dhcp/dhcpd.conf
default-lease-time 600;
max-lease-time 7200;
authoritative;

subnet 192.168.1.0 netmask 255.255.255.0 {
	range 192.168.1.100 192.168.1.200;
	option routers 192.168.1.254;
	option domain-name-servers 192.168.1.1, 192.168.1.2;
	# option domain-name "mydomain.example";
}
```