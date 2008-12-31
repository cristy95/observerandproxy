Feature: Create Proxys

Scenario: Instantiate Object
	Given an object is created and I run the proxy python file
	When It finishes the processes
	Then I should see the following number of references and count of objects deleted:
		|returns			|
		|Count of references = 1	|
		|Count of references = 2	|
		|Count of references = 3	|
		|Count of objects = 2		|
		|Count of objects = 1		|
		|Count of references = 0	|
		|Count of objects = 0		|

