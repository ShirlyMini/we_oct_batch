from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_ops = webdriver.ChromeOptions()
# chrome_ops.add_argument('--headless')
#https://peter.sh/experiments/chromium-command-line-switches/


chrome_ops.add_argument('--start-maximized')
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_ops)

driver.get("https://money.rediff.com/gainers")

# print(driver.get_cookies())
# print(len(driver.get_cookies()))
# for cookie in driver.get_cookies():
#     print(cookie['domain'])
#     print(cookie['name'])
#     print(cookie['value'])



# [{'domain': '.rediff.com', 'expiry': 1741531146, 'httpOnly': False, 'name': '_col_uuid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '8d14e8a5-4a0f-4a11-bc04-0b322de0820e-10ofk'}, {'domain': '.rediff.com', 'expiry': 1722523143, 'httpOnly': False, 'name': '__eoi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=5c789903be225b74:T=1706971143:RT=1706971143:S=AA-AfjZ8amFKN_wvWKiwnhVXe2vC'},
# {'domain': '.rediff.com', 'expiry': 1738507145, 'httpOnly': False, 'name': 'connectId', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '{"ttl":86400000,"lastUsed":1706971145272,"lastSynced":1706971145272}'}, {'domain': '.rediff.com', 'expiry': 1740667143, 'httpOnly': False, 'name': '__gpi', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'UID=00000cf7a0f4a6f5:T=1706971143:RT=1706971143:S=ALNI_MYO7472TbHDoWrcQHVFLcQbQneMUA'},
# {'domain': '.rediff.com', 'expiry': 1740667146, 'httpOnly': False, 'name': 'cto_bundle', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2y_AI19HJTJCSjY0diUyQjJPYmFPWmRxQTEydWVkU3dXUXhUeURITlFWbXJWTU1zQlJTNDNIcElNS1FEYjRPdGtxSnRGZ0VaUWhBTXBRS2FnRDNLa0FyY255QzBWemNIJTJCaVROUG1qWHQzMkZ4Q2hqUkJsUlRUJTJCR2pqbGtwb0FNQkQlMkZBTjRTMkp0ZSUyRjglMkYlMkJiRDZHJTJCU0RBQ3VDY2pCOUElM0QlM0Q'}, {'domain': '.rediff.com', 'expiry': 1740667143, 'httpOnly': False, 'name': '__gads', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ID=902573e9d741187d:T=1706971143:RT=1706971143:S=ALNI_MY6kibHD6OVh3n-m7hveb67d9Puvg'},
# {'domain': '.rediff.com', 'expiry': 1707057544, 'httpOnly': False, 'name': 'panoramaId_expiry', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1707057543457'}, {'domain': '.rediff.com', 'expiry': 1706971154, 'httpOnly': False, 'name': 'lotame_domain_check', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'rediff.com'}, {'domain': '.rediff.com', 'expiry': 1730299145, 'httpOnly': False, 'name': '_cc_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '66b74e12536dcfd6e0cb2b2cab775055'}, {'domain': '.rediff.com', 'expiry': 1741531143, 'httpOnly': False, 'name': 'RuW', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'a998838.6107b308a9bc3'}, {'domain': '.money.rediff.com', 'expiry': 1707057542, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.306539929.1706971142'}, {'domain': 'money.rediff.com', 'httpOnly': False, 'name': 'pbjs_debug', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'null'}, {'domain': '.money.rediff.com', 'expiry': 1741531142, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1816586329.1706971142'}]



#{'domain': '.rediff.com', 'expiry': 1707057544, 'httpOnly': False, 'name': 'panoramaId_expiry', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1707057543457'}



driver.add_cookie({'name':'mycookie', 'value':'123456kxslkm'})
print(driver.get_cookie('mycookie'))

driver.delete_cookie('mycookie')
print(driver.get_cookie('mycookie'))
driver.delete_all_cookies()
print(driver.get_cookies())

driver.quit()