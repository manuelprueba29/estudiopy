class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario  # ID único del usuario
        self.nombre = nombre
        self.correo = correo
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, concesionario, modelo):
        mensaje = concesionario.vender_vehiculo(modelo)
        if "vendido con éxito" in mensaje:
            for v in concesionario.vehiculos:
                if v.modelo == modelo and v.estado == "Vendido":
                    self.vehiculos_comprados.append(v)
        return mensaje

    def listar_mis_vehiculos(self):
        return [v.mostrar_info() for v in self.vehiculos_comprados]


class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, id_usuario, nombre, correo):
        if id_usuario in self.usuarios:
            return "Error: Usuario ya registrado."
        self.usuarios[id_usuario] = Usuario(id_usuario, nombre, correo)
        return f"Usuario {nombre} agregado con éxito."

    def actualizar_usuario(self, id_usuario, nombre=None, correo=None):
        if id_usuario not in self.usuarios:
            return "Error: Usuario no encontrado."
        if nombre:
            self.usuarios[id_usuario].nombre = nombre
        if correo:
            self.usuarios[id_usuario].correo = correo
        return f"Usuario {id_usuario} actualizado."

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            return f"Usuario {id_usuario} eliminado con éxito."
        return "Error: Usuario no encontrado."

    def listar_usuarios(self):
        return [f"{u.id_usuario}: {u.nombre} - {u.correo}" for u in self.usuarios.values()]
