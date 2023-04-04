import allure
from allure_commons.types import AttachmentType


def logs(browser):
    try:
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(body=log,
                      name='browser_logs_' + browser.driver.session_id,
                      attachment_type=AttachmentType.TEXT,
                      extension='.log')
    except Exception:
        pass


def html(browser):
    html = browser.driver.page_source
    allure.attach(body=html,
                  name='page_source_' + browser.driver.session_id,
                  attachment_type=AttachmentType.HTML,
                  extension='.html')
