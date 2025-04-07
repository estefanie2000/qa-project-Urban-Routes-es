import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage


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
        boton_comfort = routes_page.get_boton_comfort().text
        comfort = "Comfort"
        assert comfort in boton_comfort

    def test_boton_telefono(self):
        self.test_boton_pedir_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_boton_telefono()
        telefono = data.phone_number
        routes_page.rellenar_telefono(telefono)
        routes_page.set_boton_siguiente_telefono()
        routes_page.set_mensaje_codigo(self)
        routes_page.set_boton_confirmar_codigo()
        assert routes_page.get_telefono () == data.phone_number


    def test_metodo_de_pago(self):
        self.test_boton_telefono()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_metodo_de_pago()
        routes_page.set_agregar_tarjeta()
        routes_page.set_cvv()
        routes_page.set_numero_de_tarjeta()
        numero_de_tarjeta = data.card_number
        routes_page.set_rellenar_tarjeta(numero_de_tarjeta)
        routes_page.set_rellenar_cvv(data.card_code)
        routes_page.set_confirmar_tarjeta()
        routes_page.set_boton_cerrar_metodo_de_pago()
        assert routes_page.get_cvv().get_attribute("value") == data.card_code
        assert routes_page.get_numero_de_tarjeta().get_attribute("value") == data.card_number

    def test_mensaje_para_conductor(self):
        self.test_metodo_de_pago()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_escribir_mensaje()
        campo_mensaje = data.message_for_driver
        routes_page.set_rellenar_mensaje(campo_mensaje)
        assert routes_page.get_campo_mensaje().get_attribute("value") == data.message_for_driver


    def test_manta_pañuelos(self):
        self.test_mensaje_para_conductor()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_manta_pañuelos()
        assert routes_page.get_manta_pañuelos().is_displayed()

    def test_helados(self):
        self.test_manta_pañuelos()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_helados()
        assert routes_page.get_helados().is_displayed()

    def test_modal_taxi(self):
        self.test_helados()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_modal_taxi()
        assert routes_page.get_modal_taxi().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
