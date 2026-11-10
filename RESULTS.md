# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Misty Americana
- Step 0.12, results of the three runs without a session (optional): FAILED (401), FAILED (401), FAILED (401)
- Step 0.16, blocks of "how many of the three tools are excluded": 0 excluded, 1 excluded, 2 excluded, 3 excluded (all tools)

## Defect report
- Title: Excluding all cutting tools returns 500 with empty body
- Request: POST /api/pizza with body `{"excludedTools": ["Knife", "Scissors", "Pizza cutter"]}` and valid token
- Expected result: 400 Bad Request with a JSON error message explaining no tools are available
- Actual result: 500 Internal Server Error with empty body
- Severity: High, because the server returns an unhandled server error with no error message for the client to handle

## Part A
- Step A4, status codes when the other user reads, changes and deletes:
  - Read (GET): 404
  - Change (PUT): 400
  - Delete (DELETE): 400

## Part B
1. They can find real network issues, server configuration problems. Unit tests with stubs are still useful because they run instantly in memory and make it easy to sepecify the error.
2. Cause if all tests use the shared public token, it could modify or delete each other's data. In Project 2, we should use like unique record IDs so test runs stay independent.
3. Because QuickPizza runs behind a load balancer with multiple backend servers that don't share user data. Using one session keeps the AWSALB cookie so all our requests go to the same server where our user was created.
4. block that all 3 tools are excluded. Because 500 with an empty body gives no clue what went wrong, while 400 with a message lets the frontend tell the user to uncheck a tool. xfail keeps the defect documented and actively monitored while letting the overall test suite stay green.
5. Base choice needs 9 tests: 1 base test + (3 - 1) + (4 - 1) + (2 - 1) + (3 - 1) = 1 + 2 + 3 + 1 + 2 = 9. All combinations = 3 * 4 * 2 * 3 = 72 tests.
6. 404 , 400. I would expect 403 Forbidden since the user is authenticated but not authorized. 404 for read, and 400 for update and delete is misleading because the request syntax itself was valid.
7. 200 OK with a list of ratings. Defect because a made-up token should not be able to run. On a real system, an attacker could use this to read private user ratings without logging in.
8. An API test directly verifies status codes, response headers, and raw JSON data. A web UI test is required to verify the actual visual layout, responsive design, and browser-rendered UI elements.
