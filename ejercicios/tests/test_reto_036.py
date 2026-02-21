"""Tests para RETO #036: BATALLA POKÉMON"""
import sys
import os

# Configurar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest           # pylint: disable=wrong-import-position
from reto_036 import (  # pylint: disable=import-error,wrong-import-position # type: ignore
    calcular_dano_pokemon, TipoPokemon, obtener_efectividad,
    mostrar_resultado_batalla, Efectividad
)


class TestObtenerEfectividad:
    """Tests para la función obtener_efectividad"""

    @pytest.mark.parametrize("tipo_atacante,tipo_defensor,efectividad_esperada", [
        # Súper efectivos (x2.0)
        (TipoPokemon.AGUA, TipoPokemon.FUEGO, 2.0),
        (TipoPokemon.FUEGO, TipoPokemon.PLANTA, 2.0),
        (TipoPokemon.PLANTA, TipoPokemon.AGUA, 2.0),
        (TipoPokemon.ELECTRICO, TipoPokemon.AGUA, 2.0),

        # No muy efectivos (x0.5)
        (TipoPokemon.AGUA, TipoPokemon.PLANTA, 0.5),
        (TipoPokemon.FUEGO, TipoPokemon.AGUA, 0.5),
        (TipoPokemon.PLANTA, TipoPokemon.FUEGO, 0.5),

        # Neutrales (x1.0)
        (TipoPokemon.AGUA, TipoPokemon.AGUA, 1.0),
        (TipoPokemon.FUEGO, TipoPokemon.FUEGO, 1.0),
        (TipoPokemon.PLANTA, TipoPokemon.PLANTA, 1.0),
        (TipoPokemon.ELECTRICO, TipoPokemon.ELECTRICO, 1.0),
        (TipoPokemon.AGUA, TipoPokemon.ELECTRICO, 1.0),
        (TipoPokemon.FUEGO, TipoPokemon.ELECTRICO, 1.0),
        (TipoPokemon.PLANTA, TipoPokemon.ELECTRICO, 1.0),
        (TipoPokemon.ELECTRICO, TipoPokemon.FUEGO, 1.0),
        (TipoPokemon.ELECTRICO, TipoPokemon.PLANTA, 1.0),
    ])
    def test_efectividades_parametrizadas(self, tipo_atacante, tipo_defensor, efectividad_esperada):
        """Test parametrizado para todas las combinaciones de efectividad"""
        efectividad = obtener_efectividad(tipo_atacante, tipo_defensor)
        assert efectividad == efectividad_esperada


class TestCalcularDanoPokemon:
    """Tests para la función principal calcular_dano_pokemon"""

    def test_calculo_dano_basico(self):
        """Test básico del cálculo de daño"""
        # Fórmula: 50 * (80 / 60) * 2.0 = 133.33...
        dano = calcular_dano_pokemon("Agua", "Fuego", 80, 60)
        assert abs(dano - 133.33333333333334) < 0.0001

    def test_calculo_dano_neutral(self):
        """Test con efectividad neutral"""
        # Fórmula: 50 * (75 / 75) * 1.0 = 50.0
        dano = calcular_dano_pokemon("Eléctrico", "Eléctrico", 75, 75)
        assert dano == 50.0

    def test_calculo_dano_no_muy_efectivo(self):
        """Test con efectividad reducida"""
        # Fórmula: 50 * (90 / 70) * 0.5 = 32.14...
        dano = calcular_dano_pokemon("Fuego", "Agua", 90, 70)
        assert abs(dano - 32.142857142857146) < 0.0001

    @pytest.mark.parametrize("tipo_atacante,tipo_defensor,ataque,defensa,dano_esperado", [
        ("Agua", "Fuego", 100, 50, 200.0),   # 50 * (100/50) * 2.0 = 200
        ("Planta", "Agua", 60, 40, 150.0),   # 50 * (60/40) * 2.0 = 150
        ("Fuego", "Planta", 80, 80, 100.0),  # 50 * (80/80) * 2.0 = 100
        ("Agua", "Planta", 40, 80, 12.5),    # 50 * (40/80) * 0.5 = 12.5
        ("Agua", "Agua", 50, 100, 25.0),     # 50 * (50/100) * 1.0 = 25
    ])
    def test_calculos_dano_parametrizados(self, tipo_atacante, tipo_defensor,
                                           ataque, defensa, dano_esperado):
        """Tests parametrizados para diferentes combinaciones de daño"""
        dano = calcular_dano_pokemon(tipo_atacante, tipo_defensor, ataque, defensa)
        assert abs(dano - dano_esperado) < 0.0001

    def test_uso_enums_directos(self):
        """Test usando enums directamente"""
        dano = calcular_dano_pokemon(TipoPokemon.PLANTA, TipoPokemon.AGUA, 85, 50)
        # 50 * (85/50) * 2.0 = 170.0
        assert dano == 170.0

    def test_mezcla_strings_y_enums(self):
        """Test mezclando strings y enums"""
        dano1 = calcular_dano_pokemon("Agua", TipoPokemon.FUEGO, 80, 60)
        dano2 = calcular_dano_pokemon(TipoPokemon.AGUA, "Fuego", 80, 60)
        dano3 = calcular_dano_pokemon(TipoPokemon.AGUA, TipoPokemon.FUEGO, 80, 60)

        # Todos deben dar el mismo resultado
        assert dano1 == dano2 == dano3


class TestValidaciones:
    """Tests para validaciones de entrada"""

    @pytest.mark.parametrize("ataque,defensa", [
        (0, 50),    # Ataque muy bajo
        (101, 50),  # Ataque muy alto
        (50, 0),    # Defensa muy baja
        (50, 101),  # Defensa muy alta
        (-10, 50),  # Ataque negativo
        (50, -10),  # Defensa negativa
    ])
    def test_rangos_estadisticas_invalidos(self, ataque, defensa):
        """Test para rangos de estadísticas inválidos"""
        with pytest.raises(ValueError, match="debe estar entre 1 y 100"):
            calcular_dano_pokemon("Agua", "Fuego", ataque, defensa)

    @pytest.mark.parametrize("ataque,defensa", [
        (1, 1),      # Valores mínimos
        (100, 100),  # Valores máximos
        (50, 75),    # Valores medios
        (1, 100),    # Ataque mínimo, defensa máxima
        (100, 1),    # Ataque máximo, defensa mínima
    ])
    def test_rangos_estadisticas_validos(self, ataque, defensa):
        """Test para rangos de estadísticas válidos"""
        # No debería lanzar excepción
        dano = calcular_dano_pokemon("Agua", "Fuego", ataque, defensa)
        assert isinstance(dano, float)
        assert dano > 0

    @pytest.mark.parametrize("tipo_invalido", [
        "Hielo", "Fantasma", "Dragón", "Acero", "Volador", "Psíquico", "", "agua", "FUEGO"
    ])
    def test_tipos_pokemon_invalidos(self, tipo_invalido):
        """Test para tipos de Pokémon inválidos"""
        with pytest.raises(ValueError, match="no válido"):
            calcular_dano_pokemon(tipo_invalido, "Agua", 50, 50)

        with pytest.raises(ValueError, match="no válido"):
            calcular_dano_pokemon("Agua", tipo_invalido, 50, 50)

    @pytest.mark.parametrize("ataque_invalido,defensa_invalida", [
        (50.5, 50),  # Ataque float
        (50, 50.5),  # Defensa float
        ("50", 50),  # Ataque string
        (50, "50"),  # Defensa string
        (None, 50),  # Ataque None
        (50, None),  # Defensa None
    ])
    def test_tipos_datos_invalidos(self, ataque_invalido, defensa_invalida):
        """Test para tipos de datos inválidos"""
        with pytest.raises(TypeError, match="deben ser números enteros"):
            calcular_dano_pokemon("Agua", "Fuego", ataque_invalido, defensa_invalida)


class TestMostrarResultadoBatalla:
    """Tests para la función mostrar_resultado_batalla"""

    def test_formato_resultado_super_efectivo(self):
        """Test del formato para ataque súper efectivo"""
        resultado = mostrar_resultado_batalla("Agua", "Fuego", 80, 60, 133.3)

        assert "Pokémon Agua (ATQ: 80) ataca a Pokémon Fuego (DEF: 60)" in resultado
        assert "Daño causado: 133.3" in resultado
        assert "¡Es súper efectivo!" in resultado

    def test_formato_resultado_no_muy_efectivo(self):
        """Test del formato para ataque no muy efectivo"""
        resultado = mostrar_resultado_batalla("Fuego", "Agua", 90, 70, 32.1)

        assert "Pokémon Fuego (ATQ: 90) ataca a Pokémon Agua (DEF: 70)" in resultado
        assert "Daño causado: 32.1" in resultado
        assert "No es muy efectivo..." in resultado

    def test_formato_resultado_neutral(self):
        """Test del formato para ataque neutral"""
        resultado = mostrar_resultado_batalla("Eléctrico", "Eléctrico", 75, 75, 50.0)

        assert "Pokémon Eléctrico (ATQ: 75) ataca a Pokémon Eléctrico (DEF: 75)" in resultado
        assert "Daño causado: 50.0" in resultado
        assert "Es efectivo." in resultado

    def test_formato_con_enums(self):
        """Test del formato usando enums"""
        resultado = mostrar_resultado_batalla(TipoPokemon.PLANTA, TipoPokemon.AGUA, 85, 50, 170.0)

        assert "Pokémon Planta (ATQ: 85) ataca a Pokémon Agua (DEF: 50)" in resultado
        assert "Daño causado: 170.0" in resultado
        assert "¡Es súper efectivo!" in resultado


class TestCasosEspeciales:
    """Tests para casos especiales y edge cases"""

    def test_ataque_minimo_defensa_maxima(self):
        """Test con ataque mínimo y defensa máxima"""
        dano = calcular_dano_pokemon("Agua", "Fuego", 1, 100)
        # 50 * (1/100) * 2.0 = 1.0
        assert dano == 1.0

    def test_ataque_maximo_defensa_minima(self):
        """Test con ataque máximo y defensa mínima"""
        dano = calcular_dano_pokemon("Agua", "Fuego", 100, 1)
        # 50 * (100/1) * 2.0 = 10000.0
        assert dano == 10000.0

    def test_estadisticas_iguales_efectividad_neutral(self):
        """Test con estadísticas iguales y efectividad neutral"""
        dano = calcular_dano_pokemon("Agua", "Agua", 50, 50)
        # 50 * (50/50) * 1.0 = 50.0
        assert dano == 50.0

    def test_todos_los_tipos_validos(self):
        """Test que verifica que todos los tipos de TipoPokemon son reconocidos"""
        tipos_validos = ["Agua", "Fuego", "Planta", "Eléctrico"]

        for tipo in tipos_validos:
            # No debería lanzar excepción
            dano = calcular_dano_pokemon(tipo, "Agua", 50, 50)
            assert isinstance(dano, float)
            assert dano > 0


class TestEnums:
    """Tests para las enumeraciones"""

    def test_tipo_pokemon_valores(self):
        """Test de los valores de TipoPokemon"""
        assert TipoPokemon.AGUA.value == "Agua"
        assert TipoPokemon.FUEGO.value == "Fuego"
        assert TipoPokemon.PLANTA.value == "Planta"
        assert TipoPokemon.ELECTRICO.value == "Eléctrico"

    def test_efectividad_valores(self):
        """Test de los valores de Efectividad"""
        assert Efectividad.SUPER_EFECTIVO.value == 2.0
        assert Efectividad.NEUTRAL.value == 1.0
        assert Efectividad.NO_MUY_EFECTIVO.value == 0.5

    def test_cantidad_tipos_pokemon(self):
        """Test que verifica que hay exactamente 4 tipos"""
        assert len(TipoPokemon) == 4

    def test_cantidad_efectividades(self):
        """Test que verifica que hay exactamente 3 efectividades"""
        assert len(Efectividad) == 3


if __name__ == "__main__":
    pytest.main([__file__])
