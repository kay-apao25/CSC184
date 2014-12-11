Feature: Observer Design Pattern: Able to add USA and Europe time Observers
         
         As a user I wish to be able to know the time in USA and Europe
        
	Scenario Outline: Get 12-hour format and 24-hour time format
	Given I run observer file
	When it registers the usa and eu time observers 
	Then I can see the following:
	|Processes																	|							
	|Observer usa_time_observer says: 2014-12-11 11:44AM						|										
	|Observer eu_time_observer says: 2014-12-11 11:44							|
	