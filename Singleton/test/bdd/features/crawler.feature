Feature: Singleton Design Pattern Uploads images
         
         As a user I wish to be able to download pictures from a particular website (Example: http://tipidpc.com/)
        
	Scenario Outline: Cannot Retrieve/Download  images
	Given I do not run crawler file
	When it does not get the images from the site
	Then I cannot see the image "tpcmast.jpg"

	Scenario Outline: Retrieve/Download  images
	Given I run crawler file
	When it finishes getting the images from the site
	Then I can see the image "tpcmast.jpg"

	
	
	
     
	
        

