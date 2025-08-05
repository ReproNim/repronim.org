---
title: News
date: 2024-12-04T11:52:52-05:00
type: docs
weight: 40
---

<link rel="stylesheet" href="/css/science-highlights.css">

## Science Highlights

<div class="science-highlights">
<div class="highlight-item">
<h3>Variability in the analysis of a single neuroimaging dataset by many teams</h3>
<p><em>Botvinik-Nezer et al. (2020), Nature</em></p>
<p>A groundbreaking study revealed significant variations in brain activation patterns when 70 independent research teams analyzed the same neuroimaging dataset using their own methods. Despite using identical data, teams reached different conclusions about brain activity, highlighting critical challenges in neuroimaging reproducibility. This landmark research demonstrates why standardized analysis pipelines and transparent reporting are essential for reliable neuroscience findings. The study's findings have profound implications for how we interpret brain imaging research and underscore the importance of initiatives like ReproNim in promoting reproducible neuroimaging practices across the scientific community.</p>
<p><strong>Publication:</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/30792636/" target="_blank">PubMed: 30792636</a></p>
</div>
</div>

## Latest News

<div id="news">
See <a href="https://repronim.wordpress.com/category/news/">our news site</a>.
</div>

<script defer>
function load_news() {

    news_div = document.getElementById("news");

    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        // wait for DONE
        if(req.readyState != 4) {
            return;
        }
        if(req.status == 200) {
            var posts = eval("(" + req.responseText + ")");
            news_div.innerHTML = "";
            var n_items = 0;
            for(var i = 0;i < posts.length;i++) {
                var a = document.createElement("a");
                a.href = posts[i].link;
                a.target = "_blank";
                a.innerHTML = posts[i].title.rendered;
                var div = document.createElement("div");
                div.appendChild(a)
                var date = new Date(posts[i].date);
                div.appendChild(document.createTextNode(" (" + date.toLocaleDateString() + ")"));
                news_div.appendChild(div);
                n_items++;
            }
        var p = document.createElement("p");
        p.innerHTML = '<a href="https://repronim.wordpress.com/category/news/" target="_blank">See all news</a>.';
        news_div.appendChild(p);
        }
    }

    // limit list length with paginated request with category filter
    req.open("GET", "https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com/posts?categories=103&per_page=10", true);
    req.send();

    return;

}

load_news();
</script>
