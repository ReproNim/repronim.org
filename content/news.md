---
linkTitle: News
title: "" # Empty so we can have each section on right bar while preventing dup titles
date: 2024-12-04T11:52:52-05:00
type: docs
weight: 40
---

## News

{{< wordpress-posts 
    category="103" 
    id="news-posts" 
    linkurl="https://repronim.wordpress.com/category/news/" 
    linktext="news" 
    numentries="10"
    apibase="https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com"
>}}

## Science Highlights

[The Science Highlights series](https://repronim.wordpress.com/category/sciencehighlight/) provides high-level, easy to read summaries of exciting findings from ReproNim and the greater reproducible neuroimaging community.

{{< wordpress-posts 
    category="783350058" 
    id="science-highlights-posts" 
    linkurl="https://repronim.wordpress.com/category/sciencehighlight/" 
    linktext="science highlights" 
    showexcerpt="true" 
    striptitleprefix="Science Highlight"
    numentries="10"
    apibase="https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com"
>}}

## Community Events

{{< wordpress-posts 
    category="42098758"
    id="community-events-posts" 
    linkurl="https://repronim.wordpress.com/category/communityevent/" 
    linktext="community events" 
    showexcerpt="true" 
    numentries="10"
    apibase="https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com"
>}}
