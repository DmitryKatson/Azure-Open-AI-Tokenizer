# Azure Function Text Tokenizer

## Repository Description

This repository contains an Azure Function app written in Python, designed to tokenize text inputs. It's primarily focused on AI and NLP (Natural Language Processing) applications, where text tokenization plays a crucial role. The app provides two main functionalities: counting the number of tokens in a given text and retrieving the individual tokens themselves.

## Endpoints

The app exposes two HTTP-triggered endpoints:

1. **`/api/tokensCount`**: Returns the count of tokens in the provided text.
2. **`/api/tokens`**: Returns the actual tokens extracted from the provided text.

Both endpoints expect a JSON payload with a key `"text"` containing the string to be tokenized.

## Usage with cURL

### 1. Getting Token Count

- **Request**:
  
  ```bash
  curl -X GET http://localhost:7071/api/tokensCount \
  -H "Content-Type: application/json" \
  -d '{"text":"Helllllo AL developers! Welcome to the AI world!!!"}'
  ```

- **Response**:

  ```json
  {"tokensCount": 12}
  ```

### 2. Getting Tokens

- **Request**:

  ```bash
  curl -X GET http://localhost:7071/api/tokens \
  -H "Content-Type: application/json" \
  -d '{"text":"Helllllo AL developers! Welcome to the AI world!!!"}'
  ```

- **Response**:

  ```json
  {"tokens": ["Hell", "ll", "lo", " AL", " developers", "!", " Welcome", " to", " the", " AI", " world", "!!!"]}
  ```

### Global Endpoints

The global endpoint for this Azure Function app is available at:

```
https://azure-openai-tokenizer.azurewebsites.net
```

You can access the functionalities of this app by appending the specific endpoint routes to this base URL. For example:

- For getting the token count, use:
  ```
  https://azure-openai-tokenizer.azurewebsites.net/api/tokensCount
  ```

- For retrieving the tokens, use:
  ```
  https://azure-openai-tokenizer.azurewebsites.net/api/tokens
  ```

These endpoints are configured to handle requests in the same format as the local testing examples provided earlier.

## Setup and Local Testing

To set up and test this Azure Function app locally:

1. Ensure you have Python, Azure Functions Core Tools, and the required libraries installed.
2. Clone the repository to your local machine.
3. Navigate to the repository directory and start the function app using `func start`.
4. Use cURL or any other HTTP client to test the endpoints as shown above.

Note: Make sure to modify the request URLs accordingly if you deploy the app to Azure or any other host.