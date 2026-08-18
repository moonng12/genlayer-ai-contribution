from genlayer import *

@gl.contract
class SentimentContract:
    def __init__(self):
        pass

    @gl.public.view
    def analyze(self, text: str) -> str:
        prompt = f"Analyze sentiment of: '{text}'. Return 'Positive' or 'Negative'."
        return gl.exec_prompt(prompt).strip()
