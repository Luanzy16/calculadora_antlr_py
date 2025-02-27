# Calculadora con ANTLR y Python

Este proyecto implementa una calculadora funcional utilizando ANTLR para el análisis sintáctico y Python para la evaluación de expresiones matemáticas.

## Integrantes

- Luis Sánchez
- David Bermudez
- Santiago Ospina

## 🛠️ Instalación y Configuración

### 1️⃣ Instalar ANTLR4 en Linux / macOS

Si aún no tienes ANTLR instalado, sigue estos pasos:

```sh
curl -O https://www.antlr.org/download/antlr-4.13.0-complete.jar
alias antlr4='java -jar antlr-4.13.0-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```

### 2️⃣ Instalar ANTLR en Python

Ejecuta el siguiente comando para instalar ANTLR y sus dependencias en Python:

```sh
pip install antlr4-python3-runtime
```

## 🌍 Creación de un Entorno Virtual

Es recomendable usar un entorno virtual en Python para evitar conflictos de dependencias. Para crearlo y activarlo, sigue estos pasos:

```sh
python3 -m venv mi_entorno
source mi_entorno/bin/activate
```

Luego, instala las dependencias dentro del entorno:

```sh
pip install antlr4-python3-runtime
```

## 🚀 Generar los Archivos de ANTLR

Antes de ejecutar el programa, debes generar los archivos de ANTLR:

```sh
antlr4 -visitor -Dlanguage=Python3 calculadora.g4
```

Esto generará los archivos necesarios:
- `CalculadoraLexer.py`
- `CalculadoraParser.py`
- `CalculadoraVisitor.py`

## ▶️ Ejecutar la Calculadora

Para iniciar la calculadora, usa el siguiente comando:

```sh
python main.py
```

Ejemplo de uso:

```
>>> 5 + 3 * 2
Resultado: 11.0
>>> (10 - 2) / 4
Resultado: 2.0
>>> exit
```



