---
title: Introduction to Dimensional Modeling
description: Dimensional modeling is a way of organizing information so that data is better suited to certain types of queries. Such queries often arise during statistical analysis of numerical trends and...
---

# Introduction to Dimensional Modeling

Dimensional modeling is a way of organizing information so that data is better suited to certain types of queries. Such queries often arise during statistical analysis of numerical trends and patterns. In dimensional modeling, cubes, dimensions, and measures constitute a logical schema that describes your business.

Dimensional modeling typically differentiates analysis from other types of reporting:

- Transactional reports typically display data in a fixed format. The structure is always the same, but the quantitative and qualitative information for each time period or subject of study differ.
- Analysis typically provides access to large amounts of data aggregated with respect to different variables. Each query may produce a view with a different structure. Analysis is generally interactive: it answers questions, helps you find trends and outliers in your data, and get a deeper understanding of your data.

Another way analytical reporting differs from traditional reporting is its emphasis on numerical data. While an event can be described qualitatively (Joe and Kris were married on June 15 in the park by a minister), these details could be better described if you want to summarize and examine information about a large number of marriages. In this case, you would be better off with data organized dimensionally.

Consider the five basic questions journalists ask: who, what, when, where, and why?

These questions are helpful in organizing data. Defining a standardized way to describe groups of events makes it easier to pose certain queries. For example:

- How many marriages occurred in parks in June versus in December?
- What percentage of marriages performed by ministers occurred in a church?

If the data is organized dimensionally, we can answer such questions with a single query, rather than by examining each qualitative wedding announcement in the paper.
