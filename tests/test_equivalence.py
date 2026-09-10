import pytest

from planilla.calculo import (
    bonificacion_incentivo,
    descuento_prestamo,
    pago_horas_extra,
    valor_hora,
)


def test_salario_base_valido():
    assert valor_hora(4800) == 999


def test_salario_base_invalido():
    with pytest.raises(ValueError):
        valor_hora(-100)


def test_horas_extra_validas():
    assert pago_horas_extra(2400, 10) == 150


def test_horas_extra_invalidas():
    with pytest.raises(ValueError):
        pago_horas_extra(2400, 50)


def test_dias_trabajados_validos():
    assert bonificacion_incentivo(15) == 125


def test_dias_trabajados_invalidos():
    with pytest.raises(ValueError):
        bonificacion_incentivo(35)


def test_cuota_prestamo_valida():
    assert descuento_prestamo(3000, 4000, 500) == 500


def test_cuota_prestamo_invalida():
    with pytest.raises(ValueError):
        descuento_prestamo(3000, 4000, -100)