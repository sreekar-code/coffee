#!/usr/bin/env python3
"""Generate rss.xml from blog posts in the blog/ directory."""

import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


BASE_URL = "https://sreekar.coffee"


class PostParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_tag = ""   # from <title>
        self.h1 = ""          # from <h1>
        self.date = ""
        self.paragraphs = []
        self._in_title = False
        self._in_h1 = False
        self._in_date = False
        self._in_section = 0  # depth counter
        self._in_p = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "section":
            self._in_section += 1
        elif tag == "p":
            if "date" in attrs.get("class", ""):
                self._in_date = True
            elif self._in_section:   # only capture <p> inside <section>
                self._in_p = True
                self._buf = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "section":
            self._in_section = max(0, self._in_section - 1)
        elif tag == "p":
            if self._in_date:
                self._in_date = False
            elif self._in_p:
                text = self._buf.strip()
                if text:
                    self.paragraphs.append(text)
                self._in_p = False

    def handle_data(self, data):
        if self._in_title:
            self.title_tag += data
        elif self._in_h1:
            self.h1 += data
        elif self._in_date:
            self.date += data
        elif self._in_p:
            self._buf += data


def parse_date(date_str):
    """Parse '19th Oct, 2025' → datetime."""
    clean = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", date_str).replace(",", "").strip()
    for fmt in ("%d %b %Y", "%d %B %Y"):
        try:
            return datetime.strptime(clean, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return datetime.now(tz=timezone.utc)


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def generate_rss():
    blog_dir = Path("blog")
    posts = []

    for html_file in sorted(blog_dir.glob("*.html")):
        if html_file.name == "index.html":
            continue

        parser = PostParser()
        parser.feed(html_file.read_text(encoding="utf-8"))

        # prefer <h1>, fall back to <title> tag
        title = (parser.h1.strip() or parser.title_tag.strip() or html_file.stem)
        date_str = parser.date.strip()
        pub_date = parse_date(date_str) if date_str else datetime.now(tz=timezone.utc)
        description = parser.paragraphs[0] if parser.paragraphs else ""
        url = f"{BASE_URL}/blog/{html_file.name}"

        posts.append({
            "title": title,
            "url": url,
            "pub_date": pub_date,
            "description": description,
        })

    posts.sort(key=lambda p: p["pub_date"], reverse=True)

    items = "\n".join(
        f"""    <item>
      <title>{escape(p['title'])}</title>
      <link>{p['url']}</link>
      <guid isPermaLink="true">{p['url']}</guid>
      <pubDate>{p['pub_date'].strftime('%a, %d %b %Y 00:00:00 +0000')}</pubDate>
      <description>{escape(p['description'])}</description>
    </item>"""
        for p in posts
    )

    last_build = datetime.now(tz=timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>sreekar.coffee</title>
    <link>{BASE_URL}</link>
    <description>Personal coffee blog — AeroPress experiments, tasting notes, and coffee rabbit holes.</description>
    <language>en-us</language>
    <lastBuildDate>{last_build}</lastBuildDate>
    <atom:link href="{BASE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
{items}
  </channel>
</rss>
"""

    Path("rss.xml").write_text(rss, encoding="utf-8")
    print(f"Generated rss.xml with {len(posts)} posts")


if __name__ == "__main__":
    generate_rss()
