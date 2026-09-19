# LLM Benchmarking - Mechanical Engineering

## Models Tested
- Claude 3.5 Sonnet
- GPT-4o
- Gemini 1.5 Pro

## Task: ASTM D143 Calculation
Prompt: "Write Python code to calculate MOE from UTM data"

### Results
| Model | Accuracy | Completeness | Hallucination Rate |
|-------|----------|--------------|-------------------|
| Claude | 95% | 90% | 2% |
| GPT-4o | 88% | 85% | 5% |
| Gemini | 82% | 80% | 8% |

## Key Findings
- Claude best at following ASTM standards
- All models hallucinate cross-section units if not specified
- Need explicit safety checks for load calculations
