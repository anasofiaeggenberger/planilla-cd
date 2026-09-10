import pytest

from planilla.calculo import (
    descuento_igss,
    descuento_prestamo,
    isr_anual,
)


@pytest.mark.parametrize(
    "afiliado, esperado",
    [
        (True, 483.0),
        (False, 0.0),
        (None, 0.0),
    ],
)
def test_tabla_decision_igss(afiliado, esperado):
    assert descuento_igss(10000, afiliado) == esperado


@pytest.mark.parametrize(
    "liquido_antes, salario_ordinario, cuota, esperado",
    [
        (3000, 4000, 500, 500),
        (1500, 4000, 500, 300),
        (1200, 4000, 500, 0),
        (1000, 4000, 500, 0),
    ],
)
def test_tabla_decision_prestamo(
    liquido_antes, salario_ordinario, cuota, esperado
):
    assert (
        descuento_prestamo(liquido_antes, salario_ordinario, cuota)
        == esperado
    )


@pytest.mark.parametrize(
    "renta_bruta_anual, esperado",
    [
        (48000, 0),
        (148000, 5000),
        (448000, 22000),
    ],
)
def test_tabla_decision_isr(renta_bruta_anual, esperado):
    assert isr_anual(renta_bruta_anual) == esperado