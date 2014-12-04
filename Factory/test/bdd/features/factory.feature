Feature: Factory Design Pattern
         
         As a user I wish to be able to access files from a particular website (Example: ftp.freebsd.org)
        
	Scenario Outline: Retrieve/Download  files
	Given I run factory file for http
	When it finishes getting the files from the site
	Then I can see the following files http:
	|files	 	    	  				|
	|../								|
	|CERT/							|
	|CTM/							|
	|CVSup/						|
	|ERRATA/						|
	|ISO-IMAGES-amd64/			|
	|ISO-IMAGES-i386/			|
	|ISO-IMAGES-ia64/			|
	|ISO-IMAGES-pc98/			|
	|ISO-IMAGES-powerpc/		|
	|ISO-IMAGES-powerpc64/	|
	|ISO-IMAGES-sparc64/		|
	|branches/						|
	|development/				|
	|distfiles/						|
	|doc/							|
	|ports/							|
	|releases/						|
	|snapshots/					|
	|tools/							|
	|updates/						|
	|README.TXT					|
	|TIMESTAMP					|
	|dir.sizes						|

	Scenario Outline: Retrieve/Download  files
	Given I run factory file for ftp
	When it finishes getting the files from the site
	Then I can see the following files ftp:
	|files	 	    	  										|
	|CERT													|
	|CTM -> development/CTM							|
	|CVSup -> development/CVSup						|
	|ERRATA												|
	|ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES 			|
	|ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES					|
	|ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES					|
	|ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES						|
	|ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES	|
	|ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES	|
	|ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES	|
	|README.TXT					|
	|TIMESTAMP					|
	|branches						|
	|development					|
	|dir.sizes						|
	|distfiles -> ports/distfiles	|
	|doc							|
	|ports							|
	|releases						|
	|snapshots					|
	|tools							|
	|updates						|
	

	
	
	
     
	
        

