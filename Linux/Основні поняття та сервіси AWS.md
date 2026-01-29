1. How Internet Works (основи мережі)

IP addresses
DNS (Domain Name System)
Route 53 — AWS DNS service
Packets, TCP/IP

2. AWS Networking

VPC (Virtual Private Cloud) — ізольована мережа в хмарі
Public vs Private Subnets
Internet Gateway (IGW) — для публічного доступу
NAT Gateway — для виходу приватних subnet в інтернет (без вхідного трафіку)
Security Groups — stateful firewall (на рівні інстансів)
Network ACLs — stateless firewall (на рівні subnet)

3. How a Website Actually Works

Static content → S3 (Simple Storage Service) + CloudFront (CDN для кешування та глобальної доставки)
Dynamic backend → Elastic Load Balancer (ELB / ALB) + Auto Scaling

4. Compute / Running backend

Serverless: API Gateway + Lambda (functions as a service, автоматичне масштабування)
Traditional: EC2 (Elastic Compute Cloud) — віртуальні сервери, повний контроль
Containers: ECS (Elastic Container Service) — для мікросервісів / Docker

5. Storage & Databases

Object storage: S3 — файли, images, backups, статичний контент
Relational (SQL): RDS (Relational Database Service) — managed PostgreSQL, MySQL, etc.
NoSQL: DynamoDB — key-value та document DB, висока швидкість і масштаб

6. AI and Machine Learning

Amazon Bedrock — managed foundation models (LLMs), RAG (Retrieval-Augmented Generation), chatbots
SageMaker — повний lifecycle ML: build, train, deploy custom models (наприклад, прогнози)

7. Security (основні принципи)

IAM (Identity and Access Management) — users, roles, policies, least privilege
VPC isolation
Defense in depth (багатошаровий захист)
Security Groups + NACLs + IAM + encryption

8. Monitoring and Auditing

CloudWatch — metrics, logs, alarms, dashboards, autoscaling triggers
CloudTrail — logging всіх API calls, аудит, compliance

Короткий огляд логіки (big picture)

Клієнт → DNS (Route 53) → CloudFront + S3 (static) або ALB → compute (EC2 / Lambda / ECS) → DB (RDS / DynamoDB)
Security всюди: IAM + VPC + Security Groups
Monitoring: CloudWatch + CloudTrail
Scalability: Auto Scaling, serverless де можливо

- **VPC** isolates your entire network
- **Public and private subnets** separate your internet-facing resources from your internal ones
- **NAT Gateways** give your private resources controlled internet access when needed
- **Network ACLs** protect traffic at the subnet level
- **Security Groups** provide detailed control at the resource level
- **IAM** ensures that every component only has the permissions it absolutely needs

## Security 

**GuardDuty**
- Threat Detection

**KMS**
- Encryption Key Management

**Shield & WAF**
- Protection Against Cyber Attacks

##  Monitoring systems

**CloudWatch** 
- Operational Impact

**CloudTrail**
- What Caused The Issue

#sh01