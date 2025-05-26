import temperature as temp
def test_temprature():
    test = temp.process_temperature(90)
    expect = "hot"
    assert(test == expect)