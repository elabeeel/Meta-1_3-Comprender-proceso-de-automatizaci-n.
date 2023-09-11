from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def buscar_en_amazon(producto):
    driver = webdriver.Chrome(executable_path='C:\Users\lange\Downloads\chromedriver')

    try:
        driver.get('https://www.amazon.com.mx/')

        search_box = driver.find_element_by_id('Creed Aventus Eau De Parfum Spray for Men, 3.3 Ounce')
        search_box.send_keys(producto)

        search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        driver.save_screenshot('captura_de_pantalla.png')

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

    finally:
        driver.quit()


buscar_en_amazon('Perfume creed')