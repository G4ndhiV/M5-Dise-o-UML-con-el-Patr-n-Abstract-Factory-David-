# M5-Dise-o-UML-con-el-Patr-n-Abstract-Factory-David-


Instrucciones
Seleccionar un tema:

Elige un sistema donde se pueda aplicar Abstract Factory.
Ejemplos:
Una fábrica de vehículos (autos, motos, camiones).
Un sistema de UI multiplataforma (Windows, Mac, Linux).
Diseñar el UML:

Identifica las interfaces y clases abstractas para la fábrica y los productos.
Implementa al menos dos fábricas concretas que generen distintos tipos de objetos.
Usa notación UML estándar (clases, relaciones, interfaces, etc.).
Implementación en código:

Implementa el diseño en el lenguaje de tu preferencia aplicando el patrón Abstract Factory.
Usa buenas prácticas: clases separadas en archivos
Ejemplo Referencia (Elegir un tema diferente de envios)

Tenemos diferentes fábricas que crean envíos por aire, tierra y agua según la empresa de logística (DHL, FedEx, UPS).

El UML muestra la jerarquía de clases con:

Una interfaz Envio → Implementada por envíos específicos (EnvioAereo, EnvioTerrestre, EnvioMaritimo).
Una EnvioFactory abstracta → Define los métodos para crear envíos.
Fábricas concretas (DHLFactory, FedExFactory) → Implementan la fábrica con sus propias reglas.
Métodos exclusivos → Cada empresa de envíos puede tener servicios adicionales.
