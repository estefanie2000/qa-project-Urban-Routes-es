from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    boton_pedir_taxi = (By.CSS_SELECTOR, '.button.round')
    boton_comfort = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    boton_telefono = (By.CLASS_NAME, 'np-button')
    telefono = (By.ID, 'phone')
    boton_siguiente_telefono = (By.CSS_SELECTOR, '.button.full')
    codigo = (By.ID, 'code')
    boton_confirmar_codigo = (By.XPATH, '//button[@type="submit" and text()="Confirmar"]')
    metodo_de_pago = (By.CSS_SELECTOR, '.pp-button.filled')
    agregar_tarjeta = (By.CLASS_NAME, 'pp-plus-container')
    cvv = (By.NAME, "code")
    numero_de_tarjeta = (By.ID, "number")
    confirmar_tarjeta = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    boton_cerrar_metodo_de_pago = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/button")
    campo_mensaje = (By.ID, 'comment')
    escribir_mensaje = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label")
    manta_pañuelos = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    helados = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    modal_taxi =(By.XPATH, '/html/body/div/div/div[3]/div[4]/button')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver,5).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_boton_pedir_taxi(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_pedir_taxi)
        )

    def set_boton_pedir_taxi(self):
        self.get_boton_pedir_taxi().click()

    def get_boton_comfort(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_comfort)
        )

    def set_boton_comfort(self):
        self.get_boton_comfort().click()

    def get_boton_telefono(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_telefono)
        )

    def set_boton_telefono(self):
        self.get_boton_telefono().click()

    def get_telefono(self):
        return self.driver.find_element(*self.telefono).get_property('value')

    def set_telefono(self, telefono):
        self.driver.find_element(*self.telefono).send_keys(telefono)

    def rellenar_telefono(self, telefono):
        self.set_telefono(telefono)

    def get_boton_siguiente_telefono(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_siguiente_telefono)
        )

    def set_boton_siguiente_telefono(self):
        self.get_boton_siguiente_telefono().click()


    def get_mensaje_codigo(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.codigo)
        )

    def set_mensaje_codigo(self, codigo):
        codigo = retrieve_phone_code(self.driver)
        self.get_mensaje_codigo().send_keys(codigo)

    def get_boton_confirmar_codigo(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_confirmar_codigo)
        )

    def set_boton_confirmar_codigo(self):
        self.get_boton_confirmar_codigo().click()

    def get_metodo_de_pago(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.metodo_de_pago)
        )

    def set_metodo_de_pago(self):
        self.get_metodo_de_pago().click()

    def get_agregar_tarjeta(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.agregar_tarjeta)
        )

    def set_agregar_tarjeta(self):
        self.get_agregar_tarjeta().click()


    def get_cvv(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.presence_of_element_located(self.cvv)
        )

    def set_cvv(self):
        self.get_cvv().click()

    def set_rellenar_cvv(self, card_code):
        self.get_cvv().send_keys(card_code)

    def get_numero_de_tarjeta(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.presence_of_element_located(self.numero_de_tarjeta)
        )

    def set_numero_de_tarjeta(self):
        self.get_numero_de_tarjeta().click()

    def set_rellenar_tarjeta(self, card_number):
        self.get_numero_de_tarjeta().send_keys(card_number)

    def get_confirmar_tarjeta(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.confirmar_tarjeta)
        )

    def set_confirmar_tarjeta(self):
        self.get_confirmar_tarjeta().click()

    def get_boton_cerrar_metodo_de_pago(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.boton_cerrar_metodo_de_pago)
        )

    def set_boton_cerrar_metodo_de_pago(self):
        self.get_boton_cerrar_metodo_de_pago().click()

    def get_campo_mensaje(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.presence_of_element_located(self.campo_mensaje)
        )

    def get_escribir_mensaje(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.escribir_mensaje)
        )

    def set_escribir_mensaje(self):
        self.get_escribir_mensaje().click()

    def set_rellenar_mensaje(self, message_for_driver):
        self.get_campo_mensaje().send_keys(message_for_driver)

    def get_manta_pañuelos(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.manta_pañuelos)
        )

    def set_manta_pañuelos(self):
        self.get_manta_pañuelos().click()

    def get_helados(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.helados)
        )

    def set_helados(self):
        self.get_helados().click()
        self.get_helados().click()

    def get_modal_taxi(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.modal_taxi)
        )

    def set_modal_taxi(self):
        self.get_modal_taxi().click()

