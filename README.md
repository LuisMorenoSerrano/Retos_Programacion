# 🚀 Retos de Programación

Una colección completa de **34 desafíos de programación** resueltos en Python, diseñados para practicar y mejorar habilidades de programación.

## 📊 Estado del Proyecto

- ✅ **32/34 retos completados** (94.1% - todos funcionando correctamente)
- 🔧 **2 retos requieren dependencias externas**
- 📚 **84 funciones implementadas**
- 🏗️ **10 clases definidas**
- 🎯 **100% con type hints**

## 🗂️ Estructura del Proyecto

```
Retos_Programacion/
├── 2022/                   # Directorio principal con todos los retos
│   ├── reto_001.py        # FizzBuzz
│   ├── reto_002.py        # Anagramas
│   ├── reto_003.py        # Fibonacci
│   ├── ...                # Retos 004-032
│   └── reto_034.py        # Zodíaco Chino
├── requirements.txt        # Dependencias del proyecto
├── pyproject.toml         # Configuración del proyecto
└── README.md              # Este archivo
```

## 📝 Lista de Retos

| # | Nombre | Descripción | Estado | Dependencias |
|---|--------|-------------|---------|--------------|
| 001 | FizzBuzz | Números 1-100 con fizz/buzz | ✅ | - |
| 002 | Anagramas | Detectar si dos palabras son anagramas | ✅ | - |
| 003 | Fibonacci | Primeros 50 números de Fibonacci | ✅ | - |
| 004 | Números Primos | Encontrar primos entre 1-100 | ✅ | - |
| 005 | Área Polígonos | Calcular área de triángulo, cuadrado, rectángulo | ✅ | - |
| 006 | Aspect Ratio | Calcular aspect ratio de imagen desde URL | 🔧 | PIL, requests |
| 007 | Invertir Cadena | Invertir texto sin usar funciones built-in | ✅ | - |
| 008 | Contar Palabras | Contar frecuencia de palabras en texto | ✅ | - |
| 009 | Decimal a Binario | Conversión sin usar funciones built-in | ✅ | - |
| 010 | Código Morse | Conversión bidireccional morse-texto | 🔧 | unidecode |
| 011 | Expresiones Equilibradas | Verificar paréntesis, llaves, corchetes | ✅ | - |
| 012 | Eliminar Caracteres | Caracteres no comunes entre strings | ✅ | - |
| 013 | Palíndromo | Detectar palabras palíndromo | ✅ | - |
| 014 | Número de Armstrong | Verificar números de Armstrong | ✅ | - |
| 015 | Factorial Recursivo | Calcular factorial usando recursión | ✅ | - |
| 016 | Número Aleatorio | Generar números aleatorios sin random() | ✅ | - |
| 017 | MCD y MCM | Máximo común divisor y mínimo común múltiplo | ✅ | - |
| 018 | Tres en Raya | Detectar ganador en matriz 3x3 | ✅ | - |
| 019 | Tres en Raya Avanzado | Versión completa con validaciones | ✅ | - |
| 020 | Parando el Tiempo | Suma con retardo async/sync | ✅ | - |
| 021 | Suma con Delay | Implementación asíncrona de suma | ✅ | - |
| 022 | Calculadora | Calculadora con operaciones básicas | ✅ | - |
| 023 | Conjuntos | Elementos comunes/distintos entre listas | ✅ | - |
| 024 | Generador de Contraseñas | Crear contraseñas seguras | ✅ | - |
| 025 | Iteration Master | 5 formas diferentes de contar 1-100 | ✅ | - |
| 026 | Piedra, Papel, Tijera | Simulador de juego RPT | ✅ | - |
| 027 | Polígonos | Sistema de polígonos con herencia | ✅ | - |
| 028 | Vectores Ortogonales | Detectar vectores perpendiculares | ✅ | - |
| 029 | Máquina Expendedora | Simulador con cambio de monedas | ✅ | - |
| 030 | Ordenar Lista | Algoritmo burbuja personalizado | ✅ | - |
| 031 | Marco de Palabras | Crear marco de asteriscos para texto | ✅ | - |
| 032 | Años Bisiestos | Encontrar próximos años bisiestos | ✅ | - |
| 033 | El Segundo | Encontrar segundo número más grande | ✅ | - |
| 034 | Zodíaco Chino | Ciclo sexagenario chino por año | ✅ | - |

## 🛠️ Instalación y Uso

### Prerrequisitos
- Python 3.10 o superior
- pip (incluido con Python)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/LuisMorenoSerrano/Retos_Programacion.git
cd Retos_Programacion

# Instalar dependencias
pip install -r requirements.txt

# O instalar dependencias de desarrollo
pip install -e .[dev]
```

### Ejecutar un Reto
```bash
# Ejecutar un reto específico
cd 2022
python reto_001.py

# Ejecutar con argumentos (algunos retos los aceptan)
python reto_003.py 10  # Fibonacci con 10 números
```

## 📊 Análisis de Calidad del Código

### Fortalezas del Proyecto
- ✅ **100% de archivos con type hints**
- ✅ **97% de archivos con guard `if __name__ == "__main__"`**
- ✅ **Código funcional y bien estructurado**
- ✅ **Patrones de programación consistentes**
- ✅ **Buena organización de archivos**

### Áreas de Mejora Identificadas
- 📚 **0% cobertura de docstrings** - Falta documentación de funciones
- 🔧 **26% archivos con manejo de errores** - Necesita más validación
- 🧮 **Números mágicos** - Varios archivos con constantes hardcodeadas
- 📈 **Alta complejidad** - Algunos retos muy complejos (ej. reto_019: 53 puntos)

### Estadísticas de Complejidad
- **Promedio de complejidad**: 13.7 puntos
- **Archivos con alta complejidad** (>15): 9 archivos
- **Funciones más complejas**: reto_019 (Tres en Raya), reto_022 (Calculadora)

## 🔧 Dependencias Externas

Algunos retos requieren librerías adicionales:

### reto_006.py - Aspect Ratio de Imagen
```bash
pip install Pillow requests
```

### reto_010.py - Código Morse
```bash
pip install unidecode
```

## 🧪 Testing

Actualmente el proyecto **no tiene tests automatizados**. Esta es una oportunidad de mejora prioritaria.

### Estructura de Testing Propuesta
```
tests/
├── test_reto_001.py
├── test_reto_002.py
├── ...
└── conftest.py
```

### Ejecutar Tests (cuando se implementen)
```bash
pytest
pytest --cov=src  # Con cobertura
```

## 🎯 Roadmap de Mejoras

### Prioridad Alta
- [ ] Implementar suite completa de tests unitarios
- [ ] Agregar docstrings a todas las funciones
- [ ] Crear módulo con funciones utilitarias comunes
- [ ] Mejorar manejo de errores y validaciones

### Prioridad Media  
- [ ] Refactorizar retos con alta complejidad
- [ ] Eliminar números mágicos usando constants
- [ ] Crear benchmarks de rendimiento
- [ ] Agregar logging para debugging

### Prioridad Baja
- [ ] Migrar a estructura src/ y tests/
- [ ] Crear interfaz CLI unificada
- [ ] Agregar ejemplos de uso avanzados
- [ ] Documentación API completa

## 📈 Métricas del Proyecto

- **Total líneas de código**: ~2,500
- **Funciones implementadas**: 84
- **Clases definidas**: 10
- **Imports más comunes**: unicodedata (3), os (2), abc (2)
- **Promedio líneas por función**: ~30
- **Archivos con main guard**: 33/34 (97%)

## 🤝 Contribuciones

Las contribuciones son bienvenidas, especialmente en:
- Tests unitarios
- Documentación
- Optimizaciones de rendimiento
- Nuevos retos de programación

## 📄 Licencia

Este proyecto es de código abierto. Consulta el archivo LICENSE para más detalles.

---

**Autor**: Luis Moreno Serrano  
**Última actualización**: Septiembre 2024