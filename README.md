# Physics Formula Generator 
## Project Overview
A web app that displays random physics formulas and explanations at the click of a button! Built with a serverless AWS architecture and a responsive front-end using HTML, CSS, and JavaScript. 

## Features
- Fetches random physics formulas from DynamoDB using an AWS Lambda function.
- Responsive front-end design suitable for desktop and mobile.
- Website is hosted on Amazon S3, with fast API calls to AWS Lambda via API Gateway.
- Easy to extend by addding new formulas to the DynamoDB.

  ## Technologies Used
- **Front-end:** HTML, CSS, JavaScript
- **Back-end:** AWS Lambda, API Gateway, Python
- **Database:** DynamoDB
- **Hosting:** Amazon S3
 
  ## Architecture
- **Front-end:** HTML/CSS/JS website hosted on S3
- **API:** AWS Lambda function handles formula requests
- **Database:** DynamoDB stores physics formulas and explanations
- **API Gateway:** Connects front-end requests to Lambda function
 
   *(Optional: include a simple diagram here)*

   ## Getting Started / Usage
- Visit the live demo: [Physics Formula Generator](https://your-live-website-link.com)
- Click the **"Get Formula"** button to see a random physics formula and explanation.
- The Lambda function fetches a random entry from DynamoDB and returns it as JSON.
