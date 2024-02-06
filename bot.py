from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time
import keyboard

import pyautogui

def fun(i):
      time.sleep(2)
      driver.execute_script("window.scrollTo(0, 0)")
      time.sleep(5)

      scrolls = int(driver.execute_script("return document.body.scrollHeight") )
      scrolls -= 924
      
      total_scrolls = int(scrolls/400)
      print(total_scrolls)

      for _ in range(total_scrolls): 
        actions.send_keys(Keys.ARROW_DOWN*5).perform()
     
        time.sleep(5)
        
      print(str(i)+'ª volta')

def iterator(link):
    actions = ActionChains(driver)
   
    
    time.sleep(4)
    #                                        /html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div/div/span[1]
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div/div/span[1]")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView()",element) 
    time.sleep(2)
    print('subiu') 
    # Fazer o click para os filtros
    elem1 = driver.find_element(By.XPATH, link)  
    elem1.click()
    time.sleep(2)
    print("ok")
    time.sleep(2)
  
    if recursion(10) == False:
       return False
    
    scroll_tag = recursion(10)
    
    time.sleep(2) 
    


    #clicar num ponto para a rolagem da janela
    elem7 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/ul/li[1]/div/div[1]/h6")
    elem7.click() 
    time.sleep(1)
      # Para subir a tela ao máximo 
    actions.send_keys(Keys.ARROW_UP * 200 ).perform() 


    # Calcular o total de Scrolls
    time.sleep(2)
     
    scrolls = driver.find_element(By.XPATH, scroll_tag)
    local1 = scrolls.location['y']
    print(local1)
    total_Scrolls = int(local1/400)
    print(total_Scrolls + 1) 
    
    time.sleep(7)     
    
    auxiliar = 0
    while local1!=auxiliar:
      
      local1 = scrolls.location['y']
      print(local1)
      

      actions.send_keys(Keys.ARROW_DOWN * 3 ).perform()
      time.sleep(1)
      auxiliar = scrolls.location['y']
    
    elem1.click()
    time.sleep(2)   

"""
Essa função servirá para encontrar o tamanho de cada janela pegando a posição da última classe pelo XPath,
como a última classe pode ter posição diferente em cada filtro, foi usada a recursividade para tratar as exceções
e decrementar até encontrar a última posição
"""   
def recursion(i):
   if i == 0 :
      return False
   #             /html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[6]/div/div/div
   scroll_tag = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[{i}]/div/div"
  
   new_scroll = scroll_tag.format(i=i)
   
   try:
     
     driver.find_element(By.XPATH, new_scroll)
     return new_scroll

   except NoSuchElementException:
     return recursion(i-1)   
     

def NewRecursion(i):
   
    if i == 0 :
      return False
   #             /html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[6]/div/div/div
    scroll_tag = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[{i}]/div/div/div"
  
    new_scroll = scroll_tag.format(i=i)
   
    try:
     print("In NewRecursion")
     print(i)
     while i>2: 
      elem2 = driver.find_element(By.XPATH, new_scroll)
      time.sleep(2)
      elem2.click()
      return NewRecursion(i-1)  
     
    except NoSuchElementException:
     return NewRecursion(i-1)    

driver = webdriver.Edge()
driver.maximize_window()

# Habilitar o modo tela cheia FAZER UM CLICK NA PÁGINA SE NECESSÁRIO


driver.get("")
assert " Sistema de Autenticação" in driver.title
time.sleep(5)

pyautogui.press("f11")


time.sleep(5)

try:
  
    elem1 = driver.find_element(By.ID, "username")
    elem1.clear()
    elem1.send_keys("")
    elem1.send_keys(Keys.RETURN)

    elem2 = driver.find_element(By.ID, "password")
    elem2.clear()
    elem2.send_keys("")
    elem2.send_keys(Keys.RETURN)

    driver.get("")
    actions = ActionChains(driver)
    time.sleep(6)
    
    # Minimizar as classes não importantes  /html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[5]/div/div/
  
    NewRecursion(7)
   
    time.sleep(2)
    print('Beschlagnahmen')

    keyboard.send('f11')
    
    time.sleep(2)
    # Colocar no modo tela cheia
    elem3 = driver.find_element(By.ID, "ghx-view-presentation")
    elem3.click()
    time.sleep(1)
    #clickar num ponto para a rolagem da janela 
    elem7 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/ul/li[1]/div/div[1]/h6")
    elem7.click() 
    
    time.sleep(3)


    cont = 1 


    while True:

      actions = ActionChains(driver)
      time.sleep(1) 
      actions.send_keys(Keys.ARROW_UP * 300 ).perform()   
      
      time.sleep(8)

      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[1]/a" )
       
      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[2]/a")
       
      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[3]/a")
       
      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[4]/a") 
       
      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[5]/a") 
        
      iterator("/html/body/div[1]/div/main/div/div[2]/div[3]/div[1]/div/div[2]/div/dl/dd[6]/a") 

      
      time.sleep(3)
      link  = ""
      power_bi_link = ""

      
      time.sleep(1)
      driver.execute_script("window.open('about:blank', 'new_window2')")
      driver.switch_to.window(driver.window_handles[0])
      time.sleep(2)
      driver.switch_to.window("new_window2")

       # Para evitar que em todos os casos com exceção do 1º fiquem recarregando o link 
      if(driver.current_url != link):
       driver.get(link)

      time.sleep(2)
      driver.execute_script("window.open('about:blank', 'new_window1')")

      driver.switch_to.window(driver.window_handles[1])
      
      time.sleep(3)
      
      fun(cont)
      
      time.sleep(10)


      driver.switch_to.window("new_window1")
      
      # Para evitar que em todos os casos com exceção do 1º fiquem recarregando o link
      if(driver.current_url != power_bi_link):
       driver.get(power_bi_link)  
      time.sleep(15)

      driver.switch_to.window(driver.window_handles[0])
      cont += 1
      time.sleep(2)
      driver.refresh()
      
  
except NoSuchElementException:

   raise NoSuchElementException('Elemento nao encontrado')

except ElementNotInteractableException:

  raise ElementNotInteractableException('Nao eh possivel interagir com o elemento')
finally:
 
 print("Exception raised")
    
 time.sleep(10000)


