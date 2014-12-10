Feature: Facade Design Pattern: Able to count the reference links to a certain object upon creation and deletion
         
         As a user I wish to be able to know if the number of reference links are consistent when I add and then delete the	 		referential links
        
	Scenario Outline: Get number of referential links to an object
	Given I run proxy file
	When it finishes creating the main object 
	And after creating the references to that object
	And then deletes the said references
	Then I can see the following:
	|References																		|							
	|Number of references after creating all the references: 3						|										
	|Number of references after deleting the references: 0						|