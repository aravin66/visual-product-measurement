# AI-Powered Visual Product Measurement System

## Overview
This project implements an **AI-powered visual intelligence system** that analyzes product images and produces **objective, structured visual measurements** based purely on what is visible in the images.

The system avoids merchandising logic, recommendations, or user-specific interpretation.  
All outputs are derived **strictly from visual appearance**.

This prototype is designed to simulate how large-scale product catalogs can be analyzed automatically using vision-enabled AI models.

---

## Problem Statement
Modern product catalogs rely heavily on manual tagging or business-driven categorization, which is time-consuming, inconsistent, and difficult to scale.

The challenge is to design a system that:
- Understands products **visually**
- Extracts **objective, observable characteristics**
- Produces **consistent, machine-readable outputs**
- Works with **one or multiple images per product**

---

## Solution
We designed a **Visual Product Measurement System** that:
- Accepts one or more product image URLs
- Uses a vision-capable AI model to analyze images
- Produces structured visual measurements along defined dimensions
- Returns clean JSON output suitable for downstream systems
- Provides a simple, interactive frontend for testing

The system is robust to ambiguity and enforces strict schema validation to ensure consistency.

---

## Key Features
- ✅ Accepts one or more image URLs per product
- ✅ Supports multiple images for the same product (different views)
- ✅ Vision-based analysis using AI (no metadata used)
- ✅ Continuous visual scoring from −5.0 to +5.0
- ✅ Detection of observable visual attributes
- ✅ Strict JSON schema validation
- ✅ Clean, interactive web UI
- ✅ Machine-consumable API output

---

## Visual Measurement Dimensions
Each dimension is scored between **−5.0 and +5.0**:

- **Gender Expression**: Masculine → Feminine
- **Visual Weight**: Sleek/Light → Bold/Heavy
- **Embellishment**: Simple → Ornate
- **Unconventionality**: Classic → Avant-garde
- **Formality**: Casual → Formal

> All measurements are derived exclusively from visual inspection of images.

---

## Observable Visual Attributes
The system also detects clearly visible attributes when unambiguous:
- Frame or structural geometry
- Transparency or opacity
- Dominant colors
- Visible textures or surface patterns
- Presence of visible wirecore
- Suitability for kids (only if visually clear)

Ambiguous attributes are returned as `null`.

---

## Dataset Usage
The provided dataset contains **multiple images per product**, representing different visual views (front, side, detail, etc.).

The dataset is:
- ❌ Not used for training
- ✅ Used to test multi-image product analysis
- ✅ Used to simulate real-world catalog scenarios

All images belonging to the same `product_id` are analyzed together to generate **one aggregated visual measurement output**.

---

## High-Level Architecture
flowchart TD
    A[User / Frontend UI] --> B[FastAPI Backend]
    
    B --> C[Request Validation]
    C -->|Validate Image URLs| D[Image Validator]

    D --> E[Vision AI Service]
    E -->|Analyze Images| F[Gemini Vision Model]

    F --> G[AI Response Parsing]
    G --> H[Pydantic Schema Validation]

    H --> I[Structured JSON Output]

    I --> A


