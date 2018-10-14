# Lyric Learner

Helps people learn languages by real-time translating foreign songs with easy lyrics.

## Inspiration
We started by brainstorming different ideas. For the education track, we thought about how difficult it can be to learn a foreign language, especially if learners start later in life. To remediate this issue, we tried coming up with ways to make learning a foreign language more fun. We all agreed that songs were a great way to learn new vocabulary and grammar structures. Additionally, songs introduce learners to colloquial phrases that they would otherwise not be exposed to in a classroom. Some of us have tried this method before, but it’s difficult to find songs that are relevant to our language proficiency. This tool is created to alleviate this issue. 

## What it does
Lyric Learner is a desktop app that connects users with songs in the language they are learning according to their proficiency level. It pulls up the lyrics of the song and has a translation feature to help users learn the vocabulary words through the lyrics of the song. It’s a more interactive way to learn a language. Currently, the program only works for German to English and English to German, but eventually, we hope to expand the program to other languages.

## How we built it
We built this project using multiple APIs to access, process, and translate song lyrics. We retrieve song lyrics by scraping genius lyric webpages. We processed these lyrics to get a difficulty score. We use that score to determine how advanced the user needs to be in order to understand the song. From there, we created a function to scan and translate the song lyrics for users to use to help them learn the language.  

## Challenges we ran into
Connecting the APIs in the right way was challenging. We also struggled with getting the lyrics of the songs and processing the words individually.

## Accomplishments that we are proud of
Getting the individual words to translate and appear on screen was a huge and difficult accomplishment. 

## What we learned
We learned a lot about APIs through this project and the interaction between front-end and back-end development.

## What’s next for LyricLearner
LyricLearner could be expanded into a paid service that allows free users to view song titles and paid users are given access to the lyrics with in-line translation. A tool that could be paired with LyricLearner in the future is a Spotify playlist creator. The playlist creator would generate songs based on user language proficiency and Spotify user data to suggest songs that the user would enjoy and would be helpful for language learning. Additionally, this platform could be enhanced through a machine learning algorithm that allows users to respond to the song’s helpfulness in their language learning. This algorithm would enhance the difficulty calculator that we created for our program. There is also room for this platform to integrate with online language courses, such as Duolingo, so that they can integrate music into their courses. 

## Contributors
* Jake Derry
* Ryan Ferner
* Radu Vasilescu 
* Lillian Childrey
* Hamza Waheed

