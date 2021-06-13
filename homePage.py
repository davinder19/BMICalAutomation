from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# create a constructor to get the driver from e2eBMI class

class HomePage:
    def __init__(self, davinder):
        self.davinder = davinder

    gander = (By.ID, "gander")
    height = (By.ID, "height")
    inch = (By.ID, "inch")
    calculate = (By.ID, "cal")
    message = (By.ID, "message")



    def getGander(self):
        return self.davinder.find_element(*HomePage.gander)  # star use just tell browser use it as tuple

    def getHeight(self):
        return self.davinder.find_element(*HomePage.height)  # star use just tell browser use it as tuple
    def getInch(self):
        return self.davinder.find_element(*HomePage.inch)  # star use just tell browser use it as tuple

    def doCalculation(self):
        return self.davinder.find_element(*HomePage.calculate)

    def getMessage(self):
        return self.davinder.find_element(*HomePage.message)