[source](https://blog.sedicomm.com/2016/12/16/iptables-ustanovka-i-nastrojka/)

# Последовательность действий
## Установка
Обновить информацию о пакетах, установить (либо проверить, что установлен) iptables:
```
sudo apt-get update
sudo apt-get install iptables
```
Чтобы проверить, что сетевой экран работает:
```
sudo service ufw status
```
Запустить или остановить:
```
sudo service ufw start
sudo service ufw stop
```
## Открытие портов
Для проверки откртых портов можно использовать:
```
sudo lsof -i -P -n | grep LISTEN
```
Открыть 22 порт (стандартный для SSH) для подключений по TCP:
```
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```
Подобным образом можно открыть 80 порт (стандартный для веб-серверов) для подключений по TCP:
```
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```
## Повышение безопасности
Для повышения безопасности можно перенастроить SSH на другой порт. Для этого в файле `/etc/ssh/sshd_config` нужно раскомментировать строку `#Port 22` и заменить 22 на желаемое значение (после этого нужно не забыть закрыть 22 порт и открыть новый для SSH). **После внесения изменений стоит перезапустить SSH:**
```
sudo service ssh restart
```
Дополнительно повысить безопасность сервера можно с помощью ограничения ip-адрессов, способных подключиться.

Принимать подключения с адреса {ip}/{mask}:
```
sudo iptables -A INPUT -p tcp -s {ip}/{mask} --dport 22 -j ACCEPT
```
Не принимать подключения с адреса {ip}/{mask}:
```
sudo iptables -A INPUT -p tcp -s {ip}/{mask} --dport 22 -j DROP
```
Разрешить все ip адреса и порты:
```
sudo iptables -A INPUT -p tcp -s 0/0 --dport 22 -j ACCEPT
```
## Защита от DDoS
```
sudo iptables -A INPUT -p tcp --dport 80 -m limit --limit {limit} --limit-burst {limit-burst} -j ACCEPT
```
, где:
+ limit = number/[second, minute, hour, day], например: 20/seconds
+ limit-burst = number, например: 5