title: "Backwards-compatible Short URL conversion of Mediawiki"
date: 2013-07-14 14:27
comments: false
categories: mediawiki apache mod_rewrite

Further adventures in mod_rewrite town! This time I had to convert a Mediawiki install to Short URLs while maintaining backwards compatability. Let's see how it went!

<!-- more -->

First, if you're like me, you don't plan ahead very much when doing software installs. A Mediawiki site I help with has been running for some time, and several links exist pointing to old, ugly URLs like "www.example.com/wiki/index.php/Main_Page". However, the decision makers wanted the links to lose the "index.php" in the URL!

That's easy enough to do. The [Mediawiki meta-wiki](https://www.mediawiki.org/wiki/Manual:Short_URL) has a great write up on the topic. They also link to [this handy wizard](http://shorturls.redwerks.org/), which I used.

You should come up with something like this:

    RewriteRule ^/?wiki(/.*)?$ %{DOCUMENT_ROOT}/w/index.php [QSA,L]
	RewriteRule ^/?$ %{DOCUMENT_ROOT}/w/index.php [QSA,L]
	
	RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} !-f
	RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} !-d
	RewriteRule ^/?w/images/thumb/[0-9a-f]/[0-9a-f][0-9a-f]/([^/]+)/([0-9]+)px-.*$ %{DOCUMENT_ROOT}/w/thumb.php?f=$1&width=$2 [L,QSA,B]

	RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} !-f
	RewriteCond %{DOCUMENT_ROOT}%{REQUEST_URI} !-d
	RewriteRule ^/?w/images/thumb/archive/[0-9a-f]/[0-9a-f][0-9a-f]/([^/]+)/([0-9]+)px-.*$ %{DOCUMENT_ROOT}/w/thumb.php?f=$1&width=$2&archived=1 [L,QSA,B]

That's all great, but old links won't work anymore! Let's fix that by adding this before all the other new RewriteRules:

    RewriteRule ^/?wiki/index.php(/(.*))?$ /wiki/$2 [R=301,L]

Now you should have pretty URLs, and the old-style links should redirect to the new pretty ones too!