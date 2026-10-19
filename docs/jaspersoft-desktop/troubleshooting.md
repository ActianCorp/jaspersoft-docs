# When something goes wrong

What to do with the errors you are most likely to meet, and how to find out more about the others.

## An error message

Errors show in a red box at the top of the window. **Show details** opens what the engine or the
server said: for a report, which element or expression is wrong, and why. The details also give
the error's **id**, with a button to copy it: give it to whoever helps you, so they can find the
error in the log.

**The log.** **Help › Show Logs** opens the folder of Jaspersoft Desktop's log,
`jaspersoft-desktop.log` (the start before is kept as `jaspersoft-desktop.previous.log`). It is the
first thing to send when asking for help: it has the details the window does not show, with the
passwords and keys of the addresses it records masked.

## The preview refuses the report

**"Report design not valid"**, followed by what is wrong. The most common:

| Message | What to do |
| --- | --- |
| **Element bottom reaches outside band area** | An element goes below the bottom of its band. Make it shorter, move it up, or make the band taller (select it in the **Outline**, **Height**). The message gives its `y`, its `height` and the band's height. |
| **Field not found : name** | An expression uses a field the report does not have. Check the spelling (fields are case-sensitive: `$F{COUNTRY}` is not `$F{country}`), or add the field in the **Dataset** tab: **Read Fields** adds those the data has. |
| **Parameter not found**, **Variable not found** | The same, for `$P{…}` and `$V{…}`: add it in the **Dataset** tab, or correct the name. |
| **Query parameter not found : name** | The query uses `$P{name}`, and the report has no such parameter. Create the parameter first, then use it in the query. |
| An error in an expression | The expression is not valid Java: a missing quote or parenthesis, a text compared with `==` instead of `.equals(…)`, a number where a text is expected. The details say which expression; the [expression editor](tutorial-parameters.md#2-the-filter) shows it whole. |

## The report is empty, or has fewer records than expected

- **Test the data adapter**: open it and click **Test** (see
  [Working with data adapters](data-adapters.md)).
- **Look at the data**: in the **Dataset** tab, turn on **Show Query Editor** and click **Preview
  Data**: the records the report gets.
- **A filter** may keep none: the **Filter Expression** of the dataset, at the bottom of the
  **Dataset** tab.
- **A parameter** may have a value that matches nothing: the **Parameters** panel of the preview
  shows what the report ran with; **Reset** gives them their default values.
- **When No Data Show**, in the report's **Properties**, decides what an empty report prints: by
  default, nothing at all.

## A database does not connect

- **The driver is missing**: Jaspersoft Desktop includes the drivers of PostgreSQL, MariaDB (and
  MySQL) and HSQLDB. For another database, add its JDBC driver (`.jar`) in **Settings ›
  Libraries**.
- **The URL**: each driver has its own syntax; the driver list of the data adapter fills in an
  example to complete.
- **The network**: the database must be reachable from this computer, through its VPN or proxy if
  there is one. Jaspersoft Desktop uses the proxy settings of the system.

## Texts look different in the PDF, or print as squares

A font missing where the report runs, or one that has no drawing for the characters: see
[Fonts and PDF](fonts-and-pdf.md).

## Lost changes

Jaspersoft Desktop never saves for you, but it keeps copies of your work as you go: **File › Local
History** lists the versions of the report on show, saved or not, and restores any of them (see
[Working with workspaces](workspaces.md)).

## The AI assistant does not answer

- **"The assistant of this window is not set up"**: the assistant inside Jaspersoft Desktop needs a
  model service: **AI assistant…** on the home screen. The MCP server, for Claude, ChatGPT and the
  others, does not make it answer: those you chat with in their own application. See
  [Designing reports with AI](ai-assistant.md).
- **An error from the model service**: an invalid key, no credit left, a model name the service
  does not know. **Test connection**, in the AI settings, says which.

## Jaspersoft Desktop does not start

The home screen says **Jaspersoft Desktop could not start**, with the reason and **Technical
details**. **Try again** starts it again. If it keeps failing, send the log (**Help › Show Logs**,
or the folder the details name) to support.

### On Linux, the window does not open

**The terminal says `The SUID sandbox helper binary was found, but is not configured
correctly`**: the sandbox helper of the folder has no permissions yet. Give it the two commands
of [Installation](installation.md#linux), step 2, then start Jaspersoft Desktop again.

**Nothing is printed, and no window opens**: a Wayland session does not show the window of the
window engine on every system. Jaspersoft Desktop draws it through XWayland, which every
Wayland desktop provides, and does that by itself; an older version, or a session it does not
recognise, needs the platform named:

```bash
./jaspersoft-desktop --ozone-platform=x11
```
