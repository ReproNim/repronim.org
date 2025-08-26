---
title: Science Highlights
type: docs
weight: 40
---

[The Science Highlights series](https://repronim.wordpress.com/category/sciencehighlight/) provides high-level, easy to read summaries of exciting findings from ReproNim and the greater reproducible neuroimaging community.

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
            var posts = JSON.parse(req.responseText);
            highlights_div.innerHTML = "";
            var ul = document.createElement("ul");
            highlights_div.appendChild(ul);
            var n_items = 0;
            for(var i = 0;i < posts.length;i++) {
                var a = document.createElement("a");
                a.href = posts[i].link;
                a.target = "_blank";
                var li = document.createElement("li");
                li.appendChild(a)
                a.innerHTML = posts[i].title.rendered.replace(/^[ ]*science highlight:[ ]*(.*)[ ]*$/i, "$1");
                if(!/[\.!?]$/.test(a.innerHTML)) {
                    a.innerHTML = a.innerHTML + ".";
                }
                // WordPress will generate an excerpt from the post if 
                // none is given.  The generated excerpts tend to be 
                // long, so a length check should exclude them.
                if(posts[i].excerpt.rendered.length < 500) {
                    const excerpt = posts[i].excerpt.rendered.replace(/^<p>(.*)<\/p>.*/i, "$1");
                    li.appendChild(document.createTextNode(" " + excerpt));
                }
                var date = new Date(posts[i].date);
                li.appendChild(document.createTextNode(" (" + date.toLocaleDateString() + ")"));
                ul.appendChild(li);
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
