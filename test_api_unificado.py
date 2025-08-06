import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def agregar_dispositivo(nombre, trabajo):
    data = {"name": nombre, "job": trabajo}
    r = requests.post(BASE_URL, json=data)
    return r

def listar_dispositivos():
    r = requests.get(BASE_URL)
    return r

def actualizar_dispositivo(id, nombre, trabajo):
    data = {"name": nombre, "job": trabajo}
    r = requests.put(f"{BASE_URL}/{id}", json=data)
    return r

def eliminar_dispositivo(id):
    r = requests.delete(f"{BASE_URL}/{id}")
    return r


class TestAPI(unittest.TestCase):

    def test_agregar_dispositivo(self):
        r = agregar_dispositivo("TestDevice", "Tester")
        self.assertEqual(r.status_code, 201)
        self.assertIn("id", r.json())

    def test_listar_dispositivos(self):
        r = listar_dispositivos()
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)
        self.assertIn("id", r.json()[0])
        self.assertIn("name", r.json()[0])

    def test_actualizar_dispositivo(self):
        r = actualizar_dispositivo(2, "UpdatedDevice", "UpdatedRole")
        self.assertIn(r.status_code, [200, 201])
        self.assertIn("job", r.json())

    def test_eliminar_dispositivo(self):
        r = eliminar_dispositivo(2)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "{}")

if __name__ == "__main__":
    unittest.main()

