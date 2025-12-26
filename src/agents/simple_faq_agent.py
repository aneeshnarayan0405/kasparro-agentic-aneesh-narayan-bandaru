class SimpleFAQAgent:
    def run(self, questions, product):
        # Create simple Q&A pairs
        qa_pairs = [
            {"question": questions["informational"][0], "answer": f"{product.name} is a {product.concentration} serum for {', '.join(product.skin_type)} skin."},
            {"question": questions["safety"][0], "answer": product.side_effects},
            {"question": questions["usage"][0], "answer": product.usage},
            {"question": questions["purchase"][0], "answer": f"At ₹{product.price}, it offers good value for its ingredients."},
            {"question": questions["comparison"][0], "answer": f"{product.name} contains {len(product.ingredients)} key ingredients for comprehensive benefits."}
        ]
        
        faq_output = {
            "page_type": "FAQ",
            "content": {
                "metadata": {"generated_by": "SimpleFAQAgent"},
                "questions": qa_pairs,
                "total_questions": len(qa_pairs)
            }
        }
        print(f"DEBUG: Created FAQ with {len(qa_pairs)} questions")
        return faq_output