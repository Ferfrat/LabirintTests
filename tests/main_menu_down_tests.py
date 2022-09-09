import time
from Pages.main_page import Pages


def test_button_help(web_browser):
    """Тестируем кнопку 'Доставка и оплата'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_help.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_button_top(web_browser):
    """Тестируем кнопку 'Сертификаты'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_top.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_button_rat(web_browser):
    """Тестируем кнопку 'Рейтинги'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_rating.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_button_nov(web_browser):
    """Тестируем кнопку 'Новинки'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_novelty.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_button_sale(web_browser):
    """Тестируем кнопку 'Скидки'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_sale.click()

    assert page.get_current_url() == 'https://www.labirint.ru/sale/'


def test_button_all_cont(web_browser):
    """Тестируем кнопку 'Контакты'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_all_contact.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_button_supp(web_browser):
    """Тестируем кнопку 'Поддержка'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_button_all_maps(web_browser):
    """Тестируем кнопку 'N-ое кол-во пунктов самовывоза'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_all_maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'
