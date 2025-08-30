from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_basic2():
    assert bound_to_180(360) == 0.0


def test_bound_with180():
    assert bound_to_180(180.0) == -180.0


def test_bound_with_neg180():
    assert bound_to_180(-180.0) == -180.0


def test_bound_with_neg_multiple_in_btw():
    assert bound_to_180(-990.0) == 90.0


def test_bound_with_pos_multiple_in_btw():
    assert bound_to_180(990.0) == -90.0


def test_bound_with_neg_num():
    assert bound_to_180(-350.0) == 10.0


def test_bound_with_pos_num():
    assert bound_to_180(350.0) == -10.0


def test_bound_with_pos_float():
    assert bound_to_180(1378.5) == -61.5


def test_bound_with_pos_num_in_btw():
    assert bound_to_180(910) == -170


def test_bound_with_neg_float():
    assert bound_to_180(-3430.5) == 169.5


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_given_example1():
    assert is_angle_between(0, 45, 90)


def test_between_given_example2():
    assert not is_angle_between(45, 90, 270)


def test_between_all_multiples_of_360():
    assert is_angle_between(360, 0, 720)


def test_between_all_multiples_of_360_reversed():
    assert is_angle_between(720, 0, 360)


def test_edge_case_with_180():
    assert is_angle_between(0, 270, 180)


def test_edge_case_neg_first_angle():
    assert is_angle_between(-350, 5, 300)


def test_edge_case_neg_mid_angle():
    assert not is_angle_between(230, -340, 180)


def test_edge_case_neg_sec_angle():
    assert is_angle_between(110, 90, -60)


def test_edge_case_all_neg_angles():
    assert not is_angle_between(-20, -90, -340)


def test_edge_case_all_floats():
    assert not is_angle_between(23.4, 90.8, 760.9)
