Feature: I can search for degrees

Scenario:
    Given I am on the home page
    When I go to the study page
    And I search for courses using the search term "computing"
    Then I can see a list of computing courses with titles that contain the term "computing" or "computer"