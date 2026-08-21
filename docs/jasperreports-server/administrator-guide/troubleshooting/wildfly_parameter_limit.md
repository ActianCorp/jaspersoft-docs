---
title: Maximum Parameter Size in Wildfly
description: "On Wildfly, if a report sends more than 1,000 parameters, you may see a 500 error, for example:"
---

# Maximum Parameter Size in Wildfly

On Wildfly, if a report sends more than 1,000 parameters, you may see a 500 error, for example:

``` text
"The number of parameters exceeded the maximum of 1000"
```

To allow more than 1,000 parameters, increase `max-parameters`. To do this, open the file `<wildfly-home>/wildfly/standalone/configuration/standalone.xml` and add or change the `max-parameters` attribute of the `http-listener` property. For example:

``` xml
<http-listener name="default" socket-binding="http" max-header-size="974247881"
    max-post-size="974247881" max-parameters="5000"/>
```
