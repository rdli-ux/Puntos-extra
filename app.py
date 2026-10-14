from flask import Flask, jsonify

app = Flask(__name__)

equipos_red = [
    {
        "id": 1,
        "nombre": "Switch 1841",
        "tipo": "switch",
        "marca": "Cisco",
        "cantidad": 2,
        "estado": "disponible",
    },
    {
        "id": 2,
        "nombre": "Router Borde 01",
        "tipo": "router",
        "marca": "MikroTik",
        "cantidad": 1,
        "estado": "en uso",
    },
    {
        "id": 3,
        "nombre": "Access Point Lab",
        "tipo": "access point",
        "marca": "Ubiquiti",
        "cantidad": 4,
        "estado": "disponible",
    },
    {
        "id": 4,
        "nombre": "Switch Acceso 02",
        "tipo": "switch",
        "marca": "TP-Link",
        "cantidad": 3,
        "estado": "mantenimiento",
    },
    {
        "id": 5,
        "nombre": "Firewall Perimetral",
        "tipo": "otro",
        "marca": "Fortinet",
        "cantidad": 1,
        "estado": "en uso",
    },
]


@app.route("/", methods=["GET"])
def bienvenida():
  return (
      jsonify({
          "mensaje": (
              "Bienvenido a NetStock API - Servidor Flask funcionando"
              " correctamente"
          ),
          "estado": "activo",
      }),
      200,
  )


@app.route("/equipos", methods=["GET"])
def obtener_equipos():
  return jsonify(equipos_red), 200


@app.route("/equipos/<int:id_equipo>", methods=["GET"])
def obtener_equipo_por_id(id_equipo):
  equipo = next((e for e in equipos_red if e["id"] == id_equipo), None)
  if equipo:
    return jsonify(equipo), 200
  return jsonify({"error": "Equipo no encontrado"}), 404


@app.route("/equipos/tipo/<string:tipo_equipo>", methods=["GET"])
def filtrar_por_tipo(tipo_equipo):
  # Filtra los equipos por tipo ignorando mayúsculas/minúsculas
  filtrados = [
      e for e in equipos_red if e["tipo"].lower() == tipo_equipo.lower()
  ]
  return jsonify(filtrados), 200


if __name__ == "__main__":
  app.run(debug=True, port=5006)