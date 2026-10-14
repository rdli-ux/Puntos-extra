import requests

URL_BASE = "http://127.0.0.1:5006"

response = requests.get(f"{URL_BASE}/equipos")
print("--- PRUEBA GET /equipos ---")
print("Código de estado:", response.status_code)

registros = response.json()
for item in registros:
  print(
      f"ID: {item['id']} | Nombre: {item['nombre']} | Tipo: {item['tipo']} |"
      f" Estado: {item['estado']}"
  )

print("\n--- PRUEBA FILTRO /equipos/tipo/switch ---")
resp_filtro = requests.get(f"{URL_BASE}/equipos/tipo/switch")
print("Código de estado:", resp_filtro.status_code)
print("Resultado filtrado:", resp_filtro.json())