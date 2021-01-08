class Inventario:

    def __init__(self, nombre, nombre_archivo):
        self.nombre = nombre
        self.nombre_archivo = nombre_archivo
        self.elementos = []

    def __crear_archivo(self):
        pass

    def agregar(self, elemento):
        self.elementos.append(elemento)
        return self.elementos

    def extraer(self):
        pass

    def mostrar_contenido(self):
        pass

    def vaciar(self):
        pass

    def guardar_en_archivo(self):
        pass


class HistoricoRamos(Inventario):
    pass
    #Conteo de ramos

class RamosEnComercializacion(Inventario):
    #Solo lo que sale a la venta
    pass


class RecetaRamo(Inventario):
    pass


class Ramo(RecetaRamo):
    pass


class BodegaFlores(Inventario):
    pass


class Flores:
    pass


class FabricadorRamos:
    def __init__(self, bodega_flores, ramos_en_comercializacion, historico_ramos):
        self.bodega_flores = bodega_flores
        self.ramos_en_comercializacion = ramos_en_comercializacion
        self.historico_ramos = historico_ramos

    def calcular_ramos_posibles(self):
        '''
        logica que contraste ingredientes en bodega con pizzas que se deben
        fabricar, y generará una lista de las pizzas que son posibles de generar
        en base a eso
        '''
        return lista_ramos_posibles

    def generar_ramo(self, lista_ramos_posibles):
        '''
        logica aleatoria para escoger solo una pizza de la lista de pizzas posibles
        y la genera (seguramente se necesitará el objeto de recetas)
        '''
        return ramos_generada

    def despachar_ramo(self, ramos):
        self.historico_ramos.agregar(ramos)
        return self.historico_ramos.mostrar_contenido()


class ProcesoAbastecedor:
    def __init__(self, bodega_flores, ramos_en_comercializacion):
        self.bodega_flores = bodega_flores
        self.ramos_en_comercializacion = ramos_en_comercializacion

    def generar_partida_flores(self):
        listado_tipos_ramos = ramos_en_comercializacion.mostrar_contenido()

        '''
        logica de listar ingredientes y seleccionar aleatoriamente uno o varios
        para generar una partida que entrará a bodega
        '''
        return listado_flores

    def abastecer_flores(self, flor):
        self.bodega_flores.agregar(flor)
        return self.bodega_flores.mostrar_contenido()


import time

bodega_flores = BodegaFlores()
ramos_en_comercializacion = RamosEnComercializacion()
historico_ramos = HistoricoRamos()

abastecedor = ProcesoAbastecedor(bodega_flores, ramos_en_comercializacion)

fabricador = FabricadorRamos(bodega_flores, ramos_en_comercializacion, historico_ramos)

while True:
    flores_abastecido = abastecedor.generar_partida_flores(ramos_en_comercializacion)
    abastecedor.abastecer_flores(flores_abastecido)
    print("Abasteciendo flores!!!")
    time.sleep(1)
    print("Calculando ramos factibles!!")
    if len(fabricador.calcular_ramos_posibles()) != 0:
        ramo = fabricador.generar_ramo(ramo)
        print("Fabricando ramo:", ramo)
        fabricador.despachar_ramo(ramo)
        print("Despachando ramo:", ramo)
    time.sleep(1)