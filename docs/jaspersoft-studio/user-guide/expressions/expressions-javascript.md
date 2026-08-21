---
title: Using JavaScript as a Language for Expressions
description: JavaScript is a popular scripting language with a syntax very similar to Java and Groovy. JavaScript has a set of functions and object methods that in some cases differ from Java and Groovy. For...
---

# Using JavaScript as a Language for Expressions

JavaScript is a popular scripting language with a syntax very similar to Java and Groovy. JavaScript has a set of functions and object methods that in some cases differ from Java and Groovy. For example, the method `String.startsWith(...)` does not exist in JavaScript. You can still use Java objects in JavaScript. An example is:

`(new java.lang.String("test")).startsWith("t")`

This is a valid JavaScript expression creating a Java object (in this case a `java.lang.String`) and using its methods.

JavaScript is the best choice for users who have no knowledge of other languages. The other significant advantage of JavaScript is that it is not interpreted at run time, but instead generates pure Java byte-code. As a result, it offers almost the same performance as Java itself.

!!! note

    Rhino JavaScript engine has been removed from JasperReports Server. With the removal of Rhino JS, reports created using JavaScript will not function unless you add Rhino JS back to your deployment. This can be done by stopping the web server, downloading version 1.7.14 which at the time of writing is not known to have any CVEs. This file can be replaced into the WEB-INF/lib folder, and reports that rely on JavaScript will again be functional.
