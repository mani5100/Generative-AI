from langchain.vectorstores import FAISS
from langchain.schema import Document

from langchain.embeddings import OpenAIEmbeddings

document1 = Document(
    page_content="Babar Azam, one of the world's top T20 batsmen, leads Peshawar Zalmi with elegance and consistency. He joined the franchise in 2023 and instantly became the face of the team, known for his stylish cover drives and calm leadership.",
    metadata={
        "team_name": "Peshawar Zalmi",
        "city": "Peshawar",
        "titles_won": 1,
        "founded_year": 2015
    }
)

document2 = Document(
    page_content="Shaheen Shah Afridi is the most celebrated player in Lahore Qalandars, not just for his fierce bowling but also for captaining the side to their first-ever PSL title in 2022. His ability to swing the ball at high pace makes him a game-changer.",
    metadata={
        "team_name": "Lahore Qalandars",
        "city": "Lahore",
        "titles_won": 2,
        "founded_year": 2015
    }
)

document3 = Document(
    page_content="Shadab Khan, the young and dynamic all-rounder, is the heartbeat of Islamabad United. Known for his sharp leg-spin and explosive lower-order batting, he has played a vital role in both of the team's PSL titles.",
    metadata={
        "team_name": "Islamabad United",
        "city": "Islamabad",
        "titles_won": 2,
        "founded_year": 2015
    }
)

document4 = Document(
    page_content="Mohammad Rizwan, the captain of Multan Sultans, is respected for his incredible work ethic, consistent batting, and leadership. He led the Sultans to their first PSL title in 2021 and has been a pillar of stability at the top of the order.",
    metadata={
        "team_name": "Multan Sultans",
        "city": "Multan",
        "titles_won": 1,
        "founded_year": 2017
    }
)

document5 = Document(
    page_content="Sarfaraz Ahmed, the former captain of Pakistan's national team, is the most experienced figure in Quetta Gladiators. His leadership helped the team win the PSL title in 2019, and he remains the emotional core of the squad.",
    metadata={
        "team_name": "Quetta Gladiators",
        "city": "Quetta",
        "titles_won": 1,
        "founded_year": 2015
    }
)

document6 = Document(
    page_content="Imad Wasim, known for his tactical bowling and aggressive batting, is one of the key players in Karachi Kings. He played a major role in helping the team secure its maiden PSL title in 2020.",
    metadata={
        "team_name": "Karachi Kings",
        "city": "Karachi",
        "titles_won": 1,
        "founded_year": 2015
    }
)
document7= Document(
    page_content="Shahid Afridi, the legendary all-rounder, is a crowd favorite and a key player for Peshawar Zalmi. His explosive batting and charismatic personality have made him an icon in the PSL.",
    metadata={
        "team_name": "Peshawar Zalmi",
        "city": "Peshawar",
        "titles_won": 1,
        "founded_year": 2015
    }
)
document8= Document(
    page_content="Ben Dunk, the Australian batsman, is known for his explosive batting and has been a key player for Lahore Qalandars. He holds the record for the highest individual score in PSL history.",
    metadata={
        "team_name": "Lahore Qalandars",
        "city": "Lahore",
        "titles_won": 2,
        "founded_year": 2015
    }
)

docs= [document1, document2, document3, document4, document5, document6,document7,document8]

from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
vectorstore.similarity_search(
    query="Who among these are batsman?",
    k=3
)
document9= Document(
    page_content="Mohammad Hafeez, the veteran all-rounder, has been a consistent performer for Lahore Qalandars. His experience and ability to play spin make him a valuable asset in the PSL.",
    metadata={
        "team_name": "Lahore Qalandars",
        "city": "Lahore",
        "titles_won": 2,
        "founded_year": 2015
    }
)

vectorstore.add_documents([document9])

vectorstore.get_by_ids(['640fb051-7b25-4e57-8583-17347b79d3d6'])

vectorstore.similarity_search_with_relevance_scores(
    query="Who is babar",
    k=1
)

vectorstore.delete(ids=['84cf1895-a962-4fb0-960a-5e0b67d17256'])

