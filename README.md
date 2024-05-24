# Selenium-Python-BDD-Framework
Website- E-commerce tutorials ninja <br>

developed and automate test scenarios for login and product search functionalities using BDD testing framework with selenium and python, integrating Data-driven testing (DDT), following the page object model (POM) pattern and Utilized allure reports for test result visualization.

**key Features** <br>

**Feature Files (Gherkin Syntax):** <br>
Define test scenarios in a human-readable format using Gherkin syntax.<br>
Clearly outline steps for login and product search functionalities

**Configuration:** <br>
Manage environment-specific configurations such as URLs and browser settings.<br>
Ensure seamless execution across different testing environments.

**Utilities :** <br>
Contains reusable functions or classes for tasks such as browser management, screenshot capture.<br>
Enhance the maintainability and flexibility of the framework.

**Page Object Model (POM):** <br>
Maintain a clear separation between test logic and web elements.<br>
Enhance script maintainability and scalability.

**Data-Driven Testing (DDT):** <br>
Execute test cases with multiple sets of input data.<br>
Improve test coverage and ensure the reliability of the automation suite.

**Allure Reports:** <br>
Generate detailed test execution reports using Allure.<br>
Provide comprehensive insights into test scenarios and steps.

# Commands to generate allure report
To run the test case with allure report<br>
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

view reports<br>
once the report generated you can view them in command prompt, opening the generated HTML files in web browser.<br>
allure serve %allure_result_folder%









