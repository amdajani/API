# Credit Card Validation REST-ful API

## Description
This API allows users to validate credit card numbers and determine their type.

## Endpoints

### Validate Credit Card

- **URL**: `/credit-cards`
- **Method**: `POST`
- **Request Body**:
  - `credit_card`: The credit card number to validate (integer)

- **Response**:
  - `status`: `success` or `error`
  - `message`: Information about the validation result
  - `type`: The type of the credit card if valid (e.g., `VISA`, `MASTERCARD`, `AMEX`)

### Example Request
```bash
curl -X POST http://localhost:8000/credit-cards -H "Content-Type: application/json" -d '{"credit_card": "4111111111111111"}'
