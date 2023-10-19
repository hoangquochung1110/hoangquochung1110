import feedparser
from pathlib import Path

def main():
    bio = [
        "✌🏻 Hi, I'm Hung Hoang and welcome you to my Github space.\n",
        "💻 I'm Web developer working with Python/Django.\n",
        "🇻🇳 I'm living in Hochiminh city, Vietnam.\n",
        "🚴🏻 In my spare time, I rides with my single-speed bike.\n",
    ]
    chunks = []
    chunks.extend(bio)
    chunks.extend(get_latest_posts())

    readme = Path(__file__).parent / "README.md"
    readme.write_text("\n".join(chunks))

def get_latest_posts():
    chunks = ["## Latest blog posts\n"]
    posts = feedparser.parse("https://hoangquochung1110.github.io/static-site-generator/feed.xml")["entries"][:5]
    chunks.extend(
        [
            f'* [{post["title"]}]({post["link"]})'
            for post in posts
        ]
    )
    return chunks

if __name__ == "__main__":
    main()
