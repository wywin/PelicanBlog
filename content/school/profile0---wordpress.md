Title: Profile0 - Wordpress
Date: 2015-03-12 17:57
Slug: profile0-wordpress
Categories:
Tags: bizlegfoss

###Rationale

Wordpress is a gigantic thing. It powers (at least) 23% of the web. ([http://w3techs.com/technologies/details/cm-wordpress/all/all](http://w3techs.com/technologies/details/cm-wordpress/all/all){target=_blank}) We wanted to dive deeper into what the community looks like that generates such a massively popular piece of software.


It was also one of the suggested ones, so that is also a reason.

###Organizational Details

- Is the subject of your profile a corporate entity?
     - Automattic is the corporate entity
- What type?
     - Incorporated
- When was it founded?
     - May 27, 2003
- By whom?
    - Matt Mullenweg and Mike Little
- Original founder(s) still active?
    - Matt Mullenweg is still active on the project. Mike Little is no longer active on the project.
- Publicly Traded? Since when? Initial Stock Price? Current stock price?
    - Automattic/Wordpress is not publically traded.
- Has the company made any acquisitions? If yes, which companies, and what were their core products?
    - Gravatar - Avatars
    - BuddyPress - Social networking on a blog
    - IntenseDebate - Commenting service
    - Polldaddy - Surveys and polls
    - Blo.gs - Directory of blogs
    - After The Deadline - Spell checker
    - Plinky - Writing prompts
    - Code Garage - Backups and security scanning
    - Simperium and Simplenote - Note taking and data synchronization
    - Poster - Wordpress mobile app
    - Lean Domain Search - Domain name search
    - Cloudup - File-sharing service
    - Longreads - Sharing service for long form posts
    - Scroll Kit - Visual HTML editor
    - Parka - Security scanning
    - Code For the People - Wordpress development firm
    - Source: [http://wptavern.com/a-look-back-at-16-automattic-acquisitions-since-2007](http://wptavern.com/a-look-back-at-16-automattic-acquisitions-since-2007){target=_blank})
- Has the company made any investments in other companies? If yes, which ones.
    - No they have not. They normally just purchase the companies.
- Number of Employees?
    - 306 ([http://automattic.com/about/](http://automattic.com/about/){target=_blank})
- Where is HQ?
    - 132 Hawthorne St, San Francisco, CA 94107 ([https://www.crunchbase.com/organization/automattic](https://www.crunchbase.com/organization/automattic){target=_blank})
- Does it have any other offices or locations?
    - None
- Website?
    - [http://automattic.com/](http://automattic.com/){target=_blank}
- Wikipedia?
    - [https://en.wikipedia.org/wiki/Automattic](https://en.wikipedia.org/wiki/Automattic){target=_blank}
- Does your organization file any annual reports? Please include links to any relevant documents (i.e. 990, Annual Report, Year in Review, etc...)
    - Bi-annual transparency reports: [http://transparency.automattic.com/](http://transparency.automattic.com/){target=_blank}

###Communications

- Does your subject participate in social media? If yes, please list a URL for each account, and reach within that community. (i.e. Twitter: @RedHatNews - 61.9K Followers.
    - Twitter: @wordpress - 442K followers
- What communication channels does your subject use to reach their public? Briefly describe and include a URL for each.
    - Users of the SaaS product can get notifications and other info on their landing pages. Users of their own installations can get similar notifications.
    -  The Twitter handle mentioned above appears to be more or less a release log.
- Does your subject organize or participate in any conferences? If so, list them here, and provide links to any relevant sessions, keynotes, or content.
    - Wordcamp - first organized by Matt Mullenweg, but numerous spinoffs have been established. [http://central.wordcamp.org/about/](http://central.wordcamp.org/about/){target=_blank}
    -  There’s a conference aggregator named Lanyrd that has a Wordpress tag: [http://lanyrd.com/topics/wordpress/](http://lanyrd.com/topics/wordpress/){target=_blank}

###Community Architecture

Your subject likely runs or contributes to one or more Open Source products or projects. Choose one (or more) of these and answer the following questions:

- If applicable, list and provide links to:
    - The project's IRC Channel
        - [http://codex.wordpress.org/IRC](http://codex.wordpress.org/IRC){target=_blank}
    - Source Code repository
        - [https://core.svn.wordpress.org/trunk/](https://core.svn.wordpress.org/trunk/){target=_blank}
        - [https://github.com/WordPress/WordPress](https://github.com/WordPress/WordPress){target=_blank}
    - Mail list archive
        - [http://codex.wordpress.org/Mailing_Lists](http://codex.wordpress.org/Mailing_Lists){target=_blank}
    - Documentation
        - [http://codex.wordpress.org/](http://codex.wordpress.org/){target=_blank}
    - Other communication channels
        - They are currently evaluating Slack: [https://make.wordpress.org/chat/](https://make.wordpress.org/chat/){target=_blank}
    - Project Website and/or Blog
        - [https://wordpress.org/news/](https://wordpress.org/news/){target=_blank}
        - [https://wordpress.org/](https://wordpress.org/){target=_blank}
- Describe the software project, its purpose and goals.
    - Wordpress is a blogging platform and CMS. “...the mission of the WordPress open source project: to democratize publishing through Open Source, GPL software.” ([http://codex.wordpress.org/WordPress_Policies](http://codex.wordpress.org/WordPress_Policies){target=_blank})
- Give brief history of the project. When was the Initial Commit? The latest commit?
    - First commit: Tue Apr 1 06:17:43 2003 +0000
    - Probably in the last 24 hours.
- Who approves patches? How many people?
    - It appears that the people who approve patches and those who have commit access are the same group.
- Who has commit access, or has had patches accepted? How many total?
    - There are 42 people in the log of the SVN, so most likely a number smaller than 42 (assuming some people have since retired from contributing).
- Has there been any turnover in the Core Team? (i.e. has the top 20% of contributors stayed the same over time? If not, how has it changed?)
    - There is a list of “Developer Emeriti”, comprised of 10 people. ([https://wordpress.org/about/](https://wordpress.org/about/){target=_blank})
- Does the project have a BDFL, or Lead Developer? (BDFL == Benevolent Dictator for Life)
    - Lead Developers: ([https://wordpress.org/about/](https://wordpress.org/about/){target=_blank})
       - Helen Hou-Sandí
       - Dion Hulse
       - Mark Jaquith
       - Matt Mullenweg
       - Andrew Nacin
       - Andrew Ozz
-  Are the front and back end developers the same people? What is the proportion of each?
    - There are 4 people listed as “design”, so we will call them front end devs for our purposes. Discarding the non-differentiated “contributing developers”, that leaves a 4/6 split for frontend/backend.
- What have been some of the major bugs/problems/issues that have arisen during development? Who is responsible for quality control and bug repair?
    - A vast majority of Wordpress vulns are a result of third-party plugins, and as such, do not fall under the umbrella of the core project.
       - No major bugs / vulns in core Wordpress were highly publicized.
- How is the project's participation trending and why?
    - The project’s number of contributors is difficult to gauge accurately - because of the architecture of the community, a large number of contributions via patches get “filtered” through a smaller number of people. As such, the number of contributors has remained roughly the same over time. ([https://www.openhub.net/p/wordpress](https://www.openhub.net/p/wordpress){target=_blank})
- In your opinion, does the project pass "The Raptor Test?" (i.e. Would the project survive if the BDFL, or most active contributor were eaten by a Velociraptor?) Why or why not?
    - Yes, because there are numerous people with access to the main repo.
- In your opinion, would the project survive if the core team, or most active 20% of contributors, were hit by a bus? Why or why not?
    - Maybe not - the access to the main repo seems limited at best, and consequently the most active are the ones who have access.
- Does the project have an official "on-boarding" process in place? (new contributor guides, quickstarts, communication leads who focus specifically on newbies, etc...)
    - There is a Contributor Handbook, but it’s in a very rough state: [https://make.wordpress.org/core/handbook/](https://make.wordpress.org/core/handbook/){target=_blank}
- Does the project have Documentation available? Is it extensive? Does it include code examples?
    - User documentation is at: [http://codex.wordpress.org/](http://codex.wordpress.org/){target=_blank}
    -  Code documentation is at: [https://developer.wordpress.org/reference/](https://developer.wordpress.org/reference/){target=_blank}
   3. Both sets of documentation are extensive.
- If you were going to contribute to this project, but ran into trouble or hit blockers, who would you contact, and how?
    - Asking in the Slack most likely, but it appears to be invite only / requires approval before accounts can be created.
- Based on these answers, how would you describe the decision making structure/process of this group? Is it hierarchical, consensus building, ruled by a small group, barely contained chaos, or ruled by a single or pair of individuals?
    - It’s a small group - one can only make changes with discrete patch files, not pull requests. Patches are submitted to the bug tracker ([https://core.trac.wordpress.org/](https://core.trac.wordpress.org/){target=_blank}) and assessed / merged from there by core devs.
- Is this the kind of structure you would enjoy working in? Why, or why not?
    - While the strict structure resulted in a very robust and very stable core product, it feels difficult to contribute. It also feels a little too reliant on a small group of people.
Technology/Product (Section adapted from EFF Worksheet)
- Who invented, created, or sponsored the technology?
    - Matt Mullenweg and Mike Little founded Automattic Inc. to (initially) work on Wordpress.
- What was the technology designed to do? How was it used?
    - “...the mission of the WordPress open source project: to democratize publishing through Open Source, GPL software.” ([http://codex.wordpress.org/WordPress_Policies](http://codex.wordpress.org/WordPress_Policies){target=_blank})
    -  It is a browser based CMS / blogging platform.
- Who would benefit from using this technology?
    - Anyone who wants to publish content, written or otherwise, easily online.
- What kinds of companies or organizations (stakeholders) might have been concerned about the development of this technology? Why?
    - Developers of other (commercial) blogging platforms, governments wishing to squelch dissent, and people who generally dislike blogs for whatever reason.
- Did an aspect of copyright law play a role in controversies about the technology? How?
    - A case of a fraudulent DMCA (fairly recent as well!): [http://www.theverge.com/2015/3/9/8175491/wordpress-automattic-wins-dmca-takedown-straight-pride-uk-case](http://www.theverge.com/2015/3/9/8175491/wordpress-automattic-wins-dmca-takedown-straight-pride-uk-case){target=_blank}