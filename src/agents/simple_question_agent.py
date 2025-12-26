class SimpleQuestionAgent:
    def run(self, product):
        questions = {
            "informational": [
                f"What is {product.name}?",
                "What does Vitamin C do for skin?",
                "Who is this serum suitable for?",
                "What skin types benefit most?",
                "How long does one bottle last?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is it safe for sensitive skin?",
                "Can I use it with other actives?",
                "What if I experience irritation?"
            ],
            "usage": [
                "How should I apply this serum?",
                "Can I use it both day and night?",
                "How many drops should I use?",
                "Should I follow with moisturizer?"
            ],
            "purchase": [
                "Is it worth the price?",
                "Where can I buy it?",
                "Is there a return policy?",
                "How does it compare to cheaper alternatives?"
            ],
            "comparison": [
                "How does it compare to other Vitamin C serums?",
                "What makes it different from drugstore options?",
                "Is it better than DIY Vitamin C solutions?"
            ]
        }
        print(f"DEBUG: Generated {sum(len(q) for q in questions.values())} questions")
        return questions