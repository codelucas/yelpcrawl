YelpCrawl: Exhaustive Yelp! Scraper
===================================

Example usage for `yelp`_ extraction.

Extract all restaurant data from a specific zipcode.

::

    $ python2.7 crawler.py -z 98029

    ===== Attempting extraction for zipcode < 98029 >=====
    
    title: Issaquah Coffee Company
    categories: Coffee & Tea
    rating: 4.0 star rating
    ...


Extract all restaurant data from America (all American zipcodes).

::

    $ python2.7 crawler.py

    **We are attempting to extract all zipcodes in Amerrica!**

    ===== Attempting extraction for zipcode < 35004 >=====

    title: Brasher Sam Tire &amp; Auto Service Inc
    categories: Tires
    rating: 5.0 star rating
    ...


Installation:
-------------

::

    $ git clone https://github.com/codelucas/yelpcrawl
    $ cd yelpcrawl
    $ pip install -r requirements.txt

And now you can begin!

::

    $ python2.7 crawler.py -z 98029

Feel free to send in pull requests. We need some test cases please :)

This code was written when the two of us were still relatively new at python 
so excuse the shittyness. This was open sourced just for keepsake, it's nothing
fancy and there are definitely better scraping solutions out there.

We used slower parsers like `beautifulsoup`_ and no multithreading
because `yelp`_ would've rate limited us anyways :)

By: `Lucas`_, `Mathew`_

.. _`yelp`: http://www.yelp.com
.. _`beautifulsoup`: http://www.crummy.com/software/BeautifulSoup/
.. _`Lucas`: http://codelucas.com
.. _`Mathew`: https://www.facebook.com/matsprehn
