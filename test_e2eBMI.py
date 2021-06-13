import pytest
from selenium import webdriver

# @pytest.mark.usefixtures("setup")
from TestData.HomePagedata import homePageData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2eBmi(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.davinder)

        # 1st way to do
        # dropdown = Select(homePage.getGander())
        # dropdown.select_by_visible_text("Male")
        # second Way to do use define method in base class and call from here
        self.selectOptionByText(homePage.getGander(), getData["Gander"])
        homePage.getHeight().send_keys(getData["Height"])
        homePage.getInch().send_keys(getData["Inch"])
        homePage.doCalculation().click()
        # print(self.davinder.find_element_by_id("message").text)
        Message = homePage.getMessage().text
        log.info("Message is " + Message)
        # assert ("Correct Info" in Message)
        # self.davinder.refresh()

        # print the input value we use ( .get attribute('value)
        print('Your Weight is =', self.davinder.find_element_by_id("input").get_attribute('value'))
        print('Your BMI is =', self.davinder.find_element_by_id("bm").get_attribute('value'))
        print('Your Weight is =', self.davinder.find_element_by_id("protien").get_attribute('value'))
        self.davinder.get_screenshot_as_file("success.png")

    @pytest.fixture(params=homePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
