# Сервис поиска ближайших машин для перевозки грузов

[Тестовое задание](https://faint-adasaurus-4bc.notion.site/web-Python-3682ad009f2a43589f7fdb1d2e0ed312)

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание](#описание)
- [Установка](#установка)
- [Запуск](#запуск)
- [Автор](#автор)

<br>

## Технологии

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![psycopg2](https://img.shields.io/badge/-psycopg2-464646?logo=psycopg2)](https://pypi.org/project/psycopg2/)
[![geopy](https://img.shields.io/badge/-geopy-464646?logo=psycopg2)](https://pypi.org/project/geopy/)
[![docker](https://img.shields.io/badge/-Docker-464646?logo=docker)](https://www.docker.com/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)




[⬆️Оглавление](#оглавление)

<br>

## Описание

При запуске приложения БД инициализируется следующими данными:

1. Список уникальных локаций, представленых в csv файле "uszips.csv". Каждая локация содержит в себе следующие характеристики:
   - почтовый индекс (zip)
   - широта
   - долгота
   - город
   - название штата
2. Список из 20 машин. Каждая машина - включает следующие характеристики:
   - уникальный номер (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце, пример: "1234A", "2534B", "9999Z")
   - текущая локация
   - грузоподъемность (1-1000). При создании машин по умолчанию локация каждой машины заполняется случайным образом

Сервис поддерживает следующие функции:

   - Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду).
   - Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль)).
   - Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза).
   - Редактирование машины по ID (локация (определяется по введенному zip-коду)).
   - Редактирование груза по ID (вес, описание).
   - Удаление груза по ID.


[⬆️Оглавление](#оглавление)

<br>

## Установка

Клонируйте репозиторий с GitHub:

```bash
git clone https://github.com/Shone-Kristas/Service-to-search-cars-nearby.git
```

Подразумевается, что на локальной машине, или на удаленном сервере, уже установлены Docker и Docker Compose.

[⬆️Оглавление](#оглавление)

<br>

## Запуск

Из корневой директории проекта "car_search" выполните команду:
```bash
docker compose up
```
* Сервис должен быть запущен [http://localhost:8080/](http://localhost:8080/)

[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Nickolay](https://github.com/Shone-Kristas)

[⬆️В начало](#Сервис-поиска-ближайших-машин-для-перевозки-грузов)
