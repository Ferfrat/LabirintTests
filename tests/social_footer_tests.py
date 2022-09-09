import time
from Pages.main_page import Pages

def test_link_vk(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'ВКонтакте'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_link_vk_kids(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'ВКонтакте.Дети'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_link_youtube(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Ютьюб'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_link_classmates(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Одноклассники'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_classmates.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_link_zen(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Дзен'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_zen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_link_t_me(web_browser):
    """Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Телеграм'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_t_me.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://t.me/labirintru'


