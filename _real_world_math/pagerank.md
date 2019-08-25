---
title: "Understanding Google's (old) PageRank Algorithm"
collection: real_world_math
date: 2019-8-23
permalink: /real_world_math/pagerank/
tags:
  - google
  - networks

---

So most people probably know the PageRank Algorithm as the way Google ranks the pages that show up after a google search. Many of those people, like myself, may have thought it was named "PageRank" because of this, when in reality it was named after Larry Page, one of the founders of Google. The cool thing is, this algorithm goes far beyond just ranking website pages and can technically be used to rank mostly anything in a connected society. (Unfortunately, I'm pretty sure Google's done far more by this point to polish their algorithm, and even if I worked there I doubt I could say anything about it) In this post, I explain it in a digestible manner and show how it can be used to rank College Basketball teams and movie actors, as well as websites.

Now a bit of prior knowledge that'll help is certainly a bit of graph theory. There's a lot of places where that's pretty easy to learn, so I won't cover too much of it here. But funny thing is, a lot of the fancy PageRank algorithm simply stems from the old network idea of how things are connected to each other. One website has a link to one or more websites, and on it goes. See **Figure 1** for example. That gives us a simple adjacency matrix to work with.

![graph1](https://joeleung16.github.io/images/PageRank/graph1.png)

*Figure 1*: An example graph of how websites are connected. Imagine that, say, website 'a' has a hyperlink to 'b', 'c', and 'd'.

Now there is a bit of variation. Though I can't think of a website like this off of the top of my head, some sites don't link to other websites. So like in node 'b' in **Figure 1**, let's be real, anyone can go anywhere they want to, so in this algorithm we adjust it to say that from website 'b', someone can go wherever they want. Thus we have a new graph and corresponding adjacency matrix like **Figure 2**.

![graph1](https://joeleung16.github.io/images/PageRank/graph2.png)

*Figure 2*: Updated from Figure 1

Now...until I find the time to edit this...I'm gonna skip a lot. What I skip shouldn't detract from understanding, but it's definitely glossing over a lot of theory as to why we can do what we can do. I don't like this, because justifying what we do is immensely important, partly for reproducibility and the obvious fact to show that I'm not just pulling this stuff our of my butt. But alas...I'm here to help understanding in general, for myself and maybe for like, the 2 people that read this. So...

As with most models in general, we can't be certain about what's going to happen, so we assign probability to things. In this case, we assume that the probability of going from one site to another is how many hyperlinks link to that site, in other words, we normalize our matrix. One other detail is that, well who knows how long someone stays on a website before getting bored? Well hey welcome to math where if you're not sure about an extra factor, add an epsilon to signify "some error that we can't account for". After mathing things around...we get a really convenient equation to simply solve for the eigenvalues of that epsilon * the new matrix + [(1 - epsilon)/n]* E where E is just a matrix of ones to make the matrices add up. And that's it! PageRank is ultimately a fancy way of looking at things and doing an old eigenvector calculation on it. Again, why that works is something I don't know how to type in Markdown, but hey! It works! If you wanna test it out, my code's at the bottom and the website data is labelled accordingly as well.

And the basketball and movie data stuff, you ask? Yeah at this point it's literally just one more step. The way you weight the edges. Right so like with basketball, I just made sure the edges point from who lost to who won, and how many games they lost to that winning team. As for the movies, meh, just make sure who comes up first in the billing order is pointed to, and then see how many movies they shared. Feel free to play with it for yourself.


[PageRank Code](https://joeleung16.github.io/files/PageRank/pagerank.py)

[Movie Data](https://joeleung16.github.io/files/PageRank/top250movies.txt)

[Website Data](https://joeleung16.github.io/files/PageRank/web_stanford.txt)

[NCAA 2017 Data](https://joeleung16.github.io/files/PageRank/ncaa2017.csv)

[NCAA 2010 Data](https://joeleung16.github.io/files/PageRank/ncaa2010.csv) Using this data with epsilon = 0:85, the top three ranked teams (of the 607 total teams)
should be UConn, Kentucky, and Louisville, in that order. That season, UConn won the
championship, Kentucky was a semifinalist, and Louisville lost in the first tournament round
(a surprising upset).



Testing: $$e = mc^2$$
