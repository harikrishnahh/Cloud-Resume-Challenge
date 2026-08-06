# ☁️ Cloud Resume Challenge

A fully serverless resume website built on AWS as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/).

🔗 **Live Site:** [d32kvvpvx64e3a.cloudfront.net](https://d32kvvpvx64e3a.cloudfront.net)

---

## Architecture

Browser → CloudFront → S3 (index.html)
↓
JavaScript fetch()
↓
API Gateway → Lambda (Python) → DynamoDB
---

## Tech Stack

| Layer | Technology |
|---|---|
| Hosting | AWS S3 (Static Website) |
| CDN / HTTPS | AWS CloudFront |
| Visitor Counter API | AWS API Gateway |
| Backend Logic | AWS Lambda (Python) |
| Database | AWS DynamoDB |
| CI/CD | GitHub Actions |
| Frontend | HTML, Tailwind CSS, JavaScript |

---

## Repository Structure
cloud-resume/
├── frontend/
│ └── index.html # Resume webpage
├── backend/
│ ├── lambda_function.py # Visitor counter Lambda
│ └── test_lambda.py # Python unit tests
└── .github/workflows/
├── frontend.yml # Deploy to S3 + invalidate CloudFront
└── backend.yml # Run Python tests
---

## CI/CD

- **Frontend:** Pushing to `frontend/` triggers automatic S3 upload and CloudFront cache invalidation
- **Backend:** Pushing to `backend/` triggers Python unit tests via pytest

---

## How the Visitor Counter Works

1. Page loads and JavaScript calls the API Gateway endpoint
2. API Gateway triggers a Lambda function
3. Lambda increments the count in DynamoDB and returns the updated value
4. JavaScript displays the live count on the page

