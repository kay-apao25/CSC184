Feature: Observer Design Pattern: Able to add USA and Europe time Observers
         
         As a user I wish to be able to know the time in USA and Europe
        
	Scenario Outline: Get 12-hour format and 24-hour time format
	Given I run observer file
	When it registers the first observer and displays the 12-hour time format 
	And it registers another server and displays both the 12-hour and 24-hour time format
	And then unregisters the first observer and display the 24-hour format
	Then I can see the following:
	|Processes																		|							
	|Adding usa_time_observer   													|
	|Observer usa_time_observer says: 2014-12-10 07:26PM						|										
	|Adding eu_time_observer														|
	|Observer usa_time_observer says: 2014-12-10 07:26PM						|
	|Observer eu_time_observer says: 2014-12-10 19:26							|
	|Removing usa_time_observer													|
	|Observer eu_time_observer says: 2014-12-10 19:26							|