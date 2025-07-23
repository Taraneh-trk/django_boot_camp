from project import check,check_email,check_phone

def test_check():
    assert check('09153038580',"tara@gmail.com") == True
    assert check('0915303858',"taragmail.com") == False

def test_check_email():
    assert check_email("kordi@gmail.com") == True
    assert check_email("tara@gamil.com") == False

def test_check_phone():
    assert check_phone("0915234") == False
    assert check_phone("09155892694") == True

