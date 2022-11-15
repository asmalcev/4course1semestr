[source](https://linuxize.com/post/how-to-install-and-configure-samba-on-ubuntu-18-04/)

# Установка и настройка
```
sudo apt install samba
sudo systemctl status smbd

sudo ufw allow 'Samba'

sudo cp /etc/samba/smb.conf{,.backup}

sudo mkdir /samba
sudo chgrp sambashare /samba



sudo useradd -M -d /samba/caseuser -s /usr/sbin/nologin -G sambashare caseuser

sudo mkdir /samba/caseuser
sudo chown caseuser:sambashare /samba/caseuser

sudo chmod 2770 /samba/caseuser

sudo smbpasswd -a caseuser
[password=caseuserpass]

sudo smbpasswd -e caseuser



sudo useradd -M -d /samba/users -s /usr/sbin/nologin -G sambashare sadmin

sudo smbpasswd -a sadmin
[password=caseadminpass]

sudo smbpasswd -e sadmin



sudo mkdir /samba/users

sudo chown sadmin:sambashare /samba/users

sudo chmod 2770 /samba/users
```
change conf
```
sudo nano /etc/samba/smb.conf
```
content:
```
[users]
    path = /samba/users
    browseable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @sambashare @sadmin

[caseuser]
    path = /samba/caseuser
    browseable = no
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = caseuser @sadmin
```

```
sudo systemctl restart smbd
sudo systemctl restart nmbd
```

# Тестирование
```
sudo apt install smbclient

smbclient //host-ip/caseuser -U caseuser
[password=caseuserpass]
```