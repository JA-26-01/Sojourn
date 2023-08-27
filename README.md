<h1 align="center">SOJOURN</h1>
<p align="center">
<!--<img width="25%" src="" alt="logo">-->
</p>

## About Sojourn ##

Sojourn is a simple travel recommendation app, which allows the users to not only explore new places in a given area of their choice, but also allows them to
seacrh for famous tourist spots all over India, and see what other tourists say about them. Tourism is one of India's biggest monetary means of development.Sojourn is an attempt to enhance the reach of tourism to all people.

You can try out the demo application at <a href="https://sojourn-fbmkb2ecngwii6afg7uwsc.streamlit.app/" target="_blank">here</a>
<br>

The main algorithm used for recommendation is **Content-Based Filtering**, which is aimed to find the similarity between the two entities. Here, the similarity score is calculated based 
on 3 main indexdes - location, name of the spot and concatenated reviews posted by others tourists. Since the dataset used did not contain the images of the desired places, image scraping using "requests" has been performeed.

The base app, as of now, includes two main features:
> 1. **Find** - Allows the user to find a place of choice and see what is other people's opinion about them.
> 2. **Explore** - Allows the user to see famous spots in the city of their choice, and also similar places in other cities.

<br>

## :sparkles: Languages used:
> 1. Python
> 2. HTML
> 3. CSS

Framework for creating UI and app deployment - Streamlit

You can find the package installation details in the requirements.txt file

## :sparkles: Project Struture:
> 1. app.py - the starter code for the application
> 2. find.py - codes to find a place, based on user's query
> 3. predict.py - codes to recommend spots in the given city of choice, and other similar places
> 4. reviews.py - displaying the required reviews posted by other tourists
> 5. similarity_matrix.npy - contains the similarity matrix containing the scores between different places, created using Count_Vectorizer function
> 6. reviews_db.csv - dataset containing location details and reviews 
> 7. Modified.csv - dataset containing the pre-processed dataset, containing the concatenated categories index for each location

The dataset has been modified in order to make it suitable for deployment. You can find the original dataset at https://www.kaggle.com/datasets/ritvik1909/indian-places-to-visit-reviews-data

