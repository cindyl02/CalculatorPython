import main
import pytest


def test_calculate_add_happy_paths(capfd, monkeypatch):
    inputs = ["1", "+", "2", "no", "1", "+", "-1", "no", "-1", "+", "-1", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.calculate()
    out, err = capfd.readouterr()
    assert "1.0 + 2.0 = 3.0\n" in out
    assert "1.0 + -1.0 = 0.0\n" in out
    assert "-1.0 + -1.0 = -2.0\n" in out
    assert "Bye!\n" in out


def test_calculate_subtract_happy_paths(capfd, monkeypatch):
    inputs = ["10", "-", "5", "no", "-1", "-", "1", "no", "-1", "-", "-1", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.calculate()
    out, err = capfd.readouterr()
    assert "10.0 - 5.0 = 5.0\n" in out
    assert "-1.0 - 1.0 = -2.0\n" in out
    assert "-1.0 - -1.0 = 0.0\n" in out
    assert "Bye!\n" in out


def test_calculate_multiply_happy_paths(capfd, monkeypatch):
    inputs = ["10", "*", "5", "no", "-1", "*", "1", "no", "-1", "*", "-1", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.calculate()
    out, err = capfd.readouterr()
    assert "10.0 * 5.0 = 50.0\n" in out
    assert "-1.0 * 1.0 = -1.0\n" in out
    assert "-1.0 * -1.0 = 1.0\n" in out
    assert "Bye!\n" in out


def test_calculate_divide_happy_paths(capfd, monkeypatch):
    inputs = ["10", "/", "5", "no", "-1", "/", "1", "no", "-1", "/", "-1", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.calculate()
    out, err = capfd.readouterr()
    assert "10.0 / 5.0 = 2.0\n" in out
    assert "-1.0 / 1.0 = -1.0\n" in out
    assert "-1.0 / -1.0 = 1.0\n" in out
    assert "Bye!\n" in out


def test_calculate_divide_throw_an_error(monkeypatch):
    inputs = ["10", "/", "0", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    with pytest.raises(ZeroDivisionError) as excinfo:
        main.calculate()
    assert str(excinfo.value) == "Cannot divide by 0!"


def test_calculate_another_calculation(capfd, monkeypatch):
    inputs = ["10", "/", "2", "yes", "*", "8", "yes", "/", "3", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.calculate()
    out, err = capfd.readouterr()
    assert "10.0 / 2.0 = 5.0\n" in out
    assert "5.0 * 8.0 = 40.0\n" in out
    assert "40.0 / 3.0 = 13.333333333333334\n" in out
    assert "Bye!\n" in out
