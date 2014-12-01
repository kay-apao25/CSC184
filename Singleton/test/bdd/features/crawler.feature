Feature: Singleton Design Pattern Uploads images
         
         As a user I wish to be able to download pictures
        
	Scenario Outline: Retrieve/Download  images
	Given I visit page "http://localhost/about.html"
	And crawler file is running
	When it finishes getting the images from the site
	Then I can see the image "tpcmast.jpg"
	
     
	
        

