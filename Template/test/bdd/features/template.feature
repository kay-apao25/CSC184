Feature: Template Design Pattern; Able to get the top news on Google and Yahoo
	
	As a user I wish to be able to view the top news on Google and Yahoo

	Scenario Outline: Get top news from Google and Yahoo
	Given I run template file
	When it has already gathered the top news from Google and Yahoo
	Then I can see the following:
	| News 																						|
	| Tail of AirAsia plane located in Java Sea, Indonesian official says - Fox News			|
	| An inside look at the newest Alabama congressman's first day in D.C. - Yellowhammer News	|
	| FBI to question 'hundreds of witnesses' in hospital shooting - Washington Times			|
	| Tail of missing AirAsia jet located														|
	| FBI to question 'hundreds of witnesses' in hospital shooting								|
	| Group seeks new grand jury in Ferguson police shooting case								|
	
