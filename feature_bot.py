# -*- coding: utf-8 -*-
import requests
import json
from selenium import webdriver
import time



def nomeTenis():
    nome = input("Entre com o nome do produto que você quer: ")
    return nome
def tamanhoTenis():
    tamanho = input("Entre com o tamanho do tênis: ")
    return tamanho

nome = nomeTenis()
tamanho = tamanhoTenis()
 
    
def comprarTenis(nome, tamanho):

    
    
    driver = webdriver.Chrome('./chromedriver')
    url = 'https://feature.com/pages/search-results?q=' + nome
    driver.get(url)
  
    driver.find_element_by_xpath('//*[@id="isp_search_results_container"]/li[1]').click()
    
    driver.find_element_by_xpath('//div[@data-value=' + '"' + tamanho + '"' + ']').click()
    time.sleep(1)
  
    driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
    time.sleep(2)
    
    
    driver.get("https://feature.com/checkout")
    time.sleep(1)
    
    
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('Email')
    time.sleep(1)
    
    
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Primeiro nome')
    time.sleep(1)
    
    
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Segundo nome')
    time.sleep(1)
    
    
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('Rua')
    time.sleep(1)
    
   
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Cidade')
    time.sleep(1)
    
   
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[Opção]').click()
    time.sleep(1)
    
    
    driver.find_element_by_xpath('//input[@placeholder="Postal code"]').send_keys('CEP')
    time.sleep(1)
 
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('Numero do Telefone')

comprarTenis(nome, tamanho)
