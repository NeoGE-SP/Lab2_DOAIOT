import temp

def test_minmax():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 90]

    result = temp.find_min_max(input_arr)

    assert (result == test_arr)

def test_average():
    input_arr = [1, 2, 3]
    average = 2.0

    result = temp.calc_average(input_arr)

    assert (result == average)


def test_median():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = temp.sort_temperature(input_arr)
    
    test_arr = 25

    result = temp.cal_median_temp(sorted_arr)

    assert (result == test_arr)
