# Project_12
EPIC EVENTS-API:  API providing customer informations
The EPIC EVENTS-AP project is a REST API application to be executed locally . It provides clients information from GET http endpoints. The API provides these endpoints 
to get detailed infomation about client filtered by name or sale contact. Endpoints allow users to retrieve information for individual client, contract and event
or a lists of all previous item.

Installation
This locally-executable API can be installed and executed from http://localhost:8000/api/ using the following steps.

Installation and execution (using venv and pip)
Clone this repository using $ git clone clone https://github.com/j-zouaoui/Project_12.git  (you can also download the code using as a zip file)
Move to the api root folder 
Activate the virtual environment with $ env\Scripts\activate on windows or $ source env/bin/activate on macos or linux.
Install project dependencies with $ pip install -r requirements.txt if request
Run the server with $ python manage.py runserver
When the server is running, the EPIC EVENTS-API can be requested from endpoints starting with the following base URL: http://localhost:8000/api/.
