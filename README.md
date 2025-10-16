# Dynamic Profile API (Stage 0 - Backend Wizards)

## Description >> README.md
A simple FastAPI app that returns my profile info and a random cat fact from the Cat Facts API. >> README.md

## Endpoint 
 **GET** `/me` >> README.md

 ## Example Response >> README.md
 ```json >> README.md
 { 
  "status": "success", 
  "user": { 
    "email": "frank@example.com", 
    "name": "Frank Zafka", 
    "stack": "Python/FastAPI"
 },
  "timestamp": "2025-10-16T06:45:10.444Z", 
  "fact": "Cats purr at around 26 cycles per second." 
}


