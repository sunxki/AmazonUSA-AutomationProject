# AmazonUSA-SDETProject
This is the Automation suite for Amazon.com 

## How to execute it (On Windows) 
  1. Clone the directory in to your computer 
  2. Open CMD on windows
  3. cd to the directory where the repository was cloned 
  4. input "py.test" command on the console
  5. The Webdriver will start executing the script 
  6. Once it has finished, navigate to /reports on your cloned directory and locate the new report for this run generated 

## Other CMD customized commands 
1. py.test -browser_name (default = **chrome**,   "firefox" available to run the script in geckodriver)
2. py.test -environment_name (default = **prod**,   "stg" available to get a different URL for another enviroment (Not provided))

## This automation suite was created  using the following tools:

- Selenium Webdriver 3.141.0 
- Python 3.9 
- [Pytest](https://docs.pytest.org/en/6.2.x/) as framework
- [ChromeDriver 92.0.4515.43](https://chromedriver.chromium.org/home) 
- Some custom libraries: 
-- [Requests](https://docs.python-requests.org/en/master/): For API call
--  [pytest-html](https://pytest-html.readthedocs.io/en/latest/index.html#) For reporting 

The suite is organized under Page Object Model (POM) , it contains the following directory, please below find a brief description of each one. 

### **pageObject**
It contains a class per each page involved on the required test cases, , on this clases, constructors, locators and methods are declared and encapsulated  
### **report**
This directory will be used to store the HTML repors once the pytest commands has finished 
### **testData**
It contains classes where the data use on each page is stored
### **test**
- **testCases:** It contain classes for the test cases required, it will enhirent all the method from pageObject clases to performed the steps, assertion are included on this clases, as well   as data loader to bring data from testData classes.

       File:test_first_test_case       	 Go to Amazon.com
						Search for Samsung Galaxy Note 20
						Verify Item is displayed on the screen and locate the first one, then store the price
						Click on the First Result
						Once in the details page compare this price vs the above one (first stored price)
						Click on Add to Cart.
						Go to Cart and verify again the price of the phone
						Delete Item
									     
	   File:test_second_test_case   	Go to Amazon main page
						Locate at the upper right corner the button: Hello, Sign In Account & lists and click on it
						Click on "New customer? Start right here"
						Fill Email field with the data from the API response [Firstname.Lastname@fake.com](mailto:Firstname.Lastname@fake.com)
						Locate the search bar and Search for Echo
						Locate "Echo support" options and click on it
						Following elements should be displayed: Getting Started, Wi-Fi and Bluetooth, Device Software and Hardware, TroubleShooting		

- **conftest:** It contains the setup up method linked to all the testcases clases using fixture to get browser on the URL provided (www.amazon.com). 


### **utilities**
It contains Base Class where all the recycled method are declared such as, API Call method,implicit waits, text generator and it was enherinted by all the test cases.
Additionally drivers for **Chrome** and **Firefox** are loaded here, required to run the scripts 

# Jenkins Job

Work in progress 



