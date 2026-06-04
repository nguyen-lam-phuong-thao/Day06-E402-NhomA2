# AI Cafe Vibe Recommender

## 1. Project Overview

AI Cafe Vibe Recommender is a mini hackathon prototype for local cafe discovery.

Users usually know what kind of cafe they like when they see an image, but they often find it hard to describe that vibe with keywords. This prototype allows users to select one or two vibe images, then recommends cafes whose Google Maps images are visually and semantically similar.

The system works like a visual RAG recommender.

Cafe images are collected from Google Maps. An AI Vision model is used to describe each cafe image. These descriptions are converted into embeddings and stored in the database. When a user selects a vibe image, the system describes that image, converts it into an embedding, and retrieves the most similar cafes based on similarity score.

## 2. Problem Statement

Users aged 18-30, especially students and office workers, often struggle when choosing a cafe because they know the type of space they like visually, but they do not always know how to describe it in text.

Current cafe discovery flow is fragmented.

Users may look at photos on Instagram or TikTok first, then open Google Maps to check rating, address, and reviews. This creates a slow and tiring decision-making process.

The pain point is not the lack of cafe options. The real pain point is that users find it difficult to express their visual preference and verify suitable cafes quickly.

## 3. Proposed Solution

The prototype provides a short visual-first recommendation flow.

The user selects one or two vibe images that match their current preference. The system then uses AI to understand the visual style of the selected image and retrieves similar cafes from the prepared cafe database.

Each recommendation result includes the cafe name, main image, rating, address, category, similarity score, and a short reason explaining why the cafe matches the selected image.

## 4. Core User Flow

```text
User opens the app
        ↓
System shows 3 vibe images
        ↓
User selects 1 or 2 images
        ↓
System sends selected image data to backend
        ↓
AI describes the selected image
        ↓
System converts the description into an embedding
        ↓
System compares it with cafe embeddings in the database
        ↓
System ranks cafes by similarity score
        ↓
System returns the top 3 most similar cafes
        ↓
User views cafe details and opens Google Maps if interested
```

## 5. AI Role

The project follows an augmentation approach.

AI does not make the final decision for the user. Instead, AI helps convert visual preference into searchable semantic information.

AI is used in three main places.

### 5.1 Cafe Image Understanding

Cafe images from Google Maps are processed by an AI Vision model.

The model generates a short description of the cafe image, including the atmosphere, interior style, lighting, space, and category.

Example output:

```json
{
  "cafe_name": "The Hidden Garden Cafe",
  "category": "Garden cafe",
  "ai_description": "A cozy garden cafe with many green plants, warm lighting, wooden furniture, and a quiet relaxing atmosphere."
}
```

### 5.2 User Image Understanding

When the user selects a vibe image, the same AI Vision process is used to describe the selected image.

Example output:

```json
{
  "preference_description": "The user seems to prefer a warm and cozy cafe with natural lighting, wooden furniture, green plants, and a peaceful atmosphere."
}
```

### 5.3 Recommendation Explanation

After the system retrieves similar cafes, AI or a simple template can generate a short match reason.

Example:

```text
This cafe matches your selected vibe because it has warm lighting, green plants, and a quiet cozy atmosphere similar to the image you chose.
```

## 6. Recommendation Logic

The recommendation logic is based on semantic similarity.

The system does not use manually assigned vibe scores such as cozy, minimal, or quiet. Instead, it compares the embedding of the user-selected image description with the embeddings of cafe image descriptions.

The main ranking metric is similarity score.

```text
similarity_score = cosine_similarity(user_image_embedding, cafe_image_embedding)
```

Cafes with higher similarity scores are ranked higher.

The output is the top 3 cafes with the highest similarity scores.

## 7. Data Requirements

The prototype uses a small prepared dataset of around 30 cafes.

Each cafe record contains:

```json
{
  "id": "cafe_001",
  "name": "The Hidden Garden Cafe",
  "address": "District 1, Ho Chi Minh City",
  "rating": 4.6,
  "category": "Garden cafe",
  "image_url": "https://example.com/cafe-image.jpg",
  "google_maps_url": "https://maps.google.com/...",
  "ai_description": "A cozy garden cafe with many green plants, warm lighting, wooden furniture, and a quiet relaxing atmosphere.",
  "embedding": [0.012, -0.083, 0.092]
}
```

For the hackathon prototype, the dataset can be stored in a JSON or CSV file.

A full production database is not required at this stage.

## 8. System Architecture

```text
Google Maps Cafe Images
        ↓
AI Vision Captioning
        ↓
Cafe Descriptions
        ↓
Text Embedding
        ↓
Cafe Database
        ↓

User Selects Vibe Image
        ↓
AI Vision Captioning
        ↓
User Preference Description
        ↓
Text Embedding
        ↓
Similarity Search
        ↓
Top 3 Cafe Recommendations
```

## 9. API Design

### 9.1 Get Vibe Images

```http
GET /api/vibes
```

Returns the 3 vibe images shown to the user.

Example response:

```json
{
  "vibes": [
    {
      "id": "vibe_01",
      "image_url": "/images/vibe_01.jpg",
      "label": "Cozy Green Cafe"
    },
    {
      "id": "vibe_02",
      "image_url": "/images/vibe_02.jpg",
      "label": "Minimal Study Cafe"
    },
    {
      "id": "vibe_03",
      "image_url": "/images/vibe_03.jpg",
      "label": "Vintage Warm Cafe"
    }
  ]
}
```

### 9.2 Recommend Cafes

```http
POST /api/recommend
```

Request body:

```json
{
  "selected_vibe_ids": ["vibe_01", "vibe_03"]
}
```

Response:

```json
{
  "query_description": "The user prefers a cozy cafe with warm lighting, green plants, natural materials, and a relaxing atmosphere.",
  "results": [
    {
      "id": "cafe_001",
      "name": "The Hidden Garden Cafe",
      "image_url": "https://example.com/cafe-image.jpg",
      "rating": 4.6,
      "address": "District 1, Ho Chi Minh City",
      "category": "Garden cafe",
      "similarity_score": 0.89,
      "reason": "This cafe matches your selected vibe because it has green plants, warm lighting, and a cozy relaxing atmosphere.",
      "google_maps_url": "https://maps.google.com/..."
    }
  ]
}
```

### 9.3 Feedback

```http
POST /api/feedback
```

Request body:

```json
{
  "cafe_id": "cafe_001",
  "feedback": "not_my_vibe"
}
```

For the MVP, feedback is handled simply.

If the user clicks `Not my vibe`, the system hides that cafe and returns the next most similar cafe from the ranking list.

## 10. Frontend Screens

### Screen 1: Vibe Selection

The user sees 3 cafe vibe images.

The user can select 1 or 2 images.

Main button:

```text
Find my cafe vibe
```

### Screen 2: Loading

The system shows a short loading state.

Example:

```text
Analyzing your vibe...
```

### Screen 3: Recommendation Results

The system displays the top 3 most similar cafes.

Each cafe card includes:

```text
Cafe name
Main image
Rating
Address
Category
Similarity score
Match reason
Open in Google Maps button
Not my vibe button
```

## 11. Tech Stack

Recommended stack for the hackathon prototype:

```text
Frontend: Next.js
Backend: Next.js API Routes or FastAPI
Data storage: JSON or CSV
AI Vision: GPT-4o, Gemini Vision, or Claude Vision
Embedding: OpenAI Embedding or Sentence Transformers
Similarity Search: Cosine Similarity
Deployment: Vercel, Render, or Railway
```

For the fastest prototype, the project can be built as a single Next.js app with local JSON data.

## 12. MVP Scope

The MVP includes:

```text
3 predefined vibe images
User can select 1 or 2 vibe images
Around 30 cafes in the dataset
AI-generated description for each cafe image
Embedding for each cafe description
Similarity-based recommendation
Top 3 cafe results
Cafe name, image, rating, address, category, similarity score, and match reason
Open in Google Maps button
Not my vibe button
```

The MVP does not include:

```text
Realtime Google Maps crawling
User-uploaded images
GPS-based distance calculation
Complex ranking with rating or distance weight
Manual vibe score
Chatbot conversation
Production-ready database
```

## 13. Handling Multiple Selected Images

If the user selects two images, the system combines the two selected image descriptions into one preference description.

Example:

```text
Image 1 description: A bright minimal cafe with clean interior and quiet study-friendly atmosphere.

Image 2 description: A cozy green cafe with plants, warm lighting, and relaxing atmosphere.

Combined query description: The user prefers a cafe that feels bright, clean, cozy, green, relaxing, and suitable for studying.
```

The combined description is then converted into one embedding and used for similarity search.

## 14. Failure Handling

### Case 1: Result does not match user taste

The user can click:

```text
Not my vibe
```

The system hides that cafe and returns the next highest similarity result.

### Case 2: Not enough strong matches

If similarity scores are too low, the system can show a message:

```text
We could not find a very close match, but here are the nearest options from our current dataset.
```

### Case 3: Dataset is too small

The system clearly communicates that this is a prototype using a limited dataset.

## 15. Evaluation Metrics

The prototype can be evaluated with the following metrics:

```text
Top-3 relevance
Recommendation acceptance rate
Not my vibe rate
Average similarity score
Time to recommendation
User satisfaction score
```

## 16. Team Roles

```text
Huy: Research, evidence, demo script, repo
Thảo: SPEC, product flow, AI logic
Kiên: Frontend prototype
Hà: Dataset, testing, failure path
Kiên, Hà, Thảo: Prototype implementation
```

