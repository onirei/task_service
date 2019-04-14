# Список заявок

Небольшое приложение для организации отображения списка существующих на сервере заявок пользователя. Приложение написано на языке Python с использованием Django.

# Используемые технологии

+ Python 3.7
+ Django 2.1.3
+ Django REST Framework 3.9.2

## Приложение включает в себя следующие страницы:

1. Страница создания и редактирования заявки содержащая следующие поля (атрибуты), задаваемые пользователем:
    + Название – текстовое поле, не более 64 символов.
    + Изображение – возможность upload-а и прикрепления изображения к заявке.
    + Полнотекстовое описание – большой блок текста, с поддержкой форматирования.
    + Дата завершения – возможность выбора даты с помощью date-picker-а, дата не может быть меньше чем <сегодня>. 
    + Статус – возможность выбора и указания статуса из списка предопределенных статусов:
        + Open
        + Needs offer
        + Offered
        + Approved
        + In progress
        + Ready
        + Verified
        + Closed

2.	Страница просмотра списка заявок. На ней отображаться таблица, содержащая все заявки. Таблица должна поддерживает пагинацию и возможность сортировки по любой из колонок. Колонки таблицы: 
    + Название
    + Дата создания
    + Дата завершения
    + Статус

3.	Страница подробного просмотра заявки отображает полную информация по заявке, включает все атрибуты:
    + Название
    + Изображение
    + Полнотекстовое описание
    + Дата создания
    + Дата завершения
    + Статус

# API
Реализованы методы REST API для работы с заявками.
1. Метод возвращения списка заявок.
В параметре start - указывается номер с которого будут выводиться заявки, в count - количество выводимых заявок. Данные параметры являются обязательными.
    ```python
    requests.get('http://localhost:8000/api/snippets/', params={'start':<int>, 'count':<int>})
    ```
2. Метод возвращения заявоки.
    В параметре int указывается id заявки.
    ```python
    requests.get('http://localhost:8000/api/snippets/<int>')
    ```
3. Метод загрузки изображения.
    Параметр image принимает путь к файлу. Данный метод после сохранения изображения возвращает его имя для для последующей загрузки.
    ```python
    requests.post('http://localhost:8000/api/upload/<format>', files={'file':open(<image>', 'br')})
    ```
3. Метод создания заявки.
    Параметр str принимает строку, параметр date принимает дату формата yyyy-mm-dd, параметр image принимает имя изображения из 3 метода. Параметры name, about, expiration date являются обязательными.
    ```python
    requests.post('http://localhost:8000/snippets/', data={'name':<str>,'about':<str>,'expiration_date':<date>, 'status':<str>', 'img_file':<image>})
    ```
4. Метод обновления заявки.
    Параметр int принимает id заявки, str принимает строку, параметр date принимает дату формата yyyy-mm-dd, параметр image принимает имя изображения из 3 метода. Параметры name, about, expiration date являются обязательными.
    ```python
    requests.put('http://localhost:8000/snippets/<int>/', data={'name':<str>,'about':<str>,'expiration_date':<date>, 'status':<str>', 'img_file':<image>})
    ```
5. Метод удаления заявки.
    В параметре int указывается id заявки.
    ```python
    requests.delete('http://localhost:8000/snippets/<int>')
    ```