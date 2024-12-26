from patchright.sync_api import sync_playwright
import random, threading, time

url = 'https://ptp.today/144782'
#urllist = ["https://ptp.today/144782","https://ptp.today/145341","https://ptp.today/145342","https://ptp.today/145343","https://ptp.today/145345","https://ptp.today/145348","https://ptp.today/145349","https://ptp.today/145350","https://ptp.today/145351","https://ptp.today/145352","https://ptp.today/145353","https://ptp.today/145354","https://ptp.today/145356","https://ptp.today/145357","https://ptp.today/145359"]


chromelist = ['130.0.6723.86','119.0.6045.48','126.0.6460.1','126.0.6456.0','123.0.6312.41','121.0.6111.1','121.0.6111.2','121.0.6111.0','127.0.6533.38','119.0.6045.214','123.0.6312.13','119.0.6045.189','125.0.6393.0','119.0.6045.22','125.0.6379.0','125.0.6379.5','123.0.6274.0','127.0.6499.1','125.0.6379.2','127.0.6533.47','126.0.6452.1','122.0.6241.2','126.0.6473.1','119.0.6045.196','125.0.6379.1','122.0.6238.1','119.0.6045.190','126.0.6478.45','122.0.6211.0','119.0.6045.47','125.0.6422.229','127.0.6533.37','119.0.6045.54','124.0.6367.152','119.0.6043.1','125.0.6394.0','119.0.6045.187','126.0.6478.9','127.0.6504.0','122.0.6238.0','119.0.6045.212','127.0.6529.1','126.0.6478.110','126.0.6474.0','119.0.6045.213','119.0.6045.3','119.0.6045.206','121.0.6110.1','125.0.6422.234','119.0.6045.203','125.0.6373.1','124.0.6367.240','121.0.6109.1','122.0.6212.0','122.0.6237.0','119.0.6042.2','125.0.6422.224','124.0.6367.130','121.0.6109.0','119.0.6045.198','127.0.6533.49','126.0.6478.107','127.0.6503.1','119.0.6045.205','125.0.6422.204','119.0.6043.0','126.0.6473.0','123.0.6312.1','127.0.6499.2','119.0.6045.211','119.0.6045.5','119.0.6041.0','127.0.6503.0','126.0.6478.37','127.0.6533.46','129.0.6668.79','119.0.6045.46','119.0.6042.1','128.0.6613.192','131.0.6745.1','130.0.6723.23','121.0.6108.1','130.0.6723.22','119.0.6045.4','131.0.6745.0','122.0.6197.1','132.0.6789.1','119.0.6045.188','127.0.6502.1','124.0.6367.150','126.0.6478.44','131.0.6744.1','119.0.6045.21','131.0.6743.2','127.0.6515.10','131.0.6778.9','128.0.6613.175','131.0.6764.3','128.0.6613.174','127.0.6533.0','132.0.6784.1','131.0.6742.0','119.0.6041.1','125.0.6422.237','125.0.6422.205','131.0.6743.1','131.0.6743.0','119.0.6042.0','130.0.6723.21','129.0.6668.78','124.0.6367.128','131.0.6765.0','131.0.6777.2','126.0.6472.1','127.0.6533.14','119.0.6040.1','126.0.6462.0','124.0.6367.151','119.0.6045.197','123.0.6277.1','131.0.6772.1','131.0.6742.1','126.0.6478.39','122.0.6213.0','131.0.6765.1','131.0.6753.1','128.0.6613.193','131.0.6753.0','131.0.6740.0','129.0.6668.95','130.0.6723.30','130.0.6723.17','129.0.6668.71','131.0.6774.0','130.0.6723.54','131.0.6739.1','130.0.6723.16','128.0.6613.188','126.0.6478.256','129.0.6668.73','128.0.6613.172','132.0.6783.1','131.0.6778.5','128.0.6613.184','131.0.6735.1','126.0.6478.200','132.0.6783.0','130.0.6723.20','129.0.6668.69','131.0.6766.1','131.0.6768.4','131.0.6764.4','131.0.6778.18','131.0.6741.1','132.0.6784.0','131.0.6741.0','131.0.6764.1','129.0.6668.75','131.0.6739.0','131.0.6756.1','131.0.6778.6','131.0.6764.0','130.0.6723.31','131.0.6773.1','130.0.6723.53','130.0.6723.51','132.0.6799.0','131.0.6778.8','128.0.6613.183','131.0.6738.1','128.0.6613.173','129.0.6668.76','130.0.6723.18','132.0.6794.1','131.0.6738.0','130.0.6723.41','128.0.6613.187','130.0.6723.33','129.0.6668.77','130.0.6723.79','131.0.6775.1','131.0.6757.1','130.0.6723.36','130.0.6723.78','132.0.6792.1','131.0.6764.2','128.0.6613.170','132.0.6784.2','120.0.6099.338','129.0.6668.112','131.0.6739.2','120.0.6099.336','131.0.6735.0','131.0.6778.10','129.0.6668.72','130.0.6723.19','131.0.6740.1','120.0.6099.337','126.0.6478.254','131.0.6776.0']

app_stop = 0  #判断是否终止程序
start_time = time.time()
print('app start time:')
print(start_time)
end_time = time.time()

def naproxy():
    global chromelist
    global url
    global app_stop

    
    print("start naproxy thread!")
    
    thread_stop = 0 # 判断是否终止线程
    error = 0
    count = 0
    country = 0 # 0为俄罗斯 1为德国
    while thread_stop == 0 and app_stop == 0 and error < 10:
        try:
            with sync_playwright() as p:
 
                if country == 0:
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s1 = '.select > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2)'
                else:
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s1 = '.select > div:nth-child(2) > ul:nth-child(1) > li:nth-child(12)'                
               
                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./nap",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()

                page.goto('https://www.naproxy.com/croxyproxy/', wait_until='domcontentloaded')
                element = page.wait_for_selector('.select')
                element.click()
                page.wait_for_timeout(1000)
                page.locator(s1).click()
                page.locator('.input > input:nth-child(2)').fill(url)
                page.locator('div.content:nth-child(5) > div:nth-child(1) > form:nth-child(1) > button:nth-child(2)').click() 
                page.wait_for_timeout(30000)
                browser.close()
                print("naproxy count :" + str(count))
                count = count + 1
                error = 0

                if country == 0:
                    country = 1
                else:
                    country = 0
        except:
            error = error + 1
            print("naproxy have errors")

    print("stop naproxy thread!")  
        
def lumiproxy():
    global chromelist
    global url
    global app_stop

    
    print("start lumiproxy thread!")

    thread_stop = 0 # 判断是否终止线程
    error = 0
    count = 0
    country = 0 # 0为俄罗斯 1为德国
    while thread_stop == 0 and app_stop == 0 and error < 10:
        try:
            with sync_playwright() as p:

                if country == 0:
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s2 = 'li.el-select-dropdown__item:nth-child(2)'
                else:
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s2 = 'li.el-select-dropdown__item:nth-child(12)'               
               
                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./lumip",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()

                page.goto('https://www.lumiproxy.com/online-proxy/croxyproxy/', wait_until='domcontentloaded')
                element = page.wait_for_selector('.el-input--suffix > input:nth-child(1)')
                element.click()
                page.wait_for_timeout(1000)
                page.locator(s2).click()
                page.locator('.search_wrapper > div:nth-child(1) > input:nth-child(1)').fill(url)
                page.locator('div.btn').click()
                page.wait_for_timeout(30000)
                browser.close()
                print("lumiproxy count :" + str(count))
                count = count + 1
                error = 0

                if country == 0:
                    country = 1
                else:
                    country = 0
        except:
            error = error + 1
            print("lumiproxy have errors")

    print("stop lumiproxy thread!")

def p911():
    global chromelist

    global url
    global app_stop

   
    print("start 911proxy thread!")

    thread_stop = 0 # 判断是否终止线程
    error = 0
    count = 0
    country = 0 # 0为俄罗斯 1为德国
    while thread_stop == 0 and app_stop == 0 and error < 10:
        try:
            with sync_playwright() as p:
                
                if country == 0:
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s5 = '.selectList > li:nth-child(2)'
                else:
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s5 = '.selectList > li:nth-child(12)'               
               
                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./p911",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()           
                
                page.goto('https://www.911proxy.com/croxyproxy/', wait_until='domcontentloaded')
                try:
                    element = page.wait_for_selector('/html/body/div[1]/div/div/div[1]/div[6]/div/img[2]', timeout=5000)
                    element.click()
                except:
                    print("have errors")
                page.locator('.showValue').click()
                page.wait_for_timeout(1000)
                page.locator(s5).click()
                page.locator('.m-input > input:nth-child(2)').fill(url)
                page.locator('.search_btn').click()                
                page.wait_for_timeout(30000)
                browser.close()
                print("911proxy count :" + str(count))
                count = count + 1
                error = 0

                if country == 0:
                    country = 1
                else:
                    country = 0
        except:
            error = error + 1
            print("911proxy have errors")
            
    print("stop 911proxy thread!")


def plite():
    global chromelist
    global url
    global app_stop

    global start_time   
    global end_time
    run_time = end_time - start_time
    count = 0
    countrys = [0, 2] # 0为俄罗斯 2为德国
    while run_time < 10800:   # 运行时间少于 3 小时 就是 3x60x60=10800 秒
        try:
            with sync_playwright() as p:

                country = random.choice(countrys)
                if country == 0: #俄罗斯 Russia
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s4 = 'li.t-select-option:nth-child(2)'
                elif country == 1:  #乌克兰 Ukraine
                    lc = 'uk-UA'
                    timezone = 'Europe/Kyiv'
                    s4 = 'li.t-select-option:nth-child(19)'
                elif country == 2:  #德国 Germany
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s4 = 'li.t-select-option:nth-child(12)'
                elif country == 3:  #美国 USA
                    lc = 'en-US'
                    timezone = 'America/Chicago'
                    s4 = 'li.t-select-option:nth-child(1)'
                elif country == 4:  #白俄罗斯 Belarus 
                    lc = 'be-BY'
                    timezone = 'Europe/Minsk'
                    s4 = 'li.t-select-option:nth-child(55)'
                elif country == 5:  #哈萨克斯坦 Kazakhstan
                    lc = 'kk-KZ'
                    timezone = 'Asia/Almaty'
                    s4 = 'li.t-select-option:nth-child(30)'
                elif country == 6:  #乌兹别克斯坦 Uzbekistan
                    lc = 'uz-UZ'
                    timezone = 'Asia/Tashkent'
                    s4 = 'li.t-select-option:nth-child(37)'
                elif country == 7:  #保加利亚 Bulgaria
                    lc = 'bg-BG'
                    timezone = 'Europe/Sofia'
                    s4 = 'li.t-select-option:nth-child(84)'
                else:   #尼日利亚 Nigeria
                    lc = 'en-NG'
                    timezone = 'Africa/Lagos'
                    s4 = 'li.t-select-option:nth-child(17)'

                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./plite",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()    

                page.goto('https://www.proxylite.com/croxyproxy/', wait_until='domcontentloaded')
                try:
                    element = page.wait_for_selector('.close')
                    element.click()
                except:
                    print("have errors")
                page.locator('.t-is-readonly > input:nth-child(1)').click()
                page.wait_for_timeout(1000)
                page.locator(s4).click()
                page.locator('.search > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').fill(url)
                page.locator('.search_btn').click()
                page.wait_for_timeout(30000)
                browser.close()
                end_time = time.time()
                run_time = end_time - start_time
                print("proxylite count :" + str(count))
                count = count + 1

        except:
            end_time = time.time()
            run_time = end_time - start_time
            print("proxylite have errors")
    app_stop = 1            
    print("stop proxylite thread!")



def proxycc():
    global chromelist
    global url
    global app_stop
    
    print("start proxycc thread!")
    
    thread_stop = 0 # 判断是否终止线程
    error = 0
    count = 0
    countrys = [0, 2] # 0为俄罗斯 2为德国
    while thread_stop == 0 and app_stop == 0 and error < 10:
        try:
            with sync_playwright() as p:

                country = random.choice(countrys)
                if country == 0: #俄罗斯 Russia
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s3 = 'Russia'
                elif country == 1:  #乌克兰 Ukraine
                    lc = 'uk-UA'
                    timezone = 'Europe/Kyiv'
                    s3 = 'Ukraine'
                elif country == 2:  #德国 Germany
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s3 = 'Germany'
                elif country == 3:  #美国 USA
                    lc = 'en-US'
                    timezone = 'America/Chicago'
                    s3 = 'United States'
                elif country == 4:  #白俄罗斯 Belarus 
                    lc = 'be-BY'
                    timezone = 'Europe/Minsk'
                    s3 = 'Belarus'
                elif country == 5:  #哈萨克斯坦 Kazakhstan
                    lc = 'kk-KZ'
                    timezone = 'Asia/Almaty'
                    s3 = 'Kazakhstan'
                elif country == 6:  #乌兹别克斯坦 Uzbekistan
                    lc = 'uz-UZ'
                    timezone = 'Asia/Tashkent'
                    s3 = 'Uzbekistan'
                elif country == 7:  #保加利亚 Bulgaria
                    lc = 'bg-BG'
                    timezone = 'Europe/Sofia'
                    s3 = 'Bulgaria'
                else:   #尼日利亚 Nigeria
                    lc = 'en-NG'
                    timezone = 'Africa/Lagos'
                    s3 = 'Nigeria'

                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./pcc",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()

                page.goto('https://proxy.cc/croxyproxy/', wait_until='domcontentloaded')
                try:
                    element = page.wait_for_selector('.close')
                    element.click()
                except:
                    print("have errors")
                page.locator('.search-input').click()
                page.wait_for_timeout(1000)
                page.get_by_title(s3).click()
                page.locator('.input > input:nth-child(1)').fill(url)
                page.locator('.go').click()
                page.wait_for_timeout(30000)
                browser.close()
                print("proxycc count :" + str(count))
                count = count + 1
                error = 0

        except:
            error = error + 1
            print("proxycc have errors")
                
    print("stop proxycc thread!")



def omegaproxy():
    global chromelist
    global url
    global app_stop
    
    print("start omegaproxy thread!")
    
    thread_stop = 0 # 判断是否终止线程
    error = 0
    count = 0
    countrys = [0, 2] # 0为俄罗斯 2为德国
    while thread_stop == 0 and app_stop == 0 and error < 10:
        try:
            with sync_playwright() as p:

                country = random.choice(countrys)
                if country == 0: #俄罗斯 Russia
                    lc = 'ru-RU'
                    timezone = 'Europe/Moscow'
                    s6 = 'li.el-select-dropdown__item:nth-child(2)'
                elif country == 1:  #乌克兰 Ukraine
                    lc = 'uk-UA'
                    timezone = 'Europe/Kyiv'
                    s6 = 'li.el-select-dropdown__item:nth-child(19)'
                elif country == 2:  #德国 Germany
                    lc = 'de-DE'
                    timezone = 'Europe/Berlin'
                    s6 = 'li.el-select-dropdown__item:nth-child(12)'
                elif country == 3:  #美国 USA
                    lc = 'en-US'
                    timezone = 'America/Chicago'
                    s6 = 'li.el-select-dropdown__item:nth-child(1)'
                elif country == 4:  #白俄罗斯 Belarus 
                    lc = 'be-BY'
                    timezone = 'Europe/Minsk'
                    s6 = 'li.el-select-dropdown__item:nth-child(55)'
                elif country == 5:  #哈萨克斯坦 Kazakhstan
                    lc = 'kk-KZ'
                    timezone = 'Asia/Almaty'
                    s6 = 'li.el-select-dropdown__item:nth-child(30)'
                elif country == 6:  #乌兹别克斯坦 Uzbekistan
                    lc = 'uz-UZ'
                    timezone = 'Asia/Tashkent'
                    s6 = 'li.el-select-dropdown__item:nth-child(37)'
                elif country == 7:  #保加利亚 Bulgaria
                    lc = 'bg-BG'
                    timezone = 'Europe/Sofia'
                    s6 = 'li.el-select-dropdown__item:nth-child(84)'
                else:   #尼日利亚 Nigeria
                    lc = 'en-NG'
                    timezone = 'Africa/Lagos'
                    s6 = 'li.el-select-dropdown__item:nth-child(17)'

                print(lc)
                print(timezone)

                chooseChrome = random.randint(0, 199)
                print('第' + str(chooseChrome) + '个 chrome')
                ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ chromelist[chooseChrome] +' Safari/537.36'

                browser = p.chromium.launch_persistent_context(
                user_data_dir="./omega",
                channel="chrome",
                headless=False,
                no_viewport=True,
                locale=lc,
                timezone_id=timezone,
                user_agent=ua
                )
                page = browser.new_page()

                page.goto('https://www.omegaproxy.com/croxyproxy/', wait_until='domcontentloaded')
                element = page.wait_for_selector('div.el-input:nth-child(1) > input:nth-child(1)')
                element.click()
                page.wait_for_timeout(1000)
                page.locator(s6).click()
                page.locator('div.el-input:nth-child(2) > input:nth-child(1)').fill(url)
                page.locator('a.btn').click()
                page.wait_for_timeout(30000)
                browser.close()
                print("omegaproxy count :" + str(count))
                count = count + 1
                error = 0

        except:
            error = error + 1
            print("omegaproxy have errors")
                
    print("stop omegaproxy thread!")


   
t1 = threading.Thread(target=naproxy)
t2 = threading.Thread(target=lumiproxy)
t5 = threading.Thread(target=p911)
t4 = threading.Thread(target=plite)
t3 = threading.Thread(target=proxycc)
t6 = threading.Thread(target=omegaproxy)

t1.start()
t2.start()
t5.start()
t4.start()
t3.start()
t6.start()

t1.join()
t2.join()
t5.join()
t4.join()
t3.join()
t6.join()

print ("退出主线程")
print('app stop time:')
print(end_time)
