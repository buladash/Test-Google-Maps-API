API Testing Framework — Google Maps API
framework for automating Google Maps API tests (CRUD: create → read → update → delete).
The framework demonstrates basic skills in working with:
Python
PyTest
Requests
JSON validation
Allure Report
Native utilities (logging, validation, HTTP methods)

Project structure:
tests/              # Test cases
utils/              # Helper modules (API client, checks, logging, HTTP methods)
logs/               # Request/response logs
test_results2/       # Raw test outputs (json/txt)

Test Scenario (CRUD):
POST — Create a new location
GET — Get a created location
PUT — Update an address
DELETE — Delete
GET (404) — Check that the location has been deleted
