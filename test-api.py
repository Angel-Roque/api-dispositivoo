# test_api_client.py
import unittest
from api_client import agregar_dispositivo, listar_dispositivos, actualizar_dispositivo, eliminar_dispositivo

class TestAPI(unittest.TestCase):
    def test_agregar_dispositivo(self):
        r = agregar_dispositivo("TestDevice", "Tester")
        self.assertEqual(r.status_code, 201)
        self.assertIn("id", r.json())

    def test_listar_dispositivos(self):
        r = listar_dispositivos()
        self.assertEqual(r.status_code, 200)
        self.assertIn("data", r.json())

    def test_actualizar_dispositivo(self):
        r = actualizar_dispositivo(2, "UpdatedDevice", "UpdatedRole")
        self.assertIn(r.status_code, [200, 201])
        self.assertIn("job", r.json())

    def test_eliminar_dispositivo(self):
        r = eliminar_dispositivo(2)
        self.assertEqual(r.status_code, 204)

if __name__ == "__main__":
    unittest.main()


