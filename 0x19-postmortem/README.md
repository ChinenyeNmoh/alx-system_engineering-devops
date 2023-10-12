# Apache Server Postmortem Report
### [504 Error while accessing a given URL](https://world.siteground.com/kb/504-gateway-timeout/#:~:text=The%20504%20(Gateway%20Timeout)%20status,toward%20the%20server%20or%20site.)
![What caused this!](https://assets-global.website-files.com/5c51758c58939b30a6fd3d73/63954b879834c146bbb418fc_retrospectives-p-500.webp)
## Date: October 12, 2023


## Summary
This postmortem report provides an analysis of the incident that occurred on October 12, 2023, involving the Apache server. The incident led to a 504 error for anyone trying to access a website for approximately 30 minutes, impacting the availability of our website and API endpoints. This report aims to identify the root cause, document the mitigation steps taken, and propose preventive measures to avoid similar incidents in the future.

## Incident time Details

- 10:00 AM PST:Issue: 500 error for anyone trying to access the website.
- 10:05 AM PST:Process: Ensuring Apache and MySQL are up and running.
- 10:10 AM PST:Observation: The website was not loading properly. A background check revealed that the server and database were working properly.
- 10:12 AM PST:Action: Quick restart of Apache server. Result: Server returns a status of 200 and OK when trying to curl the website.
- 10:18 AM PST:Action: Reviewing error logs to identify the source of the error.
- 10:25 AM PST:Action: Checking /var/log to see that the Apache server was being prematurely shut down. The error log for PHP was not found.
- 10:30 AM PST:Action: Checking php.ini settings, which revealed that all error logging had been turned off. Turning error logging on.
- 10:32 AM PST:Observation: Reviewing error logs for PHP revealed a mistyped file name, which was causing incorrect loading and premature closing of Apache.
- 10:31 AM PST:Action: Fixing the file name.
- 10:40 AM PST:Result: Server is now running normally, and the website is loading properly.
Impact: The website and API endpoints were inaccessible, leading to customer dissatisfaction and potential revenue loss.

## Root Cause Analysis

The issue was caused by a wrong file name referenced in the wp-settings.php file, leading to a 500 error when trying to access the server. Initially, the absence of PHP error logs and limited information in the Apache default error log made it challenging to identify the problem.

Upon investigation, it was discovered that error logging for PHP was turned off in the php.ini file. After enabling error logging and restarting the Apache server, it became evident that the issue was due to a misspelled file extension (.phpp) in the wp-settings.php file, preventing proper site access.

This problem may have affected other servers as well. To resolve it, the engineer deployed Puppet code to correct the misspelled file extensions across all servers, resulting in the successful loading of the site and server.

## Corrective and Preventive Measures
1. Enable Error Logging: Implement a policy to ensure that error logging is enabled on all servers and websites. This proactive measure allows for easier identification and troubleshooting of errors if issues arise.
2. Local Testing: Prior to deploying any updates or new websites on a multi-server setup, conduct thorough local testing. Local testing can help identify and correct errors before they go live, reducing downtime and the need for emergency fixes.