Feature: Facade Design Pattern: Able to get the current temperature in London, UK
         
         As a user I wish to be able to know the current temperature of London, UK
        
	Scenario Outline: Get Current Temperature (London)
	Given I run facade file
	When it finishes checking the temperature of London from the site
	Then I can see the temperature "2.49"
	
	
	
     
	
        

