def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    equiv_angle = angle % 360.0
    if equiv_angle >= 180.0:
        equiv_angle = equiv_angle - 360.0
    return equiv_angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    first_within_360 = first_angle % 360
    mid_within_360 = middle_angle % 360
    sec_within_360 = second_angle % 360

    if first_within_360 > sec_within_360:
        angle_difference = first_within_360 - sec_within_360
        if angle_difference >= 180:
            return not (sec_within_360 <= mid_within_360 <= first_within_360)
        else:
            return sec_within_360 <= mid_within_360 <= first_within_360
    else:
        angle_difference = sec_within_360 - first_within_360
        if angle_difference >= 180:
            return not (first_within_360 <= mid_within_360 <= sec_within_360)
        else:
            return first_within_360 <= mid_within_360 <= sec_within_360
