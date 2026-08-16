# AWS Serverless Todo API AWS 无服务器 Todo API

A serverless REST API built with AWS Lambda, API Gateway and DynamoDB.
一个基于 AWS Lambda、API Gateway 和 DynamoDB 构建的无服务器 REST API。

## Architecture 架构

![Architecture](architecture.png)

## Features 功能

- GET /todos
- POST /todos
- DELETE /todos

## AWS Services AWS 服务

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- IAM

## API Example API 示例

GET

/todos


POST

{
"title":"Learn AWS",
"status":"doing"
}


DELETE

{
"id":"todo-id"
}

## Deployment 部署

Created using AWS Console.
使用 AWS 控制台创建。

## Lessons Learned 经验总结

- Lambda execution role configuration
- Lambda 执行角色配置

- DynamoDB CRUD operations
- DynamoDB CRUD 操作

- API Gateway integration
- API Gateway 集成

- CloudWatch debugging
- CloudWatch 调试

## Demo 演示

GET /todos response（返回）:

![API Response](demo.png)

## Project Status 项目状态

- This project has been completed and archived. The AWS infrastructure has been destroyed to avoid ongoing cloud costs. The source code, architecture diagram, screenshots, and deployment documentation are preserved for portfolio purposes.

- 本项目已完成并归档。为避免持续产生云资源费用，AWS 基础设施已销毁。源代码、架构图、截图及部署文档保留用于作品集展示。