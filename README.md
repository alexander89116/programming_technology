# programming_technology

## Task 6 - Почтовый веб-сервер


docker-compose.yml и mailu.env - конфиги. Чтобы развернуть образ, надо заменить все вхождения домена и ip-адресса на свои, тогда он развернётся. Это сделает команда:
```shell
$ docker-compose -p mailu up -d
```

#### Выполнение задания
1) Создаём droplet на https://digitalocean.com
2) Регистрируем домен на https://namecheap.com
3) Привязываем домен к DNS серверам digitalocean
4) Настраиваем DNS записи для web-интерфейса и почты
5) Устанавливаем docker и docker-compose на droplet  
    5.1. https://docs.docker.com/install/linux/docker-ce/ubuntu/

    5.2. https://docs.docker.com/compose/install/
6) Настраиваем mailu сервер https://setup.mailu.io/1.6/
7) Запускаем mailu сервер
8) Profit


#### Администрирование
https://mail.alexander89116.me/admin

Логин: admin@alexander89116.me

Пароль: PASSWORD


#### Почта
https://mail.alexander89116.me

Логин: admin@alexander89116.me

Пароль: PASSWORD
