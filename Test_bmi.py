import Lab2.bmi as bmi

print("Test_bmi")


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75,72)
    correctresult = 0
    assert (result==correctresult)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75,80)
    correctresult = 1
    assert (result==correctresult)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75,40)
    correctresult = -1
    assert (result==correctresult)