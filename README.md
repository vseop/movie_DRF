## API фильмотеки (DRF)
### Функционал
* Аутентификация по токенам  (djoser).
* Фильтрация по жанрам и годам (django-filter).
* Автодокументирование swagger (application.yasg).
* Настройка админ панели (TabularInline, ckeditor, actions, группировка, вывод изображения и т.д.)
* Рекурсивный вывод комментариев (movies.serializers.RecursiveSerializer).
* Возможность добавления permission в зависимости от action (типа запроса) в аттрибут permission_classes_by_action , подмешивая написанный mixin (movies.classes.MixedPermission).
* Реализован свой action для возможности просматривать свои комментарии.
* Пагинация (movies.service.PaginationMovies)
* Рейтинг фильма - выставлять, смотреть средний
* Доступ доменов к backend (corsheaders)

### Установка и запуск
1) docker-compose up -d (запуск postgres в фоновом режиме)
2) pip install -r requirements.txt 
3) cd django_movie && python manage.py makemigrations 
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver

