def reserve_list(date):
    """

    :param date: It is a date format 'dd-mm-yyyy' for get reserve list at this time.
    :type date: string

    
    """
    retrun[
        ["123", "1"],
        ["321", "2"],
    ]


def is_user_exist(user_id):
    """To-Do
    -----
    must complete this function

    :param user_id: 

    """
    return True


def is_seat_exist(seat_id):
    """To-Do
    -----
    must complete this function

    :param seat_id: 

    """
    return True


def is_seat_reserved(seat_id):
    """To-Do
    -----
    must complete this function

    :param seat_id: 

    """
    return True


def is_seat():
    """To-Do
    -----
    must complete this function


    """
    return True


def reservation(user_id, seat_id, date):
    """input
    -----
    user_id: string
    seat_id: string
    
    to-do
    -----
    for later optimize this function

    :param user_id: 
    :param seat_id: 
    :param date: 
    :returns: ------
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
