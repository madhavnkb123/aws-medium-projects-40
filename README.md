# AWS Medium Projects – 40 Hands-On Projects

A practical collection of 40 intermediate AWS projects using Python and boto3.

## Projects
1. S3 File Upload
2. S3 Event → Lambda
3. S3 Presigned URLs
4. S3 Data Processing
5. DynamoDB CRUD
6. DynamoDB Query & Update
7. Lambda REST API
8. API Gateway + DynamoDB
9. SQS Producer
10. SQS + Lambda Worker
11. SNS Notifications
12. SNS Fan-Out
13. SES Email Automation
14. EC2 Instance Inventory
15. EC2 Start/Stop Automation
16. EBS Snapshot Automation
17. CloudWatch Custom Metrics
18. CloudWatch Alarms
19. Cost Explorer Report
20. AWS Cost-Saving Scanner
21. IAM Access-Key Audit
22. IAM User/Role Inventory
23. Secrets Manager
24. Systems Manager Parameter Store
25. Route 53 DNS Automation
26. CloudFront Invalidation
27. VPC Resource Inventory
28. Security Group Audit
29. Textract Document Extraction
30. Rekognition Image Analysis
31. Comprehend Sentiment Analysis
32. Translate Text API
33. Transcribe Audio
34. Athena Query Automation
35. Glue Data Catalog
36. EventBridge Scheduled Lambda
37. Step Functions Workflow
38. Serverless Monitoring Dashboard
39. Serverless CRUD App
40. Complete AWS Serverless Project

## Safety
Use IAM roles or the AWS credential chain. Never hard-code access keys. Audit/read-only projects are designed to report findings rather than modify resources unless explicitly documented.

## Common setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

## Project folders
Every numbered folder is an independent hands-on project. Check the source file for required environment variables and AWS resources.
aws configure
```

Each project contains its own README with setup notes and environment variables.


## Projects 41–100: Industry Teaching Track

These projects extend the original 40 into production-oriented teaching: storage governance, serverless reliability, API operations, observability, security, networking, databases, containers and deployment operations.

- 41–50: S3 and DynamoDB production patterns
- 51–60: Lambda production patterns
- 61–70: API Gateway, SQS, SNS and EventBridge operations
- 71–80: Observability, CloudTrail, Systems Manager and KMS
- 81–90: VPC, ALB and Auto Scaling operations
- 91–100: RDS, ElastiCache, OpenSearch, ECR and ECS

**Industry teaching focus:** architecture, IAM, monitoring, automation, reliability, security, cost awareness and deployment operations. Review every write/delete operation in a non-production AWS account before execution.
