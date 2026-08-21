---
title: Server Requests Rejected After csrfguard Library Upgrade
description: "With the csrfguard library upgraded from version 3.1.0 to 4.3.0, it was observed that all server requests were rejected."
---

# Server Requests Rejected After csrfguard Library Upgrade

With the csrfguard library upgraded from version 3.1.0 to 4.3.0, it was observed that all server requests were rejected.

This is because in the original OWASP library version 4.3.0, the `org.owasp.csrfguard.TokenPerPage` property is set to `true` by default and cannot be set to `false`. The said library does not support it for better security. Having this property set to `true` will create new tokens per API URL within a valid session time.

The JavaScriptServlet API now returns a unique CSRF token for each visited API URL (page). These per-page tokens are generated on the first visit to that URL and remain valid for the entire session. If a page has not been visited, the master token can be used to request a new page-specific token. This per-page token behavior is standard for the library.

!!! note

    Setting `org.owasp.csrfguard.TokenPerPage` to `false` is **not** a supported configuration. Doing so can disrupt the proper functioning of different JasperReports Server workflows.

    Support or fixes for issues encountered when this property is set to `false` shall **not** be provided.
