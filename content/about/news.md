---
title: News
date: 2024-12-04T11:52:52-05:00
type: docs
weight: 40
---

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
                // 103 is News
                if(!posts[i].categories.includes(103)) {
                    continue;
                }
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
                // limit list length
//                if(n_items == 5) {
//                    break;
//                }
            }
        var p = document.createElement("p");
        p.innerHTML = '<a href="https://repronim.wordpress.com/category/news/" target="_blank">See all news</a>.';
        news_div.appendChild(p);
        }
    }

    req.open("GET", "https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com/posts", true);
    req.send();

    return;

}

load_news();
</script>
