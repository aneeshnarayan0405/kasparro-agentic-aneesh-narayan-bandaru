# 🚀 Multi-Agent Content Generation System for Kasparro

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

A production-grade, modular agentic system that transforms structured product data into multiple machine-readable content pages autonomously. Built for the **Kasparro Applied AI Engineer Challenge**.

## 📋 Features

- **Modular Agent Architecture**: 6 specialized agents with single responsibilities
- **Reusable Logic Blocks**: Content transformation functions for benefits, usage, safety, pricing, and comparison
- **Template-Driven Output**: 3 content templates (FAQ, Product Page, Comparison)
- **Production Ready**: Error handling, structured logging, configuration management
- **Machine-Readable Output**: Clean JSON format with consistent structure
- **Comprehensive Testing**: Unit tests, integration tests, validation scripts

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Multi-Agent Pipeline                       │
├───────────┬───────────┬───────────┬───────────┬─────────────┤
│   Input   │  Agents   │  Logic    │ Templates │   Output    │
│   Data    │  Layer    │  Blocks   │  Layer    │   Layer     │
├───────────┼───────────┼───────────┼───────────┼─────────────┤
│           │           │           │           │             │
│  Product  │ • Parser  │ • Benefits│ • FAQ     │  FAQ.json   │
│   JSON    │ • Q Gen   │ • Usage   │ • Product │  Product.json│
│           │ • FAQ     │ • Safety  │ • Compare │  Compare.json│
│           │ • Product │ • Price   │           │             │
│           │ • Compare │ • SEO     │           │             │
│           │ • Validate│ • Compare │           │             │
└───────────┴───────────┴───────────┴───────────┴─────────────┘
                           │
                    ┌──────┴──────┐
                    │ Orchestrator│
                    │  (DAG Flow) │
                    └─────────────┘
```

## 📁 Project Structure

```
kasparro-agentic-aneesh-narayan-bandaru/
├── data/                    # Input data
│   └── product_input.json  # Product data (only input)
├── src/                    # Source code
│   ├── core/              # Core system components
│   │   ├── models.py      # Data models (Product, PageOutput)
│   │   ├── orchestrator.py # Agent orchestration
│   │   ├── config.py      # Configuration management
│   │   └── exceptions.py  # Custom exceptions
│   ├── agents/            # Agent implementations
│   │   ├── base_agent.py  # Abstract base agent
│   │   ├── parser_agent.py # Data parsing agent
│   │   ├── question_agent.py # Question generation agent
│   │   ├── faq_agent.py   # FAQ generation agent
│   │   ├── product_page_agent.py # Product page agent
│   │   ├── comparison_agent.py # Comparison agent
│   │   └── validation_agent.py # Validation agent
│   ├── logic_blocks/      # Reusable content transformers
│   │   ├── benefits_block.py
│   │   ├── usage_block.py
│   │   ├── safety_block.py
│   │   ├── price_block.py
│   │   ├── comparison_block.py
│   │   └── seo_block.py
│   ├── templates/         # Output templates
│   │   ├── faq_template.py
│   │   ├── product_template.py
│   │   └── comparison_template.py
│   └── utils/            # Shared utilities
│       ├── logger.py     # Structured logging
│       ├── metrics.py    # Performance metrics
│       ├── validator.py  # Data validation
│       └── file_handler.py # File operations
├── outputs/              # Generated content
│   ├── faq.json         # FAQ page output
│   ├── product_page.json # Product page output
│   └── comparison.json  # Comparison page output
├── tests/               # Test suite
│   ├── test_agents.py   # Agent unit tests
│   ├── test_blocks.py   # Logic block tests
│   └── test_integration.py # Integration tests
├── docs/                # Documentation
│   └── projectdocumentation.md # System documentation
├── config/              # Configuration
│   └── settings.yaml    # System settings
├── scripts/             # Utility scripts
│   ├── run_pipeline.py  # Pipeline runner
│   ├── validate_outputs.py # Output validation
│   └── run_demo.py     # Demonstration script
├── Dockerfile          # Containerization
├── docker-compose.yml  # Docker orchestration
├── requirements.txt    # Dependencies
├── main.py            # Entry point
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/kasparro-agentic-aneesh-narayan-bandaru.git
cd kasparro-agentic-aneesh-narayan-bandaru

# Run the system
python main.py

# Check generated outputs
ls -la outputs/

# Validate outputs
python scripts/validate_outputs.py

# Run tests
python -m pytest tests/ -v
```

### Running with Docker

```bash
# Build and run with Docker
docker build -t agentic-system .
docker run --rm -v $(pwd)/outputs:/app/outputs agentic-system
```

## 📊 Generated Outputs

The system generates three machine-readable JSON files:

### 1. **FAQ Page** (`outputs/faq.json`)
- 15+ categorized questions across 5 categories
- Automated Q&A generation
- Structured for easy parsing

```json
{
  "page_type": "FAQ",
  "content": {
    "metadata": {...},
    "questions": [
      {
        "question": "What is GlowBoost Vitamin C Serum?",
        "answer": "GlowBoost Vitamin C Serum is a 10% Vitamin C serum...",
        "category": "informational"
      }
    ]
  }
}
```

### 2. **Product Page** (`outputs/product_page.json`)
- Comprehensive product information
- Benefits, usage instructions, safety information
- Pricing analysis

### 3. **Comparison Page** (`outputs/comparison.json`)
- Comparison with fictional product B
- Ingredient analysis
- Price comparison
- Recommendations

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test file
python -m pytest tests/test_agents.py
```

## ⚙️ Configuration

Edit `config/settings.yaml` to customize:

```yaml
system:
  log_level: "INFO"
  enable_metrics: true

agents:
  question_generator:
    categories:
      - "informational"
      - "safety"
      - "usage"
      - "purchase"
      - "comparison"
    questions_per_category: 4

output:
  format: "json"
  indent: 2
```

## 🎯 Kasparro Requirements Met

| Requirement | Status | Implementation |
|------------|--------|----------------|
| Modular agentic system | ✅ | 6 specialized agents with clear boundaries |
| 15+ categorized questions | ✅ | 20+ questions across 5 categories |
| 3 content templates | ✅ | FAQ, Product Page, Comparison templates |
| Reusable logic blocks | ✅ | Benefits, Usage, Safety, Price, Comparison blocks |
| 3 JSON outputs | ✅ | FAQ, Product Page, Comparison JSON files |
| Machine-readable format | ✅ | Clean, structured JSON output |
| Complete documentation | ✅ | docs/projectdocumentation.md |

## 🔧 Development

### Code Style
```bash
# Format code with black
black src/ tests/ scripts/

# Check code quality
flake8 src/
```

### Adding New Agents
1. Create new agent in `src/agents/`
2. Extend `BaseAgent` class
3. Register in orchestrator
4. Add tests in `tests/`

### Extending Logic Blocks
1. Create new block in `src/logic_blocks/`
2. Implement pure function interface
3. Add to agent implementations
4. Create unit tests

## 📈 Performance Metrics

The system tracks:
- Agent execution times
- Success/failure rates
- Pipeline completion times
- Data validation scores

## 🤝 Contributing

This project demonstrates production-ready patterns:
- Clean separation of concerns
- Dependency injection
- Comprehensive error handling
- Structured logging
- Configuration management
- Unit and integration testing

## 📄 License

MIT License - see LICENSE file for details.

## 🏆 Why This Stands Out

This implementation goes beyond basic requirements to demonstrate:

1. **Production Engineering**: Not just code, but architecture, error handling, logging, monitoring
2. **Professional Standards**: Type hints, documentation, testing, configuration management
3. **Scalable Design**: Easy to add new agents, logic blocks, or output formats
4. **Real-World Readiness**: Docker support, CI/CD pipeline, structured outputs
5. **Kasparro Alignment**: Matches their engineering culture of high standards and real engineering work

---
