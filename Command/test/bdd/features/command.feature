Feature: Command Design Pattern; Able to create and delete files
	
	As a user I wish to be able to create and delete a file

	Scenario Outline: Create and delete a file in the current diirectory
	Given I run command file
	When it creates and deletes a file
	The I can see the following:
	|Processes											|
	|Content of dir: myFile command.py test_file  		|
	|Content of dir: myFile .test_file command.py  		|
