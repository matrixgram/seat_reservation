def reserve_list(date):
    """
    input
    -----
    date: string it is a date format 'dd-mm-yyyy'

    return
    ------
    return: list
    [
        ['user_id', 'seat_id'],
        ...
    ]
    """
    retrun[
        ["123", "1"],
        ["321", "2"],
    ]


def is_user_exist(user_id):
    pass


def is_seat_exist(seat_id):
    pass


def is_seat_reserved(seat_id):
    pass


def is_seat():
    pass


def reservation(user_id, seat_id, date):
    """
    input
    -----
    user_id: string
    seat_id: string

    to-do
    -----
    for later optimize this function

    return
    ------
    result is a tuple
    (true,'Okay')

    (false, 'it is not exist seat_id')
    (false, 'it is not exist user_id')
    (false, 'it is reserved')
    (false, 'can't be reserved')
    (false, 'one seat per person')
    """
    if not is_user_exist(user_id):
        return (False, "it is not exist user_id")
    if not is_seat_exist(seat_id):
        return (False, "it is not exist seat_id")

    if not is_seat_enable():
        return (False, "can't be reserved")

    reserve_list = reserve_list()
    for r in reserve_list:
        pass
    return (true, "Okay")
