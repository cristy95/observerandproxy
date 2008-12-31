Feature: Show Observers

		As I user I want to see the time observers

Scenario: show observers
	Given observer.py is running
	When the processes are done
	Then I should see the following:
		|observers 			|
		|Observer usa_time_observer says: 2009-01-01 01:03AM |
		|Observer usa_time_observer says: 2009-01-01 01:03AM |
		|Observer eu_time_observer says: 2009-01-01 01:03 	 |
		|Observer eu_time_observer says: 2009-01-01 01:03 	 |
