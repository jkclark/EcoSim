from lib.test_helpers import Bunch, create_test_world


def test_repr():
    cell = create_test_world().get_cell(3, 3)
    assert repr(cell) == 'WorldCell at (3, 3)'


def test_add_and_remove_animal():
    cell = create_test_world().get_cell(0, 0)
    assert cell.animals == []

    animal = Bunch(location=Bunch(x_pos=0, y_pos=0))
    cell.add_animal(animal)
    assert cell.animals == [animal]

    cell.remove_animal(animal)
    assert cell.animals == []


def test_remove_animal_no_such_animal(capsys):
    cell = create_test_world().get_cell(0, 0)
    assert cell.animals == []

    animal = Bunch(location=Bunch(x_pos=0, y_pos=0))
    cell.add_animal(animal)
    assert cell.animals == [animal]

    animal_not_present = Bunch()
    cell.remove_animal(animal_not_present)
    assert cell.animals == [animal]
    out, _ = capsys.readouterr()
    assert out == 'Error: Cannot remove animal from (0, 0).\n'
