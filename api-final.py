import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def agregar_dispositivo(nombre, trabajo):
    data = {"name": nombre, "job": trabajo}
    r = requests.post(BASE_URL, json=data)
    print(" POST:", r.status_code, r.json())
    return r

def listar_dispositivos():
    r = requests.get(BASE_URL)
    print(" GET:", r.status_code, r.json())
    return r

def actualizar_dispositivo(id, nombre, trabajo):
    data = {"name": nombre, "job": trabajo}
    r = requests.put(f"{BASE_URL}/{id}", json=data)
    print("PUT:", r.status_code, r.json())
    return r

def eliminar_dispositivo(id):
    r = requests.delete(f"{BASE_URL}/{id}")
    print(" DELETE:", r.status_code)
    return r

