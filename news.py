import requests
import time


# トップニュースのID一覧を取得
def get_top_stories_id():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    story_ids = response.json()
    return story_ids


# 各ニュースIDから詳細情報を取得
def get_story_by_id(story_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url)
    story = response.json()
    return story


# タイトルとURLだけを抽出
def extract_title_and_url(story):
    title = story.get("title", "No Title")
    url = story.get("url", "No URL")  # URLがない場合もある
    return {"title": title, "link": url}


# メイン処理
def main():
    story_ids = get_top_stories_id()

    print(" Hacker News トップニュース（最大10件）\n")
    for story_id in story_ids[:10]:
        time.sleep(1)  # APIへの負荷軽減
        story = get_story_by_id(story_id)
        if story and "title" in story:
            info = extract_title_and_url(story)
            print(info) 


if __name__ == "__main__":
    main()
