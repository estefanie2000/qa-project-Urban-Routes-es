import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


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
    cvv = (By.CLASS_NAME, 'card-code-input')
    numero_de_tarjeta = (By.CLASS_NAME, 'card-number-input')
    confirmar_tarjeta = (By.XPATH, '//button[@type="submit" and text()="Agregar"]')



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

    def set_telefono(self, telefono): #recomendo poner el webdriverwait, revisar que funcione hasta de enviarlo si no hacerlo como la linea 50
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
        expected_conditions.element_to_be_clickable(self.cvv)
        )

    def set_cvv(self):
        self.get_cvv().click()

    def set_rellenar_cvv(self, card_code):
        self.set_cvv()

    def get_numero_de_tarjeta(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(self.numero_de_tarjeta)
        )

    def set_numero_de_tarjeta(self):
        self.get_numero_de_tarjeta().click()

    def set_rellenar_tarjeta(self, card_number):
        self.set_numero_de_tarjeta()







class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_boton_pedir_taxi(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_boton_pedir_taxi()
        routes_page.set_boton_comfort()

    def test_boton_telefono(self):
        self.test_boton_pedir_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_boton_telefono()
        telefono = data.phone_number
        routes_page.rellenar_telefono(telefono)
        routes_page.set_boton_siguiente_telefono()
        routes_page.set_mensaje_codigo(self)
        routes_page.set_boton_confirmar_codigo()

    def test_metodo_de_pago(self):
        self.test_boton_pedir_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_metodo_de_pago()
        routes_page.set_agregar_tarjeta()
        routes_page.set_cvv()
        cvv = data.card_code
        routes_page.set_rellenar_cvv(self)
        routes_page.set_numero_de_tarjeta()
        cvv = data.card_number
        routes_page.set_rellenar_tarjeta(self)







    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
