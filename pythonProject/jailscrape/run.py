import constants as c
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
#options.add_argument("--headless")
PATH = "C:\webdriver\chromedriver.exe"
service = ChromeService(executable_path= PATH)
driver = webdriver.Chrome(service=service, options=options)
reps = []
mems = []
driver.get(c.URL)
wait = WebDriverWait(driver, 10)
#scrape top page and make URL list
for i in range(1,20):
    #memberD = wait.until(driver.find_element(By.CSS_SELECTOR, ('tbody tr:nth-child('+str(i)+') td:nth-child(2) a:nth-child(1)'))
    memberD = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody tr:nth-child(' + str(i) + ') td:nth-child(2) a:nth-child(1)')))
    result = memberD;
    link = result.get_attribute('href')
    reps.append(link)
    #scrape each page in list
for j in range(0,19):
    second_url = reps[j]
    driver.get(second_url)
    try:
            email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body app-root div[class='container'] main app-member-page-component app-loader div[class='pageContent'] div[class='row'] div[class='col-sm-12 col-md-9'] div[class='row'] div[class='col-12 col-md-6 col-lg-8'] div:nth-child(1) a:first-of-type")))
            #print(email.text)
            name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body app-root h1:nth-child(1)")))
            #print(name.text)
            emaildone = email.get_attribute('innerHTML')
            namedone = name.get_attribute('innerHTML')
            #replacin' with spacin'
            namesano = namedone.replace('href="','')
            namesano = namesano.replace('">',' ')
            namesano = namesano.replace('</a><!----><!----> • ',' ')
            namesano = namesano.replace('	• ',' ')
            namesano = namesano.replace('</div>','</div> ')
            namesano = namesano.replace('<!----><!---->',' ')
            namesano = namesano.replace(',','')
            #split
            namesano = namesano.split(' ')
            #left shuttle and merge district and city name
            namesano[0] = emaildone
            districtmerge = namesano[10]+' '+namesano[11]
            namesano[4] = districtmerge
            namesano[5] = namesano[12]
            namesano[7] = namesano[9]
            if namesano[14] == '</div>':
                namesano[6] = namesano[13]

            else:
                citymerge = namesano[13] +' '+ namesano[14]
                namesano[6] = citymerge
            namesano[8] = reps[j]

    except:
            print('Bollocks!')

    print(j, namesano)
print("done")
driver.quit()