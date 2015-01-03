Feature: Template Design Pattern; Able to get the top news on Google and Yahoo
	
	As a user I wish to be able to view the top news on Google and Yahoo

	Scenario Outline: Get top news from Google and Yahoo
	Given I run template file
	When it has already gathered the top news from Google and Yahoo
	Then I can see the following:
