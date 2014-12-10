Feature: Observer Design Pattern: Able to add USA and Europe time Observers
         
         As a user I wish to be able to know the time in USA and Europe
        
	Scenario Outline: Get number of referential links to an object
	Given I run proxy file
	When it finishes creating the main object 
	And after creating the references to that object
	And then deletes the said references
	Then I can see the following:
	|References																		|							
	|Number of references after creating all the references: 3						|										
	|Number of references after deleting the references: 0						|