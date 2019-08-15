**Test cases for Alaska API**

**Python version:** 
python3.7

**Usage:** 
python3.7 -m unittest test_add_bear.py


**List of test cases to cover:**
```
POST			/bear - create
	1) for all bear types, check that bear can be created 
		- code 201 is returned
		- response body is correct and refers to the created bear
		- bear was actually added

	2) for all bear types, check that bear can not be created if any mandatory value is missing in POST request body
		- code 400 is returned
		- response body contains error message
		- bear wasn't added


GET			/bear - read all bears
	1) check that list of all bears is returned
		- code 200 is returned
		- response contains a list of bears
		- all bears have the same list of values: id, type, name, age
		- values are present for all bears


GET			/bear/:id - read specific bear
	1) check that bear is returned given a bear id
		- code 200 is returned
		- response contains single bear 
		- bears have list of values: id, type, name, age
		- values are correct, e.g. correspond to bear with given id

	2) check that bear is not returned for non-existing bear id
		- code 404 is returned
		- response body contains error message		


PUT			/bear/:id - update specific bear
	1) check that specific bear can be updated given a bear id and update parameters
		- code 200 is returned
		- specific bear is updated according to given parameters
		- other bears are not updated

	2) check that bear is not updated if update parameters are incorrect
		- code 400 is returned
		- bear is not updated

	3) There may be any of two cases below:
		3a) check that bears are not updated for non-existing bear id
			- code 404 is returned
			- response body contains error message
			- bears are not updated

		3b) check that bear is created for non-existing bear id
			- code 201 is returned
			- response body is correct and refers to the created bear
			- bear was actually added


DELETE			/bear - delete all bears
	1) check that all bears can be deleted
		- all bears are deleted, "read all bears" request returns empty list


DELETE			/bear/:id - delete specific bear
	1) check that specific bear can be deleted given a bear id
		- code 200 is returned
		- specific bear is deleted

	2) check that bear is not deleted for non-existing bear id
		- code 404 is returned
		- response body contains error message
		- bears are not deleted
```