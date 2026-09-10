import sys

from planilla.cli import main, parse_args


def test_parse_args_numericos():
    datos = parse_args(
        [
            "salario_base=4000",
            "horas_extra=8",
            "dias_trabajados=30",
            "cuota_prestamo=500",
        ]
    )

    assert datos["salario_base"] == 4000
    assert datos["horas_extra"] == 8
    assert datos["dias_trabajados"] == 30
    assert datos["cuota_prestamo"] == 500


def test_parse_args_texto():
    datos = parse_args(["afiliado_igss=no"])

    assert datos["afiliado_igss"] == "no"


def test_parse_args_ignora_argumento_sin_igual():
    datos = parse_args(["salario_base=4000", "invalido"])

    assert datos == {"salario_base": 4000}


def test_main_sin_salario_base(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["planilla"])

    resultado = main()
    salida = capsys.readouterr()

    assert resultado == 1
    assert "uso: planilla" in salida.out


def test_main_planilla_completa(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "planilla",
            "salario_base=4000",
            "horas_extra=8",
            "dias_trabajados=30",
            "cuota_prestamo=500",
            "afiliado_igss=si",
        ],
    )

    resultado = main()
    salida = capsys.readouterr()

    assert resultado == 0
    assert "Liquido:" in salida.out
    assert "Descuentos:" in salida.out


def test_main_sin_igss(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "planilla",
            "salario_base=4000",
            "afiliado_igss=no",
        ],
    )

    resultado = main()
    salida = capsys.readouterr()

    assert resultado == 0
    assert "Liquido:" in salida.out