# mlink

## Задание 1

Написать сервис аналог [https://bitly.com/](https://bitly.com/) Сервис должен иметь простой веб интерфейс - одна страница  с одним полем для ввода ссылки на ресурс, которую нужно минифицировать, и кнопка “отправить”. После отправки данных сервис должен возвращать короткую ссылку. Если полная ссылка на ресурс уже была раньше обработана, то показать так же короткую ссылку и количество переходов по ней. При переходе по короткой ссылке, сервис должен перенаправить на ресурс, используя полную ссылку. Необходимо учесть, что для одинаковых ссылок (исходных) от разных людей переходы должны учитываться раздельно.Обязательно использование ORM и тестов.
# Project
Django, ORM, unittest

## Quickstart
- clone the repository and cd folder project
- create virtualenv `virtualenv venv`.
- activate virtualenv.
- install requirements: `pip intstall -r requirements.txt`
- make migrations `python manage.py migrate`
- run server `python manage.py runserver`

## application

creaet link. Main Page.
![image](https://user-images.githubusercontent.com/52758126/210406281-00ee8155-b416-46fd-9942-689a85efc7fd.png)

Detail about shorted link
![image](https://user-images.githubusercontent.com/52758126/210407771-d31475b7-f911-4b48-881d-15e0de47f5c2.png)

Link for redirect
![image](https://user-images.githubusercontent.com/52758126/210408005-0251fb14-280c-4533-beca-b1294fbc2337.png)


- we created link and then try create new link with the equal prev link so we get prev link
- the count open is not counted as the number of link opens. count open is individual open link seperate customer.
