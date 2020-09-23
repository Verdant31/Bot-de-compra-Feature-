# -*- coding: utf-8 -*-
import requests
import json
from selenium import webdriver
import time

def disponibilidade():
    r = requests.get('https://feature.com/products.json')
    produtos = json.loads((r.text))['products']
    
    for produto in produtos:
        
        nomeproduto = produto['title']
        #Para descobrir o nome, use o codigo abaixo no console.
        #for produto in produtos:
        #   print(produto['title'])
        if nomeproduto == 'Nome do tênis':
         
            urlproduto = 'https://feature.com/products/' + produto['handle']
            print('Item encontrado')
            return (urlproduto)
        #Caso tenha o produto em estoque, ira printar no console 'Item encontrado' e irá abrir a pagina da compra.
    else:    
        return False

def comprarProduto(url):
    
    driver = webdriver.Chrome('./chromedriver')
    driver.get(str(url))
    
    #Coloque a numeração do tamanho
    driver.find_element_by_xpath('//div[@data-value="Tamanho"]').click()
    time.sleep(1)
    #Botão para adicionar ao carrinho
    driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
    time.sleep(2)
    
    #Direcionamento para a pagina de checkout
    driver.get("https://feature.com/checkout")
    time.sleep(1)
    
    #Insira seu email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('Email')
    time.sleep(1)
    
    #Insira seu primeiro nome
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Primeiro nome')
    time.sleep(1)
    
    #Insira seu segundo nome
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Segundo nome')
    time.sleep(1)
    
    #Insira o nome da rua
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('Rua')
    time.sleep(1)
    
    #Insira o nome da cidade
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Cidade')
    time.sleep(1)
    
    #No lugar de opção, considere:
    #Acre = 2
    #Alagoas = 3
    #Amapá = 4
    #Amazonas = 5
    #...
    #Tocantins = 28
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[Opção]').click()
    time.sleep(1)
    
    #Insira seu CEP
    driver.find_element_by_xpath('//input[@placeholder="Postal code"]').send_keys('CEP')
    time.sleep(1)
    
    #Insira seu numero de telefone
    #Formato 067111111111
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('Numero do Telefone')
    
meuUrl=disponibilidade()
if meuUrl != False:
    comprarProduto(meuUrl)
else:
    print('Não há disponibilidade.')