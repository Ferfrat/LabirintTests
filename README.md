<b>Задание</b>

Вам необходимо выбрать любой сайт интернет-магазина и написать для него 50-70 автоматизированных тестов с использованием PyTest и Selenium.

Веб-сайты магазинов на ваш выбор:

- Ozon,<br>
- Tmall, <br>
- Labirint.

Или любой сайт интернет-магазина, в котором есть большое количество товаров, а также функционал поиска и сортировки / фильтрации товаров.<br>

Тестовые сценарии для интернет-магазина <a href="http://www.labirint.ru">Labirint.ru"</a>.

Файлы:
Папка <b>tests</b>:

     main_menu_center_up_tests.py - тесты центрального меню верхнего в шапке главной страницы
     
     main_menu_down_tests.py - тесты центрального меню нижнего в шапке главной страницы
     
     main_menu_right_tests.py - тесты кнопок справа в шапке главной страницы
     
     social_footer_tests.py - тесты ссылок на социальные сети в подвале на главной странице
     
     books_tests.py - тесты центральных кнопок в теле страницы "Книги" и переходов на последующие страницы

Папка <b>Pages</b>:

     base.py содержит библиотеку Smart Page Object
     
     books_page.py содержит класс для страницы "Книги"
     
     elements.py содержит класс для определения элементов на веб-страницах
     
     main_page.py содержит класс для "Главной страницы"


Запуск тестов:

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/books_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_center_up_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_down_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_right_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/social_footer_tests.py
