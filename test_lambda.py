import json
from unittest.mock import patch, MagicMock
import lambda_function

def test_lambda_returns_200():
    mock_table = MagicMock()
    mock_table.update_item.return_value = {
        'Attributes': {'count': 5}
    }
    
    with patch('lambda_function.boto3') as mock_boto3:
        mock_boto3.resource.return_value.Table.return_value = mock_table
        result = lambda_function.lambda_handler({}, {})
    
    assert result['statusCode'] == 200

def test_lambda_returns_count():
    mock_table = MagicMock()
    mock_table.update_item.return_value = {
        'Attributes': {'count': 5}
    }
    
    with patch('lambda_function.boto3') as mock_boto3:
        mock_boto3.resource.return_value.Table.return_value = mock_table
        result = lambda_function.lambda_handler({}, {})
    
    body = json.loads(result['body'])
    assert 'count' in body
    assert body['count'] == 5