from ..src.game.caissesurprise import CaisseSurprise


def test_get_list_caisses_surprises():
    list_caisses_surprises = CaisseSurprise.get_list_caisses_surprises()
    assert type(list_caisses_surprises) == list
    for caisse_surprise in list_caisses_surprises:
        assert isinstance(caisse_surprise, CaisseSurprise)


def test_get_name_caisse_surprise():
    caisse_suprise = CaisseSurprise(name="Nom de la caisse", image_surprise="🏹", case_surprise=22, ajout_pt_attack=1, ajout_pt_vie=2)
    name_caisse_surprise = caisse_suprise.get_name()
    assert name_caisse_surprise == "Nom de la caisse"


def test_repr():
    caisse_surprise = CaisseSurprise("Arc", "🏹", 1, 2, 3)
    assert repr(caisse_surprise) == caisse_surprise.image_surprise