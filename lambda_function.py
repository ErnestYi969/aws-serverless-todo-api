dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("todos")


def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]


    if method == "GET":

        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }


    elif method == "POST":

        body = json.loads(
            event.get("body", "{}")
        )

        item = {
            "id": str(uuid.uuid4()),
            "title": body.get(
                "title",
                "Default Task"
            ),
            "status": body.get(
                "status",
                "pending"
            )
        }

        table.put_item(
            Item=item
        )

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }


    elif method == "DELETE":

        body = json.loads(
            event.get("body", "{}")
        )

        todo_id = body.get("id")

        response = table.delete_item(
            Key={
                "id": todo_id
            },
            ReturnValues="ALL_OLD"
        )

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "Deleted",
                    "deleted": response.get("Attributes")
                }
            )
        }


    return {
        "statusCode":400,
        "body":json.dumps(
            {
                "message":"Unsupported method"
            }
        )
    }