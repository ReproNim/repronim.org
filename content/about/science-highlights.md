---
title: Science Highlights
type: docs
weight: 40
---

<div id="science-highlights">
See <a href="https://repronim.wordpress.com/category/sciencehighlight/">our science highlights</a>.
</div>

<script defer>
function load_highlights() {

    highlights_div = document.getElementById("science-highlights");

    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        // wait for DONE
        if(req.readyState != 4) {
            return;
        }
        if(req.status == 200) {
            var posts = eval("(" + req.responseText + ")");
            highlights_div.innerHTML = "";
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
                highlights_div.appendChild(div);
                n_items++;
            }
        var p = document.createElement("p");
        p.innerHTML = '<a href="https://repronim.wordpress.com/category/sciencehighlight/" target="_blank">See all Science Highlights</a>.';
        highlights_div.appendChild(p);
        }
    }

    // limit list length with paginated request with category filter
    req.open("GET", "https://public-api.wordpress.com/wp/v2/sites/repronim.wordpress.com/posts?categories=783350058&per_page=10", true);

    req.send();

    return;

}

load_highlights();
</script>
