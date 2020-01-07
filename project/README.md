Task:
Есть папка. В папке постепенно появляются JSON файлы. В файле объект звонка со следующими полями: номер того, кто звонил (строка), номер того, кому звонили (строка), время начала звонка (Unix timestamp), время окончания звонка (Unix timestamp), тип связи (строка, одно из (GSM, CDMA, LTE)). 

Есть БД. Две сущности: тарифный план и звонок. Тарифный план состоит из следующих атрибутов: тип связи и цена за минуту разговора (в неделимых единицах, например, в копейках, может быть просто целым положительным числом). 
Звонок состоит из следующих атрибутов: номер того, кто звонил, номер того, кому звонили, время начала звонка, время окончания звонка, стоимость звонка. 

Задача: написать сервис (EDI), который следит за тем, как появляются файлы звонков в каталоге. Как только появляется файл со звонком, он его читает, парсит, считает стоимость для соответствующего типа связи и записывает в базу и, если все ок с записью, файл удаляет.

Помимо этого есть простой REST API с одним методом:
1) GET /call с параметром number который возвращает все звонки (2 номера, время начала/конца, стоимость), в которых участвовал номер из параметра (то есть и входящие, и исходящие). Данные брать из БД. Формат данных: JSON

Техонологии: python 3, любая реляционная СУБД (например, MySQL), API на последнем flask (1.1.x)

Setting up database:
1. Install Postgresql https://www.postgresql.org/download/
2. Create database named 'calls' from sql dump file(calls.sql). (run 'psql calls < calls.sql' in command line. Beware: calls must be created before importing.)

Setting up virtual environment:
1. Run 'pip install virtualenv' 
2. Run 'virtualenv env'
3. MacOS/Linux: Run 'source env/bin/activate'
   Windows: Run 'env\Scripts\activate'
4. Run 'pip install -r requirements.txt'

Run directory watcher: 
1. Change current working directory to project\Services.
2. Run 'python watcher.py' in command line. (If problem appears, just re-run this script.)

Run api:
1. Change current working directory to project\api.
2. Run 'python run.py' in command line.
3. Go to the http://127.0.0.1:5000/api/calls in browser to get info about all calls.
4. Go to the http://127.0.0.1:5000/api/calls/<call_number> in browser to get info about calls in which call_number was involved.