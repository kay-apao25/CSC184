Feature: Singleton Design Pattern Uploads images
         
         As a user I wish to be able to download pictures
        
	Scenario Outline: Retrieve/Download  images
	Given I run crawler file
	When it finishes getting the images from the site
	Then I can see the image "tpcmast.jpg"
	
     
	
        

