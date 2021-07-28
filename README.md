# AmazonUSA-SDETProject
This is the Automation suite for Amazon.com 

## How to execute it (On Windows) 
  1. Clone the directory in to your computer 
  2. Open CMD on windows
  3. cd to the directory where the repository was cloned 
  4. input "py.test" command on the console
  5. The Webdriver will start executing the script 
  6. Once it has finished, navigate to /reports on your clone directory and locate the new report for this run generated 

## This automation suite was created  using the following tools:

- Selenium Webdriver 3.141.0 
- Python 3.9 
- [Pytest](https://docs.pytest.org/en/6.2.x/) as framework
- [ChromeDriver 92.0.4515.43](https://chromedriver.chromium.org/home) 
- Some custom libraries: 
-- [Requests](https://docs.python-requests.org/en/master/): For API call
--  [pytest-html](https://pytest-html.readthedocs.io/en/latest/index.html#) For reporting 

The suite is organized under Page Object Model (POM) , it contains the following directory, please below find a brief description of each one. 

### pageObject 
It contains a class per each page involved on the required test cases, , on this clases, constructors, locators and methods are declared and encapsulated  
### report 
This directory will be used to store the HTML repors once the pytest commands has finished 
### testData
It contains clases where the data use on eac  
### test 
It contain classes for the test cases required, it will enhirent all the method from pageObject clases to performed the steps, assertion are included on this clases, as well as data loader to bring data from testData classes 
### utilities 

