#  Pre-entrega: Automatización QA

Autora: Ariadna Arias
Fecha: Octubre - 2025

##  Descripción del proyecto

Proyecto de automatización de pruebas funcionales desarrollado en Python, utilizando Selenium WebDriver y Pytest sobre el sitio SauceDemo.

Este trabajo forma parte de la pre-entrega de Automatización QA, y tiene como objetivo aplicar los conocimientos adquiridos en las clases iniciales, automatizando flujos básicos de navegación, interacción y validación visual mediante capturas de pantalla y reportes HTML.

##  Propósito del proyecto

Validar mediante pruebas automatizadas que las funciones principales del sitio SauceDemo se comporten correctamente, asegurando que:

✅ El login con credenciales válidas redirija correctamente al inventario.

🛍️ Los productos del catálogo se muestren de forma completa y correcta.

🛒 Al agregar un producto al carrito, este se registre y visualice adecuadamente.

##  Tecnologías utilizadas

Python → lenguaje 

Pytest → estructura de testing

Selenium WebDriver → automatización del navegador

WebDriver Manager → gestión automática del driver de Chrome

Pytest-HTML → generación de reportes en formato HTML

Git y GitHub → control de versiones y publicación del proyecto

## Instrucciones de instalación y ejecución

Instalar Python y comprobar la instalación en la consola con: python --v

Instalar Pytest y el plugin para generar el reporte de errores con: pip install pytest pytest-html

Instalar selenium con el comando en consola: pip install selenium

Instalar el manager del webdriven con el comando en consola: pip install webdriver-manager

Comando para ejecutar las pruebas
para generar un reporte HTML: pytest -v --html=reports/report.html --self-contained-html

Para hacer correr los tests sin el reporte, ejecutar el siguiente comando: pytest -v