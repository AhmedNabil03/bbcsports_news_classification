<h1>BBCSport Text Classification Project</h1>

<p>This project focuses on classifying sports news articles from the BBCSport dataset using Natural Language Processing (NLP) techniques. The dataset includes raw text files across five sports categories: football, rugby, cricket, athletics, and tennis.</p>

<h2>About the Dataset</h2>

<p>The BBCSport dataset contains news from five different sports:</p>
<ul>
    <li>Football</li>
    <li>Rugby</li>
    <li>Cricket</li>
    <li>Athletics</li>
    <li>Tennis</li>
</ul>

<p>You can check out the dataset <a href="http://mlg.ucd.ie/datasets/bbc.html">here</a>.</p>

<h2>Steps Taken</h2>

<h3>Data Preprocessing</h3>

<ul>
    <li><b>Converting text to lowercase:</b> Ensuring uniformity in text data.</li>
    <li><b>Removing stopwords and single-character words:</b> Cleaning unnecessary words to improve model performance.</li>
    <li><b>Removing numbers and extra spaces:</b> Further text cleaning.</li>
    <li><b>Applying stemming:</b> Reducing words to their root form.</li>
    <li><b>Transforming text data using TF-IDF vectorization:</b> Converting text data to numerical format suitable for machine learning models.</li>
</ul>

<h3>Model Building</h3>

<p>Implemented and evaluated a Multinomial Naive Bayes model for text classification. The model was trained on the preprocessed text data.</p>

<h2>Results</h2>

<p>The model achieved perfect results with:</p>
<ul>
    <li><b>Accuracy:</b> 1.0</li>
    <li><b>F1 Score:</b> 1.0</li>
</ul>
