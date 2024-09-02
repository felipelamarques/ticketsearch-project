from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com.br") 
    page.fill("textarea[name='q']", 'Latam') 
    page.click("input[name='btnK']")

    page.click("a[href='https://www.latamairlines.com/br/pt']") 
    page.click("button[data-testid='cookies-politics-button--button']")
    page.wait_for_timeout(2000)

    page.fill("input[name='origin']", 'São Paulo')
    page.click("input[name='destination']")
    page.click("input[name='origin']")
    page.click("li[id='lstItem_2']")
    
    page.fill("input[name='destination']", 'Rio de janeiro')
    page.click("input[name='origin']")
    page.click("input[name='destination']")
    page.click("li[id='lstItem_2']")

    page.click("button[id='btnTripTypeCTA']") 
    page.click("button[id='btnTripType1']")

    page.click("button[id='btnCabinTypeCTA']")
    page.click("button[id='btnCabinType0']") 

    page.click("button[id='btnAddPassengerCTA']") 

    page.click("button[id='btnSearchCTA']")

    page.wait_for_timeout(5000)
    browser.close()