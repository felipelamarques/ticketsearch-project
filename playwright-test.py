from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Usar chrome como browser *mostrar RPA acondecendo headless=false
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()  # Abrir uma nova janela

    page.goto("https://www.google.com.br")  # ir para a página
    page.fill("textarea[name='q']", 'Latam')  # Pesquisar pelo site 'Latam'
    page.click("input[name='btnK']")  # Clicar no botão 'Pesquisa Google'

    # clica no resultado que tiver o url 'https://www.latamairlines.com/br/pt'
    page.click("a[href='https://www.latamairlines.com/br/pt']")
    # Aceita os coockies do site
    page.click("button[data-testid='cookies-politics-button--button']")
    page.wait_for_timeout(2000)

    page.fill("input[name='origin']", 'São Paulo')  # Clicar no botão de origem
    page.click("input[name='destination']")
    page.click("input[name='origin']")
    # page.click("li[id='lstItem_0']") #Selecionar a origem 'SP-todos aeroportos'
    # page.click("li[id='lstItem_1']") #Selecionar a origem 'SP-Congonhas'
    page.click("li[id='lstItem_2']")  # Selecionar a origem 'SP-Guarulhos'

    # Clicar no botão de destino
    page.fill("input[name='destination']", 'Rio de janeiro')
    page.click("input[name='origin']")
    page.click("input[name='destination']")
    # page.click("li[id='lstItem_0']") #Selecionar a origem 'RJ-todos aeroportos'
    # page.click("li[id='lstItem_1']") #Selecionar a origem 'RJ-Galeão'
    page.click("li[id='lstItem_2']")  # Selecionar a origem 'RJ-Santos dumont'

    # Clicar no botão do tipo de viagem (Ida e volta)
    page.click("button[id='btnTripTypeCTA']")
    # page.click("button[id='btnTripType0']") #Seleciona 'Somente ida'
    page.click("button[id='btnTripType1']")  # Seleciona 'Ida e volta'

    # Clicar no botão do tipo de cabine
    page.click("button[id='btnCabinTypeCTA']")
    page.click("button[id='btnCabinType0']")  # Selecionar 'Economy'
    # page.click("button[id='btnCabinType1']") #Selecionar 'Premium Economy'
    # page.click("button[id='btnCabinType2']") #Selecionar 'Premium Business'

    # clicar no botão da quantidade de passageiros
    page.click("button[id='btnAddPassengerCTA']")
    # Selecionar 1 adulto
    # Selecionar 0 crianças
    # Selecionar 0 bebes

    # Selecionar a data da ida
    # Selecionar a data da volta

    page.click("button[id='btnSearchCTA']")  # Clicar no botão de procurar

    page.wait_for_timeout(120000)
    browser.close()
