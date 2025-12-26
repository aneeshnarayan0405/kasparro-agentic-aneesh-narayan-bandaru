# Multi-Agent Content Generation System – Project Documentation

## 1. Problem Statement

Design and implement a modular agentic automation system that transforms structured product data into multiple machine-readable content pages (FAQ Page, Product Page, and Comparison Page) using reusable logic blocks and clearly defined agent boundaries.

### Key Requirements
- Parse structured product data into clean internal models  
- Generate 15+ categorized user questions  
- Define and apply multiple content templates  
- Build reusable content logic blocks  
- Assemble pages autonomously via agents  
- Output clean, machine-readable JSON  
- Ensure the entire pipeline runs through agent orchestration  

---

## 2. Solution Overview

The system is built as a **multi-agent pipeline** where each agent performs a single, well-defined responsibility.  
Agents are orchestrated through a central orchestrator that controls execution order and data flow.

### High-Level Flow
```

Input Data → Validation → Parsing → Question Generation →
Content Agents (FAQ / Product / Comparison) → Templates → JSON Output

```

### Core Components
- **Agents**: Modular units with single responsibility
- **Logic Blocks**: Reusable content transformation functions
- **Templates**: Define structured output formats
- **Orchestrator**: Coordinates agent execution
- **Utilities**: Logging, validation, metrics, and file handling

---

## 3. Scope & Assumptions

### In Scope
- Use only the provided product data
- Generate FAQ, Product Page, and Comparison Page
- Comparison with a fictional but structured Product B
- JSON-only outputs
- Modular and extensible architecture

### Out of Scope
- External APIs or LLM calls
- UI or website generation
- Persistent storage or authentication
- External data enrichment

### Assumptions
- Input follows a predefined schema
- System runs in a controlled environment
- No real-time updates required

---

## 4. System Design (Most Important)

### 4.1 Architecture Overview

```

┌──────── Input Layer ────────┐
│ Product JSON               │
└───────────┬────────────────┘
↓
┌──── Validation Agent ──────┐
└───────────┬────────────────┘
↓
┌──── Data Parser Agent ─────┐
└───────────┬────────────────┘
↓
┌─ Question Generation Agent ┐
└───────────┬────────────────┘
↓
┌── Content Agents (Parallel) ┐
│ FAQ | Product | Comparison │
└───────────┬────────────────┘
↓
┌──── Template Rendering ────┐
└───────────┬────────────────┘
↓
┌──────── JSON Outputs ──────┐
│ faq.json                  │
│ product_page.json         │
│ comparison_page.json      │
└───────────────────────────┘

```

The orchestrator manages this flow as a **Directed Acyclic Graph (DAG)**.

---

### 4.2 Agent Responsibilities

| Agent | Responsibility | Input | Output |
|------|---------------|-------|--------|
| DataParserAgent | Parse raw input into models | Raw JSON | Product model |
| ValidationAgent | Validate schema & constraints | Raw JSON | Validation result |
| QuestionGenerationAgent | Generate categorized questions | Product | 15+ questions |
| FAQAgent | Build FAQ content | Questions + Product | FAQ JSON |
| ProductPageAgent | Build product page | Product | Product JSON |
| ComparisonAgent | Compare Product A & B | Products | Comparison JSON |

---

### 4.3 Logic Blocks

Logic blocks are **pure, reusable functions** used across agents.

Key blocks include:
- **Benefits Block** – Structures benefit descriptions
- **Usage Block** – Formats usage steps and metadata
- **Safety Block** – Adds warnings and precautions
- **Price Block** – Handles pricing and value analysis
- **Comparison Block** – Computes structured differences
- **SEO Block** – Generates metadata

Each block has clear input/output contracts and no hidden state.

---

### 4.4 Template Engine

Templates define **how content is structured**, not how it is generated.

Templates implemented:
- FAQ Template
- Product Page Template
- Comparison Template

Templates ensure consistent formatting, metadata injection, and clean JSON output.

---

### 4.5 Orchestration Strategy

- **Pattern**: Phase-based DAG execution
- **Parallelism**: Content agents can run independently
- **Error Handling**: Graceful failure with logging
- **Metrics**: Execution time and success tracking

Execution Phases:
1. Validation & Parsing  
2. Question Generation  
3. Content Generation (Parallel)  
4. Template Rendering  

---

## 5. Technical Implementation

### Key Design Decisions
- No external dependencies
- Typed internal models for clarity
- Base classes for agents and blocks
- YAML-based configuration
- Structured logging
- Unit and integration tests

### Code Organization
```

src/
├── core/
├── agents/
├── logic_blocks/
├── templates/
└── utils/

````

---

## 6. Evaluation Criteria Alignment

- **Agentic System Design**: Clear boundaries and orchestration  
- **Agent Quality**: Meaningful roles and correct interfaces  
- **Content Engineering**: Reusable blocks and templates  
- **Data Structure**: Clean, machine-readable JSON  

---

## 7. Extensibility

The system is designed to easily support:
- New content types
- Additional logic blocks
- New agents
- Multiple output formats
- Distributed execution

---

## 8. Running the System

```bash
python main.py
````

With configuration:

```bash
python main.py --config config/settings.yaml
```

Run tests:

```bash
pytest tests/ -v
```

---

## 9. Conclusion

This project demonstrates a **production-ready, agentic system** with:

* Clear separation of concerns
* Strong system design and orchestration
* Modular, reusable components
* Clean and structured outputs

The implementation reflects real-world applied AI engineering practices and aligns directly with Kasparro’s evaluation criteria.