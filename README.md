Prerequisites:Python 3.7.4
Установка драйверов браузера (обратить внимание на версию браузера и подобрать подходящую версию драйвера):

chromedriver: 
 - https://chromedriver.chromium.org/downloads

geckodriver(firefox):
 - https://github.com/mozilla/geckodriver/releases/
 
Установка Allure:
 brew install allure

Установка проекта
1. Скачать проект и запустить его
2. Открыть терминал в папке проекта и создать виртуальное окружение - python3 -m venv venv
3. Активировать виртальное окружение - source venv/bin/activate
4. Обновить pip - pip install -U pip
5. Установить зависимости из файла requirements.txt - pip install -r requirements.txt
6. Установить ffmpeg - brew install ffmpeg
6. Запуск тестов: 
  
  pytest - прогнать все тесты
  
  pytest --alluredir allure-report - (ПРЕДПОЧИТАЕМЫЙ)прогнать все тесты с отчетом в allure, для просмотра отчета нужна команда allure serve allure-report
  
  pytest -m "tag" - прогнать все тесты с tag. tag == "smoke" - теги будут появляться с увелечением кол-ва тестов 

## Python Runner V2

Запускаем allure и selenium-hub с хромом:

```docker-compose up -d```

Запускаем тесты:

```docker-compose run pytest-runner bash -c 'cd /src && pytest --alluredir=allure-results'```

Смотрим результаты в allure:

http://localhost:5252/

Стенд, на который ходят тесты, указываем в docker-compose.override.yml:

```
version: "3.9"

services:
  pytest-runner:
    environment:
      - CORE_RPC_HOST_EXTERNAL=https://test-stand-01.midhub.org/
      - NOTARY_WEB_HOST_EXTERNAL=https://test-stand-01.midhub.org/
```

Для запуска с локальным солюшеном, используйте при подъёме флаг --for-tests

Доступ к UI приложения получаем через VNC Viewer. Для установки - https://www.realvnc.com/en/connect/download/viewer/macos/
При запуске VNC необходимо указать URL и порт контейнера с браузером - `localhost:9001` и ввести логин и пароль.
После чего необходимо запустить браузер с нужными флагами из env переменной - CHROME_STRING.
 - для этого в VNC запустить командую строку и ввести команду - `google_chrome $CHROME_STRING`.
 - запусться браузер.
