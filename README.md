# Interactive SWOT Analyzer API

An **LLM-powered SWOT Analyzer** built with **FastAPI**, designed primarily to demonstrate **Docker deployment** and **GitHub Actions CI/CD**.

The API generates structured **Strengths, Weaknesses, Opportunities, and Threats (SWOT)** from a project description using OpenRouter/OpenAI.

---

## Highlights

- **Dockerized** for easy deployment and portability.
- **GitHub Actions CI/CD** workflow included for automatic testing and Docker image builds.
- FastAPI backend for **interactive API**.
- LLM integration for **automated SWOT generation**.

---

## Features

- Generate **SWOT analysis** automatically from a project description.
- **Interactive chatbot-style API** for iterative refinement.
- Returns structured **JSON** output.
- Fully **Dockerized** for easy deployment.
- Ready for **GitHub Actions CI/CD**.

---

## Demo JSON Response

```json
{
  "description": "We are building a mobile app to help people find local farmers' markets.",
  "swot": {
    "strengths": [
      "Helps people access fresh produce easily",
      "Supports local farmers"
    ],
    "weaknesses": [
      "Dependent on user adoption",
      "Limited to regions with farmers markets"
    ],
    "opportunities": [
      "Potential partnerships with local farms",
      "Expand to online grocery delivery"
    ],
    "threats": [
      "Competition from large grocery apps",
      "Seasonal variations in produce availability"
    ]
  }
}
```

## Getting Started

### 1. Run using Docker

```bash
# Build Docker image
docker build -t swot-analyzer .

# Run container with API key
docker run --rm -e OPENROUTER_API_KEY="your_key" -p 8000:8000 swot-analyzer
```

### 2. Test the API using Swagger UI

Open the following URL in your browser:
http://localhost:8000/docs

This will open Swagger UI, where you can:

- See all available endpoints.
- Test the `/swot` endpoint interactively.
- Send a POST request with a JSON body, for example:

```json
{
  "description": "We are building a mobile app to help people find local farmers' markets."
}
```

The API will return a structured SWOT JSON response.
