# nlp_texts_analysis
Analyze the text chats between people to uncover important insights about their relationship. What words do they use most often, what's the general sentiment, do they talk more casually or formal, etc.?

# Requirements
1. You need [`spacy`](https://spacy.io/usage) module installed 
2. You need a [language](https://spacy.io/usage/models#languages) for the model. In this code I used [`ro_core_news_sm`](https://spacy.io/models/ro#ro_core_news_sm) as I applied it on Romanian text.
3. Export your text messages as `.txt`. For WhatsApp you can follow [this](https://faq.whatsapp.com/android/chats/how-to-save-your-chat-history/?lang=en) guide. Make sure you do it from mobile and uncheck media export.

To install the `ro_core_news_sm` run `python -m spacy download ro_core_news_sm`

# Deployment using App Engine
1. You need to package the modules using commad: `pip install -l lib -r requirements.txt`
2. Deploy using `gcloud app deploy`
