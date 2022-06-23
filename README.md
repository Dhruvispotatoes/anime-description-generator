# Anime Description Generator

## How to Use
You can try our model in your browser at ____(are we gonna get a link?). Enter a prompt, define the number of descriptions you'd like to generate, their temperature, and generate!

## Technical Stack
1. CoCalc for collaboration and programming
2. GitHub for version control
3. aitextgen: GPT-2
4. Kaggle dataset: anime titles and descriptions
5. pandas
6. Jupyter notebooks for prototyping
7. Flask: web server (HTML, CSS, and JS)


## Dataset:
We used a dataset from Kaggle which contained over 14,000 different titles, descriptions, and other information scraped from anime-planet. However, we had to narrow the dataset down because only around 8,000 of the rows actually had an entry for the description. In the end, we trained the AI on just the descriptions.


## Model:
In order to generate text, we used the GPT-2 model. GPT-2 is the most accessible open-source text generation model, and its generated text when trained well is indistinguishable from humans.

## Libraries
We used pandas and numpy while prepping our data, and we used aitextgen and scikit-learn while generating and training our model.

## Created by the Space Invaders: 
Allison Xia, Daniel Huang, Dhruv Shastry, George Parlos, Mei Satler, and Ryland Robinson. Instructed by Raj Doshi.
