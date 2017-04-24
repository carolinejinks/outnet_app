# Experience Fashion


## The What

This is my web app that allows users to access all they need for inspired and affordable shopping. On the home page it features photos posted by designers and labels within the database from their official Instagram pages. Energy is brought to the page from my playlist made of compile clips of songs featured in the designer's Fashion Week 2017 runway shows. The designer list as a whole is derived from the [Outnet.com](https://www.theoutnet.com/en-US/) and when the user clicks one they are taken to a unique information page. Each page shows the designer's name, a link to shop their work via the [Outnet.com](https://www.theoutnet.com/en-US/Shop/Designers), and a summary of the designer that matches that of their Wikipedia page. If the designer does not exist on Wikipedia, the description will say, "There is no description available for this label, but you can still click the link to see their styles!"

## The How

### Images

The slideshow of images was created using a Bootstrap carousel. In order to make sure my images were legal, I embedded Instagram posts into the carousel item div and included the necessary scripts at the bottom of my index.html page. The difficulty with this is that Instagram has a fixed size for their images, and the carousel has a fixed with for the images placed within it. To fix this, as well as to center the carousel itself, I placed the entire carousel within a div with an id of wrapper. The wrapper was then set to the width of the Instagram image, which was 600 pixels. I then centered the carousel using text-align: center;

###Audio
The audio was trickier. I intended to use the Spotify embed technique, so that I could create a full playlist and put it on my app legally. However, after embedding my playlist and testing my site, the playlist would stop itself after a few seconds and show a text box that said, "If you would like to listen to the whole playlist, sign into Spotify here." In other words, the user had to sign in to their account to actually listen to the music, and if someone had no account at all then the playlist was useless. To achieve the effect of having music playing while browsing my site, I edited together 30-second clips of my "runway" song and faded them together in one audio file. I gave the audio-player an id named songs and hid it using CSS (display: none;). This way, when the user visits my page the music automatically plays and the page still looks sleek and professional. The songs used are credited within the footer in the order that matches the playlist.

### Scraping
The data was collected using a scraper I built for the Outnet. I scraped both the designer name and the link to shop their work within one file and appended them to rows so they could be written to a csv.

```designer = []
links = []

for link in bsObj.find("div", {"class":"grid-12"}).findAll("a"):
    if 'data-urlkey' in link.attrs:
        designer.append(link.attrs['data-urlkey'])

for link in bsObj.find("div", {"class":"grid-12"}).findAll("a"):
    if 'href' in link.attrs:
        links.append(link.attrs['href'])

c.writerow( [designer, links] )
n = 0
for design in designer:

    c.writerow( [designer[n], links[n]] )
    n = n + 1
```
The designer summaries were collected using a Wikipedia python library that I was able to $pip install and run a for loop that inserted the designer's name from my scraper into the call for each Wikipedia summary.

```summaries=[]
for n in designer:
    try:
        sum = wikipedia.summary(n)
        summaries.append(sum)
        print(summaries)
    except wikipedia.exceptions.PageError:
        continue
    except wikipedia.exceptions.DisambiguationError:
        continue
```
It was necessary to use try and except so that the function would run even if the Wikipedia page did not exist. This way,I was able to get summaries for every designer that was on Wikipedia out of my 469 designers.

These summaries were then copy and pasted into my CSV, which I then converted into a Python dict so that it could be used in my **data.py** file for my Flask app.

### Flask
My Flask app gives each designer a unique ID and pairs it with the designer's name. When the list of designers is created, it pairs the id and designer and creates a url to the designer's page.

`<li value="{{ pair[0] }}"><a href="{{ url_for('designer', id=pair[0]) }}">{{ pair[1] }}</a></li>`

The carousel and audio are only on the index.html page, while the information for each designer is on the designer.html page. In order to ensure that the link to shop each designer was active I modified my code to this:

`<p>You can shop this designer on the Outnet.com by following the link provided: <a href="{{ link }}">Shop {{ designer }}</a></p>`

I used on CSS page for both html pages, so that they had consistent design. I also ensured that it was responsive by creating a media query with a max-width of 400 pixels, this way when viewed on an iPhone 6, the list of designers will still be legible.

## Conclusion
I was able to complete everything I hoped to for my web app, with the exception of modifications that allowed for a better user experience. With my app, anyone interested in fashion can view looks and hear music that is seen and heard on the runway, as well as learn more about those that created them and where they can purchase looks of their own.
