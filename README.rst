YelpCrawl: Exhaustive Yelp! Scraper
===================================

Example usage for `yelp`_ extraction.

Extract all restaurant data from a specific zipcode.

.. code-block:: pycon

    >>> python2.7 crawler.py -z 98029

    ===== Attempting extraction for zipcode < 98029 >=====
    
    title: Issaquah Coffee Company
    categories: Coffee & Tea
    rating: 4.0 star rating
    ...


Extract all restaurant data from America (all America zipcodes).

.. code-block:: pycon

    >>> python2.7 crawler.py

    **We are attempting to extract all zipcodes in Amerrica!**

    ===== Attempting extraction for zipcode < 35004 >=====

    title: Brasher Sam Tire &amp; Auto Service Inc
    categories: Tires
    rating: 5.0 star rating
    ...


Installation:
-------------

::
    git clone https://github.com/codelucas/yelpcrawl
    cd yelpcrawl

And now you can begin!

::
    >>> python2.7 crawler.py -z 98029


This code was written when the two of us were still relatively new at python 
so excuse the shittyness. This was open sourced just for keepsake, it's nothing
fancy and there are definitely better scraping solutions out there.

We used slower parsers like `beautifulsoup`_ and no multithreading
because `yelp`_ would have probably rate limited us anyways :p

- Lucas, Mathew

.. _`yelp`: http://www.yelp.com
.. _`beautifulsoup`: http://www.crummy.com/software/BeautifulSoup/
