import time
from Pages.main_page import Pages


def test_button_mess(web_browser):
    """Тестируем кнопку 'Сообщения'.Ожидаем переход на соответствующую страницу'.
    page = Pages(web_browser)
    page.button_postponed.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


def test_button_mlab(web_browser):
    """Тестируем кнопку 'Мой Лабиринт'.Ожидаем переход на соответствующую страницу'.
    page = Pages(web_browser)
    page.button_postponed.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


def test_button_post(web_browser):
    """Тестируем кнопку 'Отложено'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_postponed.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_button_cart(web_browser):
    """Тестируем кнопку 'Корзина'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


def test_book_buy(web_browser):
    """Добавление книги в корзину."""
    page = Pages(web_browser)
    page.buy.click()
    time.sleep(10)

    assert page.message_book_buy
