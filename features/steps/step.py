from selenium.webdriver.common.by import By
from behave import given, when, then


@given('user has navigated to the Target Circle Benefits page')
def open_target_benefits_page(context):
    print('1')
    context.driver.get('https://www.target.com/circle/')

@when ('user navigates to the first benefit')
def navigate_to_first_benefit(context):
         benefit_list = context.find_elements(By.CSS_SELECTOR, "li[class*= 'BenefitCard']" )
         context.driver.find_element(By.CSS_SELECTOR, "benefit_list[0]")

@then('User will find that there are five programs available')
def verify_five_programs(context):
    print('3')
    benefit_list = context.find_elements('CSS_SELECTOR', "li[class*= 'BenefitCard']")
    assert len(benefit_list) == 5, 'There should be 5 benefits, but we found {}'.format(len(benefit_list))