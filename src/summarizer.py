from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name = ""):
        self.summarizer = pipeline("summarization", model = model_name)

    def summarize(self, text, min_len=40, max_len=100):
        result = self.summarizer(
            text,
            min_length=min_len,
            max_length=max_len,
            do_sample=False

        )

        # print(result)

        return result[0]['summary_text']