# MyAnimeList-Profile-Scraper

> Developed using Python and BeautifulSoup

#### MyAnimeList (MAL) Profile Scraper using the MAL API and BeautifulSoup

I have always wanted to try web scraping. I think it's so interesting that you can automate the fetching of data online. I believe that it can be useful for any task. I also like anime and I used to regularly use a website called https://MyAnimeList.net, where you can update your anime and manga lists and share your interests.

MyAnimeList also has a public API. The API is great, and I used it to fetch the user's animelist and mangalist. However, the API does not return all the information I need such as the user profile data without authentication. I do not want to use authentication. Thus, I decided to do web scraping to fetch the information that I need about the user profile without needing to authenticate. MyAnimeList also allows web scraping because other users have done it (https://jikan.moe). It was really fun to web scrape the html elements one by one.

#### What the program does:

- Fetches the user's top and bottom anime and manga from his or her animelist and mangalist using the MAL API (information for each of the anime and manga such as the anime and manga title, status, score, is_rewatching, is_rereading, num_episodes_watched, num_volumes_read, num_chapters_read, updated_at, start_date, finish_date)
- Scrapes the user's public profile information using BeautifulSoup (information such as Last Online, Gender, Birthday, Location, Joined, Forum Posts, Reviews, Recommendations, Interest Stacks, Blog
  Posts, Clubs, Number Of Friends, About Me, Anime Days, Anime Mean Score, Anime Watching, Anime Completed, Anime On-Hold, Anime Dropped, Anime Plan to Watch, Anime Total Entries, Rewatched, Episodes, User Last Anime and Manga Updates, Manga Days, Manga Mean Score, Manga Reading, Manga Completed, Manga On-Hold, Manga Dropped, Manga Plan to Read, Manga Total Entries, Reread, Chapters, Volumes, User Favorites, User Profile Comments)

#### Requirements:

1. Python
2. requests
3. os
4. dotenv
5. BeautifulSoup
6. Note that you will need to write your MAL Client ID which can be obtained through your MAL account on the API tab on a .env file

### Resources:

- https://myanimelist.net/apiconfig/references/api/v2
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
