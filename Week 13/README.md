# Week 11: best practices

This week we'll make a pause before going to more advanced topics, and talk about best practices

#### In preparation for this week:

-   read/listen/watch as much as you can from the annotated materials below

------------------------------------------------------------------------

It is always delightful to start with the masters, and there is no larger master in this area than [Don Knuth](https://www.nytimes.com/2018/12/17/science/donald-knuth-computers-algorithms-programming.html). You may have heard his name because he's authored the still ongoing collection of books - [The Art of Computer Programming](https://www-cs-faculty.stanford.edu/~knuth/taocp.html). Let's begin this week by reading his 1974 ACM Turing Award Lecture - [**Computer Programming as an Art**](https://dl.acm.org/ft_gateway.cfm?id=1283929&type=pdf). An incredibly thoughtful and scholarly view of what coding is - and should be - all about:

> computer programming is an art, because it applies accumulated knowledge to the world, because it requires skill and ingenuity, and especially because it produces objects of beauty.

One thing we should not forget is that **computational thinking is the deeper skill for Data Scientists to learn**. Unfortunately, it is not always natural for social scientists to think as Data Scientists when it comes to exploiting the advantages of computing processes.

A fantastic introduction to starting to leverage mental tools developed in computer science is Jeanette Wing's (2006) article - [**Computational Thinking**](https://dl-acm-org.ezproxy.cul.columbia.edu/doi/10.1145/1118178.1118215) - where she carefully describes what computer thinking is about and why it is tremendously useful for all disciplines. Understanding this will go a long way to collaborate effectively with data and machine-learning engineers. In her own words:

> Computational thinking involves solving problems, designing systems, and understanding human behavior, by drawing on the concepts fundamental to computer science. Computational thinking includes a range of **mental tools** that reflect the breadth of the field of computer science. <br/> [...]<br/> Computational thinking is using abstraction and decomposition when attacking a large complex task or designing a large complex system. It is **separation of concerns**. It is choosing an appropriate representation of a problem or modeling the relevant aspects of a problem to make it tractable. [...] It is modularizing something in anticipation of multiple users or prefetching and caching in anticipation of future use. <br/>\
> [...] <br/> Computational thinking is thinking in terms of **prevention**, **protection**, and **recovery from worst-case scenarios** through **redundancy**, **damage containment**, and **error correction**.

With that background, we can jump directly to reading about coding best practices for social scientists in this old article by Jonathan Nagler (1995) - [**Coding Style and Good Computing Practices**](http://www.jstor.org/stable/420315) - providing very useful advice on coding as related to ETL and data analysis. Still incredibly relevant advice. If you only have a few minutes to skim, that piece was more recently (2015) updated and summarized in a blog post - [**Writing Good Code**](https://blog.oup.com/2015/02/jonathan-nagler-writing-good-code/).

For more advanced hackers, you will benefit from a more systematic approach to improving your coding practices by reading a few more specialized pieces:

-   [**The Practice of Programming**](http://www.informit.com/store/practice-of-programming-9780201615869), read the Preface, Chapters 1, 3, 5, 6, and the Epilogue
-   [**The Structure and Interpretation of Computer Programs**](https://mitpress.mit.edu/sicp/full-text/book/book.html) to better understand object-oriented languages
-   [**The Pragmatic Programmer**](https://www.amazon.com/dp/020161622X/ref=cm_sw_su_dp?tag=devtools-20) with general advice on how to be a good programmer/coder
-   [SOLID design principles: the single responsibility explained](https://stackify.com/solid-design-principles/) as an introduction to a principle that would make your code easier to implement and prevents unexpected side effects from future changes
-   [**Design Patterns: Elements of Reusable Object-Oriented Software**](https://stackify.com/solid-design-principles/) with incredibly useful advice to craft code with an eye to increase flexibility and reusability of your code
-   [**Fluent Python: Clear, Concise and Effective Programmings**](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming-ebook-dp-B0131L3PW4/dp/B0131L3PW4/ref=mt_other?_encoding=UTF8&me=&qid=1617839864) to take you to the next level in your Python 3.x programming.

### Coding Style in Python

Guido van Rossum, the creator of Python, has co-authored this [Style Guide for Python Code](https://peps.python.org/pep-0008/). A key insight that Guido makes here is that code is read more much more frequently than it is written, which is why making it consistent is so important. There are other style guides out there too, but this is a great one to start with. See [this](https://docs.python-guide.org/writing/style/) chapter from the Hitchhiker's Guide to Python for another example.

### Coding Style in R

A lot of knowledge has been accumulated over the last years and systematized in coding style rules by the RStudio folks. For a book-version, you may want to read [Hadley Wickham](http://hadley.nz/)'s chapter on [R code](https://r-pkgs.org/r.html) from his [**R Packages**](http://r-pkgs.had.co.nz) book. You may also want to go directly to the [`tidyverse` style guide](https://style.tidyverse.org) that contains best practices followed by all developers working on the `tidyverse`. (*Useless Random Fact:* While the guide itself was originally an evolution from an older [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml), Google has now adopted the [`tidyverse` style guide](https://style.tidyverse.org) as its own).

### Commenting your git commits

Unless you are a seasoned developer, it may not be obvious why or how to comment a git `commit`. Fortunately, Chris Beams (2014) wrote a very nice post - [**How to Write a Git Commit Message**](https://chris.beams.io/posts/git-commit/) - that provides much needed guidance and advice on the appropriate way to write `commit` messages.
