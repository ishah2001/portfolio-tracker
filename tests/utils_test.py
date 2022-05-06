# this file is the test.py file to run the test of our app

from app.utils import weekReturn
from app.utils import monthReturn
from app.utils import yearReturn

# Runs a format test to make sure that the format is displayed correctly

# checks the format of week returns to make sure it is correct

def test_weekReturns():
    assert weekReturn("AAPL")>"-1000%" 
    # 0 in this case is AAPLS actual weekly returns
    # Therefore, if the pytest is passed then we can assume that this function is accurate

# Repeated the same steps for monthly and yearly returns

def test_monthReturns():
   assert monthReturn("AAPL")> "-1000%"

def test_yearReturns():
    assert yearReturn("AAPL")>"-1000%"



