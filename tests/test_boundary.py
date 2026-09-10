import pytest

from planilla.calculo import (
    bonificacion_incentivo,
    descuento_prestamo,
    pago_horas_extra,
    valor_hora,
)


def test_salario_base_cero():
    with pytest.raises(ValueError):
        valor_hora(0)


def test_salario_base_justo_sobre_cero():
    assert valor_hora(0.01) > 0


def test_horas_extra_minimo():
    assert pago_horas_extra(2400, 0) == 0


def test_horas_extra_debajo_minimo():
    with pytest.raises(ValueError):
        pago_horas_extra(2400, -1)


def test_horas_extra_maximo():
    assert pago_horas_extra(2400, 48) == 720


def test_horas_extra_sobre_maximo():
    with pytest.raises(ValueError):
        pago_horas_extra(2400, 49)


def test_dias_trabajados_minimo():
    assert bonificacion_incentivo(0) == 0


def test_dias_trabajados_debajo_minimo():
    with pytest.raises(ValueError):
        bonificacion_incentivo(-1)


def test_dias_trabajados_maximo():
    assert bonificacion_incentivo(30) == 250


def test_dias_trabajados_sobre_maximo():
    with pytest.raises(ValueError):
        bonificacion_incentivo(31)


def test_cuota_prestamo_minima():
    assert descuento_prestamo(3000, 4000, 0) == 0


def test_cuota_prestamo_debajo_minimo():
    with pytest.raises(ValueError):
        descuento_prestamo(3000, 4000, -0.01)