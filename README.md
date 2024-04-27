# BarTag Generator

## Technologies used
- python
- flask
- pytest

## HTTP

### POST `/create_tag`

Create a new poll.

#### Request body

```json
{
  "product_code": "123456",
}
```

#### Response body

```json
{
  "path": "./123456.png"
}
```
