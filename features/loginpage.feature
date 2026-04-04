Feature: SauceDemo Login Functionality



#  Scenario: Verify login
#    Given  I open the SauceDemo login page
#    When  user enter username "Standard_user"
#    And   user enter password "secret_sauce"
#   And    user click login button
#  Then   user should see the products page

 Feature: SauceDemo Login

  Scenario Outline: Verify login for different users
    Given User is able to reach login url
    When User enters username in the username field "<username>"
    And User enters password in the password field "<password>"
    And User clicks on the login button
    Then User should be navigated to the landing page

  Examples:
    | username                  | password      |
    | standard_user             | secret_sauce  |
    | locked_out_user           | secret_sauce  |
    | problem_user              | secret_sauce  |
    | performance_glitch_user   | secret_sauce  |
    | error_user                | secret_sauce  |
    | visual_user               | secret_sauce  |