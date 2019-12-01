from django.db import models

# Create your models here.
import numpy as np
import pandas as pd
import nltk
# nltk.download('punkt') # one time execution
import re
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

import tweepy
# !pip install vaderSentiment
from sklearn.base import BaseEstimator, TransformerMixin
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.graph_objects as go
import pandas as pd
from plotly.offline import plot


# import tweepy
# import pandas as pd
# import numpy as np
# !pip install vaderSentiment
# from sklearn.base import BaseEstimator, TransformerMixin
# import re


'''
**Agersens**\
Agersens has developed an integrated hardware and software platform named "eShephard" for continuous **monitoring of livestock** animals.
The hardware consists of **wearable devices** equipped with GPS and sensors for monitoring animal health. The device guides the animal to
move on specified path for activities such as grazing. The company calls the process "**Fenceless Farming**". Data captured is moved into
the cloud and through data analytics, insights are provided to the farmer on the software platform accessible through mobile or computer.
'''

# livestock-monitoring
URL_1 = "https://www.softwebsolutions.com/resources/livestock-monitoring-using-IoT.html"
# wearable-technology
URL_2 = "https://www.businessinsider.com/wearable-technology-healthcare-medical-devices/?r=AU&IR=T"
# Fenceless Farming
URL_3 = "https://nzfarmlife.co.nz/technology-a-fenceless-future/"
# URL = "http://www.values.com/inspirational-quotes"

# nltk.download('stopwords')

# Extract word vectors
word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()
# function to remove stopwords
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

def get_summary_func(raw_string):
    sentences = sent_tokenize(raw_string)
    # sentences
    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]
    # clean_sentences
    stop_words = stopwords.words('english')
    # function to remove stopwords
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new

    # remove stopwords from the sentences
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    sentence_vectors = []
    for i in clean_sentences:
      if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
      else:
        v = np.zeros((100,))
      sentence_vectors.append(v)

    # similarity matrix
    sim_mat = np.zeros([len(sentences), len(sentences)])

    for i in range(len(sentences)):
      for j in range(len(sentences)):
        if i != j:
          sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)

    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

    # Extract top 10 sentences as the summary
    output_sentence = []
    for i in range(3):
      output_sentence.append(ranked_sentences[i][1])
    return " ".join(output_sentence)
#   print(ranked_sentences[i][1])

url_1_str = '''
There’s an increasing global concern for the expansion of agriculture production to produce enough food for the world population. Thus, the importance of livestock management in agriculture holds utmost value for livelihood. But, with the ever-growing concern about land and water resources, farmers struggle to manage their crops and livestock. Apart from this, reducing waste and cutting overall costs remains a priority for farmers.

The new advancements in technology plays a crucial role in helping to improve the quality and quantity of agriculture production. This is when the Internet of Things (IoT) comes into the picture. It brings possibilities for farmers to optimize their livestock health using remote monitoring and data-driven decision making. Here are some interesting use cases of livestock monitoring using IoT.

Monitoring health levels
It is crucial to monitor the health levels of livestock to prevent illness and diagnose diseases earlier. IoT solutions use wearables such as electronic bands with the capability to stream data to the cloud. These wearables are mounted on the animal while the built-in sensors in them help to capture data and notify farmers about several factors that directly have an impact on livestock health.
Monitoring heart rate, respiratory rate, blood pressure, digestion level, and other vitals can help farmers stay up-to-date with their cattle’s health levels. Moreover, tracking these factors also contributes to a significant reduction in livestock feeding issues.

Monitoring reproductive cycle
Observing an animal’s reproductive cycle traditionally is tedious, but with the help of IoT-based monitoring, it can be made easier. For instance, a connected IoT device can help to monitor and measure a cow when it goes into heat, as cows can be in heat for around eight hours. Not just that, but the same device can also notify the farmer when the cow goes into labor thus making the calving process safer. IoT-enabled monitoring completely removes the need of supervising cows manually for the calving process and promotes safer and successful births.

Location tracking
It is common for livestock to separate themselves from the herd, specifically when they are ill or in heat. Often, farmers face a tough time locating these separated livestock. With the help of IoT wearables, this hassle is eliminated, and livestock can be found in no time. IoT devices track the movement pattern of animals, locate them and help to optimize their grazing patterns. Moreover, the sensors integrated into the IoT device can notify the farmer when cattle’s behavior appears to be changing.

Maximizing livestock livelihood
Monitoring behavior of herds is one of the most crucial tasks for farmers. With the use of IoT devices, it is easy to correlate cattle movement with specific behaviors such as pasturing or lying down to chew cud. By monitoring cattle behavior, a farmer can easily identify if the cow needs to be milked at that time. Not just that, IoT devices can also help to measure the milking amount and speed. Similarly, they can also track the amount of food a cow consumed and the number of steps it walked in a day.

The sensors embedded within wearables that can be tied around the cow’s neck, help farmers to personally supervise the session based on the needs. All the data gathered from the cow’s activity allows a farmer to help cows improve their diet and increase lactation. IoT along with rich data-driven insights can help farmers to improve the way they monitor their livestock.

The bottom line
There’s no longer a need for farmers to depend on their gut feeling to make crucial decisions. An IoT solution for livestock that is backed up by real-time data can provide key insights in most aspects of farming livestock. Moreover, such solutions enable farmers to make better decisions that result in reduced waste and maximum efficiency. Farmers can start reaping greater productivity and revenue by integrating a livestock monitoring system. To know more about smart livestock monitoring, get in touch with our experts.
'''


url_2_str = '''
Wearable fitness technology has weaved itself into society so that FitBits and smartwatches are seen as mainstream; and the future of wearable devices shows no sign of slowing down.

wearable tech 4x2
Business Insider Intelligence
Piloted by the increasing demand of consumers to monitor their own health, use of wearable technology has more than tripled in the last four years. According to research from Business Insider Intelligence, more than 80% of consumers are willing to wear fitness technology.

This growing demand for wearables has generated a booming market, and now insurers and companies are seeing how supplying wearable health technology to their consumers and employees is beneficial.

What is wearable healthcare technology?
Wearable technology in healthcare includes electronic devices that consumers can wear, like Fitbits and smartwatches, and are designed to collect the data of users' personal health and exercise. US consumer use of wearables jumped from 9% in 2014 to 33% in 2018, according to Accenture.

Examples of Wearable Devices in Healthcare
The advancement of wearable technology and growing demand from consumers to take control of their own health has influenced the medical industry, including insurers, providers, and technology companies, to develop more wearable devices such as Fitbits, smartwatches, and wearable monitors.

Wearable Fitness Trackers
Some of the simplest and most original forms of wearable technology, wearable fitness trackers, are wristbands equipped with sensors to keep track of the user's physical activity and heart rate. They provide wearers with health and fitness recommendations by syncing to various smartphone apps.

fitbit flex
Photo Credit: Courtesy of Fitbit® Flex™
The FitBit Flex was an early, popular option for wearable technology consumers. Users were attracted to it's sleek look and ability to track their step progress throughout the day with the device's five indicator lights.

Smart Health Watches
Once only used to count steps and tell time, smartwatches have now transformed into clinically viable healthcare tools. Apple launched the Apple Heart Study app in 2017 to monitor users' heart rhythms and alert those who are experiencing atrial fibrillation.

Apple Watch
Drew Angerer/Getty Images
The company also recently released the "Movement Disorder API" to help researchers gather new insights into Parkinson's disease.

Smartwatches allow users to perform tasks they normally do on their phones — read notifications, send simple messages, make phone calls — while also offering some of the exercise- and health-tracking benefits of fitness trackers.

Wearable ECG Monitors
Wearable ECG monitors are on the cutting edge of consumer electronics, and what sets these monitors apart from some smartwatches, is their ability to measure electrocardiograms, or ECGs. Business Insider recently reported on Withings winning best wearable at the 2019 Consumer Electronics Show with their Move ECG product.

The Move ECG is able to measure an electrocardiogram and send the reading to the user's doctor, as well as detect atrial fibrillation. It's also able to track pace, distance, and elevation, as well as automatic tracking for walking, running, swimming, and biking.

Wearable Blood Pressure Monitors
Omron Healthcare launched HeartGuide in 2019, the first wearable blood pressure monitor. Though it might look like a typical smartwatch, HeartGuide is an oscillometric blood pressure monitor that can measure blood pressure and daily activity – like steps taken, distance traveled, and calories burned.

HeartGuide can hold up to 100 readings in memory and all readings can be transferred to a corresponding mobile app, HeartAdvisor, for review, comparison, and treatment optimization. HeartAdvisor users have the ability to store, track, and share their data with their physician while also gaining insights to determine how personal habits affect their blood pressure.

Biosensors
Biosensors are up and coming wearable medical devices that are radically different from wrist trackers and smartwatches. The Philips' wearable biosensor is a self-adhesive patch that allows patients to move around while collecting data on their movement, heart rate, respiratory rate, and temperature.

Research from Augusta University Medical Center showed that this wearable device registered an 89% reduction in patient deterioration into preventable cardiac or respiratory arrest. This demonstrates the ability wearables have to improve patient outcomes and possibly reduce staff workload.

Advances in & future of medical devices
The wearable healthcare technology market is surging, and its maturation will put more wearable technology in the hands of consumers and US businesses. According to Business Insider Intelligence research, the total installed base of fitness tracker and health-based wearables in the US will grow at an annualized rate of 10% to surpass 120 million by 2023.

This upward trend in wearable fitness technology will influence the decision of insurers, health providers, and companies to take advantage of the benefits of wearable health monitoring devices.

Insurers can lessen the rising cost per patient by using wearables as a means of increasing customer life value. Wearable technology incentivizes behavior that reduces hospital visits and readmissions due to poorly managed personal health – 75% of users agree that wearables help them engage with their own health.

Companies are also seeing benefits in offering wearable healthcare technology to employees. According to Business Insider Intelligence research, healthier corporate culture is shown to reduce employee turnover – employers who offer five or more well-being 'best practices' had an average turnover of 18%, compared to 29% for those that offer two or fewer.

US consumer use of wearables increased from 9% to 33% in just four years, and this number will continue to grow as wearable technology becomes more conventional. Moreover, device connectivity will expand as more accurate wearable sensors are developed, opening the door for insurers and employers to influence healthy lifestyles and boost profitability.
'''

url_3_str = '''
CategoryCountry-Wide

Will farms only need boundary fences in future? Cheyenne Nicholson reports on developments in virtual fencing (VF) technology.

The past few decades has seen massive growth in our digital appetite. From our increasing reliance on smartphones in our day-to-day and business lives through to onfarm technology that helps us farm smarter.

The next wave of the ‘digital transformation of pastoral farming’ will bring out virtual fencing, a rival to traditional wire and batten fences.

Virtual fencing (VF) is a concept that has been around for a long time but in recent years has been progressing forward with leaps and bounds with the help of improved GPS technology. Animals wear GPS-enabled devices, in many cases a collar, that monitors their location relative to the invisible fence line on a digital farm map. To deter the animal from crossing the invisible line virtual fence the collar will emit a series of audible sounds as the animal approaches the fence. If they cross the line, a mild electrical pulse or vibration provides a corrective aversion.

Three companies are in various stages of development and onfarm trials in New Zealand. Halter, a Kiwi agritech start-up, Agersens and Vence. Halter was set to commercially launch its GPS-enabled cow collars in April. Agersens are working with AgResearch for their eShepherd technology.
‘There are two sides to the equation, one is looking after animals, the other is looking after pasture. How you manage livestock on pasture is fundamental to pastoral farming and VF helps on both sides.’

Aside from the obvious benefits of reducing fencing costs, yearly maintenance, fencing difficult areas and protecting riparian and other environmentally sensitive areas the technology also claims to have benefits in animal health by alerting you if a cow is lame, calving or in heat. Technology like EveryCow by Allflex is similar in that cows wear a collar or tag containing a small IoT (internet of things) chips that store and transmit data about their condition. EveryCow technology has been launched on dairy farms with Allflex saying beef will follow.

As well as being able to replace permanent and temporary fencing, VF collars can also be used to shift animals around the farm by creating a virtual fence behind the animal to move it along.

With about 150,000km of fencing in NZ the investment by farmers in traditional fencing in both building and maintaining, is massive. However with a lot of investment already made by farmers in fencing waterways, VF may have missed the boat for some to capitalise in that area.

Greg Shepherd researched virtual fencing for his 2018 Kellogg Rural Leadership report and says once a mechanism like VF is in place, it will create significant value for the industry.

With a background in farming and digital transformation Greg was excited to delve into VF and its potential effects on pastoral farming.

“There are two sides to the equation, one is looking after animals, the other is looking after pasture. How you manage livestock on pasture is fundamental to pastoral farming and VF helps on both sides.”

The 2018 KPMG Agribusiness Agenda captures biosecurity is top of mind for farmers, highspeed rural broadband is a close second (followed by food safety).

“Those three things are fundamental to helping our industry stay ahead. The cost of Mycoplasma bovis is estimated to be around $1 billion. That’s a lot of money that could be invested in other things like getting technology on to farms,” Greg says.

An internet connection (mobile or broadband) is required for the farmer to work with VF technology. Network connectivity and coverage for pastoral farmers is constantly discussed and is fundamental in the progress of innovation and use of digital technologies for farmers in remote locations, arguably where VF technology could have the most potential benefits.

However, despite the priority of high-speed rural broadband there is only one submission from Venture Southland representing primary sector concerns for the ‘Study of mobile telecommunications market in New Zealand’ as part of the Government’s jobs and innovation policy.

“What I found with some of my research is Venture Southland was the only regional organisation looking at what’s happening with the Commerce Commission’s mobile markets study. If communication infrastructure is important there needs to be more voices from the key industry stakeholders to help drive the framework that will determine where our mobile markets go.

“Connectivity leads into all these digital solutions, including VF, so the industry really needs to help articulate the value proposition.”

From Greg’s work with Spark he says he is mindful of the cost of the last mile but being able to get a scaleable solution that provides value to farmers will support investment in core infrastructure.

“With any investment, until the value proposition is clear no one will spend money. VF is very scaleable given cattle numbers but when the technology progresses to other livestock like sheep, goats and deer, suddenly there’s huge scale in getting farm assets connected creating a paradigm shift for the digital transformation of pastoral farming.”

The combination of VF geo-spatial data of land areas with the geo-location of individual animals could provide behavioural grazing patterns for zones within a paddock. This data could be used to build baseline datasets of carrying capacity and grazing behaviours to help determine pasture allocation. In a nutshell, you can use this information to set paddock rotation and get a better idea of how much animals are grazing (potential integration with other technologies such as Farmote and Space).

Although in theory VF could replace all fencing requirements, there will always be a need for physical fences.

“From discussions I’ve had and looking at the current legislation, boundary and road fences will always be critical as it gives farmers (and the public) reassurance they’ve done everything they can to keep livestock off roads. At the end of the day they still have a duty of care.”

From a biosecurity standpoint physical fences will remain important for between farm biosecurity management.

VF provides an opportunity to understand animal behaviour, health, welfare, security and manage pasture allocation which ultimately could enable measurement of pasture conversion to a primary product from an individual animal.

“Some of the problems we are facing; water quality, environmental management etc, isn’t going to be solved by yesterday’s technologies. We need to be able to enable these new technologies and invest in them and the farming community needs to be a driving force behind that.”
'''

def get_summary():
    summary = get_summary_func(url_2_str)
    return summary



# -----------------------------------------------------------------------------------------------------------------------------


# Sentiment Analysis

ec_data_df = pd.read_csv('tweet.csv')
ec_data_df['tweets'] = ec_data_df['content']
ec_data_df.head()

class CleanText(BaseEstimator, TransformerMixin):
    def remove_mentions(self, input_text):
        return re.sub(r'@\w+', '', input_text)

    def remove_urls(self, input_text):
        return re.sub(r'http.?://[^\s]+[\s]?', '', input_text)

    def clean_text(self, input_text):
        pattern = r'\n|\t|\r'
        return re.sub(pattern, ' ', input_text)

    def remove_digits(self, input_text):
        return re.sub('\d+', '', input_text)

    def clean_extra_space(self, input_text):
        pattern = r'\s{2,}'
        return re.sub(pattern, ' ', input_text)

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, **transform_params):
        clean_X = X.apply(self.remove_mentions).apply(self.remove_urls).apply(
            self.clean_text).apply(self.remove_digits).apply(self.clean_extra_space)
        return clean_X

clean = CleanText()
cleaned_data_df = ec_data_df.copy()
cleaned_data_df.tweets = clean.fit_transform(cleaned_data_df.tweets)
cleaned_data_df.tweets[0]
# cleaned_data_df.columns

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score
def sentiment_analyzer_label(compound):
    if compound >= 0.05:
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negetive'
    else:
        sentiment = 'neutral'
    return sentiment

cleaned_data_df['scores'] = cleaned_data_df['tweets'].apply(lambda x : sentiment_analyzer_scores(x))
final_data_df = cleaned_data_df.copy()
final_data_df['negetive'] = final_data_df['scores'].apply(lambda x : x['neg'])
final_data_df['neutral'] = final_data_df['scores'].apply(lambda x : x['neu'])
final_data_df['positive'] = final_data_df['scores'].apply(lambda x : x['pos'])
final_data_df['compound'] = final_data_df['scores'].apply(lambda x : x['compound'])
final_data_df['sentiment'] = final_data_df['compound'].apply(lambda x : sentiment_analyzer_label(x))

viz_df = final_data_df[['date_time', 'sentiment']]

viz_df['date_time'] = pd.to_datetime(viz_df['date_time'])
viz_df['date'] = [d.date() for d in viz_df['date_time']]
viz_df['time'] = [d.time() for d in viz_df['date_time']]
viz_df['day'] = [d.day for d in viz_df['date']]
viz_df['month'] = [d.month for d in viz_df['date']]
viz_df['year'] = [d.year for d in viz_df['date']]

groupby_date = viz_df.groupby( ['date',
     'sentiment']).agg({
    'sentiment': {'Count':'count'}})
groupby_date = groupby_date.reset_index()
groupby_date.columns=groupby_date.columns.droplevel(1)
groupby_date.columns = ['date', 'sentiment', 'count']
groupby_date.date = groupby_date.astype(str)
# groupby_date[groupby_date.count < 70]
groupby_date =  groupby_date.loc[groupby_date['count'] < 60,:]

negetive_df = groupby_date[groupby_date.sentiment == 'negetive']
negetive_df = negetive_df.reset_index(inplace=False)[['date', 'sentiment','count']]
positive_df = groupby_date[groupby_date.sentiment == 'positive']
positive_df = positive_df.reset_index(inplace=False)[['date', 'sentiment','count']]
neutral_df = groupby_date[groupby_date.sentiment == 'neutral']
neutral_df = neutral_df.reset_index(inplace=False)[['date', 'sentiment','count']]


def plot1():
    # df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=negetive_df.date, y=negetive_df['count'], name="negetive",
                             line_color='red'))

    fig.add_trace(go.Scatter(x=positive_df.date, y=positive_df['count'], name="positive",
                             line_color='dimgray'))

    fig.add_trace(go.Scatter(x=neutral_df.date, y=neutral_df['count'], name="neutral",
                             line_color='deepskyblue'))


    fig.update_layout(title_text='Time Series with Rangeslider',
                      xaxis_rangeslider_visible=True)

    plot_div = plot(fig, output_type='div',filename='time_series')

    return plot_div
