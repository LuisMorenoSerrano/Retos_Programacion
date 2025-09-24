# Archivo README

## Estructura del Proyecto

```bash
ejercicios/
├── src/                   # Código fuente
│   ├── __init__.py
│   ├── reto_001.py        # Implementación de funcionalidades
│   ...
│   └── reto_NNN.py
├── tests/                 # Tests unitarios
│   ├── __init__.py
│   ├── test_reto_001.py   # Tests por funcionalidad (pytest)
│   ...
│   └── test_reto_NNN.py
├── README.md              # Este archivo
├── pyproject.toml         # Configuración del proyecto (pytest, Pylance, mypy)
├── pytest.ini             # Configuración adicional de pytest
└── requirements.txt       # Dependencias del proyecto
```

## Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt
```

## Uso de funcionalidades

```python
from src.reto_NNN import <funcion>
```

## Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con coverage
pytest --cov=src --cov-report=html

# Ejecutar test específico
pytest tests/test_reto_NNN.py

# Ejecutar tests en modo verbose
pytest -v
```

## Configuración del Proyecto

El proyecto utiliza `pyproject.toml` como archivo principal de configuración que incluye:

- **pytest**: Configuración para la ejecución de tests
  - Tests se buscan en el directorio `tests/`
  - Solo archivos que empiezan con `test_*.py`
  - Ejecución en modo verbose con trazas cortas

- **Pylance**: Configuración para análisis de código
  - Incluye los directorios `src/` para análisis
  - Añade `src/` al path para resolución de imports

- **mypy**: Configuración para chequeo de tipos
  - Path configurado para encontrar módulos en `src/`
  - Análisis de paquetes en el directorio `src/`

### Herramientas de Desarrollo

Para obtener el mejor experience de desarrollo, se recomienda instalar:

```bash
pip install pytest pytest-cov mypy
```
