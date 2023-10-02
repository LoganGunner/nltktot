IRC logs sourced from https://frontrowcrew.com/irc/logs/

# Python Libraries:

• NLTK

• re


Chatwork contains files used for scraping chats out of a file and recognizing the different parts with RegEx.

Examples contains practice examples of various NLTK methods and practices that are going to be used in the analysis of the chats.

# Current approach:

• recognize named entities in chat

• create objects based on named entities

• map aliases of named entities to their objects by searching for verbs that state what they are etc.

• track a "timeline" of verbs/actions affecting named entities and assigning to their objects

# Goals/Implementation

• Dashboard with GANTT graph of "timeline" or lifespan of tasks.
    - Starting with top level task lifespan, with smaller sublevels.
    - Include surrounding chats during the lifespan as separate data points to view just in case.

• Postgres Database containing chat logs, key words/phrases.

• Python scripts to organize chat data and create relationships/connections between entities recognized in chats.