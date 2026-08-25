---
title: Installation Error with Windows Path
description: "If the path of the war archive exceeds the maximum length allowed by Windows, you get an error message like the one shown below."
---

# Installation Error with Windows Path

If the path of the war archive exceeds the maximum length allowed by Windows, you get an error message like the one shown below.

``` yaml
java.io.IOException: Cannot run program "C:\Program
Files\Java\jdkx.x.x_xx\jre\bin\java.exe": CreateProcess error=206, The filename
or extension is too long
        at java.lang.ProcessBuilder.start(ProcessBuilder.java:460)
        at java.lang.Runtime.exec(Runtime.java:593)
```

You need to move the war archive to reduce the path length. More information is available from Microsoft at:<br>
<http://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx>.
