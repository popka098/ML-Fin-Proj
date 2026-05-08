from transformers import MarianMTModel, MarianTokenizer

class TranslatorService:
    def __init__(self):
        model_name = "Helsinki-NLP/opus-mt-ru-en"

        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)
    
    def ru_to_en(self, text: str) -> str:
        batch = self.tokenizer(
            [text],
            return_tensors="pt",
            padding=True,
            truncation=True,
        )

        generated = self.model.generate(**batch)

        return self.tokenizer.batch_decode(
            generated,
            skip_special_tokens=True,
        )[0]