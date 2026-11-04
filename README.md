# Restaurant-chatbot

Architecture overview:
![step1_chatbot drawio](https://user-images.githubusercontent.com/20969232/142749382-d4d5732d-4bd8-4997-a72d-f0511b392d46.png)

![restrobot_arch2 drawio](https://user-images.githubusercontent.com/20969232/142749378-ba6de4c5-2cad-4789-ab7a-0f549a7e4406.png)

Detailed explanation of the project is given in my tech blog here: https://medium.com/@barua.aindriya/building-a-nlp-chatbot-for-a-restaurant-with-flask-b978337049f2

How to set up and run the project?

1. Install Pre-requisites
To install all the required libraries, download/clone the repo and in the folder, create/activate your virtual environment and run:  
> pip install -r requirements.txt  
> python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

2. Download pre-trained FastText English model
Download cc.en.300.bin.gz from https://fasttext.cc/docs/en/crawl-vectors.html . Unzip it to cc.en.300.bin (helper script available in helper_scripts/).
3. Prepare dataset
Run data_embedder.py This will take the dataset.json file and convert all the sentences to FastText Vectors.
> python data_embedder.py
4. Set up MongoDB
Ensure MongoDB is running locally (or set MONGO_URI in your .env).
To automatically populate the `menu` collection with sample dishes:
> python helper_scripts/seed_menu.py

The database uses 3 collections:
- `menu`: includes item, cost, vegan, veg, about, offer.
- `bookings`: writes booking ID and timestamp when customer reserves a table.
- `feedback`: stores customer feedback for restaurant management.

5. Run Flask
This will launch the web app on localhost
> export FLASK_APP=app  
> flask run --debug  

