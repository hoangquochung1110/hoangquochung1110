import feedparser
from pathlib import Path

def main():
    chunks = []
    chunks.extend(get_latest_posts())

    readme = Path(__file__).parent / "README.md"
    readme.write_text("\n".join(chunks))

def get_latest_posts():
    chunks = ["## Latest blog posts\n"]
    posts = feedparser.parse("https://www.hung.codes/feed.xml")["entries"][:5]
    chunks.extend(
        [
            f'* [{post["title"]}]({post["link"]})'
            for post in posts
        ]
    )
    return chunks

if __name__ == "__main__":
    main()
