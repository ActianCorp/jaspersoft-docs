---
title: The jobs calendars Service
description: "The scheduler allows a job to be defined with a list of excluded days or times when you do not want the job to run. For example, if you have a report scheduled to run every business day, you may not..."
---

# The jobs calendars Service

The scheduler allows a job to be defined with a list of excluded days or times when you do not want the job to run. For example, if you have a report scheduled to run every business day, you may not want to run it on holidays. The list of excluded days and times is called a calendar, and a calendar may be defined as a list of annual dates, a weekly or monthly pattern, or a cron expression.

The rest_v2/jobs/calendars service defines any number of exclusion calendars that are stored in the repository. When scheduling a report, reference the name of the calendar to exclude, and the scheduler automatically calculates the correct days to trigger the report.

The scheduler also allows you to modify an exclusion calendar and update all the report jobs that used it. Therefore, you can update the calendar of holidays every year and not need to modify any report jobs.

This chapter includes the following sections:

-   [Creating an Exclusion Calendar](#creating-an-exclusion-calendar)
-   [Listing All Calendar Names](#listing-all-calendar-names)
-   [Viewing an Exclusion Calendar](#viewing-an-exclusion-calendar)
-   [Updating an Exclusion Calendar](#updating-an-exclusion-calendar)
-   [Deleting an Exclusion Calendar](#deleting-an-exclusion-calendar)
-   [Error Messages](#error-messages)

## Creating an Exclusion Calendar

The PUT method creates a named exclusion calendar that you can use when scheduling reports. Specify a unique name for the calendar in the URL. The body of the request determines the type of the calendar, as shown in the examples below the table.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml<br />
application/json</span></p></td>
<td colspan="2"><p>A well-formed XML or JSON calendar descriptor (see examples below).</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The calendar is created, and the body of the response contains the calendar definition, similar to the one that was sent.</p></td>
<td><p>400 Bad Request–When the calendar name exists or the descriptor is missing a parameter (the error message describes the missing parameter).</p></td>
</tr>
</tbody>
</table>

The following examples show the types of exclusion calendars that you can add to the scheduler:

-   Annual calendar: A list of days that you want to exclude every year.

    JSON:

    ``` json
    {
        "calendarType":"annual",
        "description":"Annual calendar description",
        "excludeDays": [ "2021-03-20", "2021-03-21", "2021-03-22"],
        "timeZone":"GMT+03:00"
    }
    ```

    XML:

    ``` xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <reportJobCalendar>
      <calendarType>annual</calendarType>
      <description>Annual calendar description</description>
      <timeZone>GMT+03:00</timeZone>
        <excludeDays>
        <excludeDay>2021-03-20</excludeDay>
        <excludeDay>2021-03-21</excludeDay>
        <excludeDay>2021-03-22</excludeDay>
      </excludeDays>
    </reportJobCalendar>
    ```

-   Cron calendar: Defines the days and times to exclude as a cron expression.

    JSON:

    ``` json
    {
        "calendarType":"cron",
        "description":"Cron calendar description",
        "cronExpression":"0 30 10-13 ? * WED,FRI",
        "timeZone":"GMT+03:00"
    }
    ```

    XML:

    ``` xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <reportJobCalendar>
      <calendarType>cron</calendarType>
      <description>Cron calendar description</description>
      <cronExpression>0 30 10-13 ? * WED,FRI</cronExpression>
      <timeZone>GMT+03:00</timeZone>
    </reportJobCalendar>
    ```

-   Daily calendar: Defines a time range to exclude every day.

    JSON:

    ``` json
    {
        "calendarType":"daily",
        "description":"Daily calendar description",
        "invertTimeRange":false,
        "rangeEndingCalendar":"2020-20T14:44:37.353+03:00",
        "rangeStartingCalendar":"2020-03-20T14:43:37.353+03:00",
        "timeZone":"GMT+03:00"
    }
    ```

    XML:

    ``` xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <reportJobCalendar>
      <calendarType>daily</calendarType>
      <description>Daily calendar description</description>
      <invertTimeRange>false</invertTimeRange>
      <rangeEndingCalendar>2020-03-20T14:44:37.353+03:00</rangeEndingCalendar>
      <rangeStartingCalendar>2020-03-20T14:43:37.353+03:00</rangeStartingCalendar>
      <timeZone>GMT+03:00</timeZone>
    </reportJobCalendar>
    ```

-   Holiday calendar: Defines a set of days to exclude that can be updated every year.

    JSON:

    ``` json
    {
        "calendarType":"holiday",
        "description":"Holiday calendar (observed)",
        "excludeDays": [
            "2020-01-01",
            "2020-01-20",
            "2020-02-17",
            "2020-05-25",
            "2020-07-03",
            "2020-09-07",
            "2020-10-12",
            "2020-11-11",
            "2020-11-26",
            "2020-12-25"
        ],
        "timeZone":"GMT+03:00"
    }
    ```

    XML:

    ``` xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <reportJobCalendar>
      <calendarType>holiday</calendarType>
      <description>Holiday calendar (observed)</description>
      <excludeDays>
        <excludeDay>2021-03-20</excludeDay>
        <excludeDay>2020-01-01</excludeDay>
        <excludeDay>2020-01-20</excludeDay>
        <excludeDay>2020-02-17</excludeDay>
        <excludeDay>2020-05-25</excludeDay>
        <excludeDay>2020-07-03</excludeDay>
        <excludeDay>2020-09-07</excludeDay>
        <excludeDay>2020-10-12</excludeDay>
        <excludeDay>2020-11-11</excludeDay>
        <excludeDay>2020-11-26</excludeDay>
        <excludeDay>2020-12-25</excludeDay>
      </excludeDays>
      <timeZone>GMT+03:00</timeZone>
    </reportJobCalendar>
    ```

-   Weekly calendar: Defines a set of days to be excluded each week.

    JSON:

    ``` json
    {
        "calendarType": "weekly",
        "description": "Weekly calendar description",
        "excludeDaysFlags": [
            true,  /*Sunday*/
            false, /*Monday*/
            false, /*Tuesday*/
            false, /*Wednesday*/
            false, /*Thursday*/
            false, /*Friday*/
            false  /*Saturday*/
        ],
        "timeZone": "GMT+03:00"
    }
    ```

-   Monthly calendar: Defines the dates to exclude every month.

JSON:

``` json
{
    "calendarType":"monthly",
    "description":"Monthly calendar description",
    "excludeDaysFlags": [
        true,  /* 1*/
        false, /* 2*/
        false, /* 3*/
        false, /* 4*/
        false, /* 5*/
        false, /* 6*/
        false, /* 7*/
        false, /* 8*/
        false, /* 9*/
        false, /*10*/
        false, /*11*/
        false, /*12*/
        false, /*13*/
        false, /*14*/
        false, /*15*/
        false, /*16*/
        false, /*17*/
        false, /*18*/
        false, /*19*/
        false, /*20*/
        false, /*21*/
        false, /*22*/
        false, /*23*/
        false, /*24*/
        false, /*25*/
        false, /*26*/
        false, /*27*/
        false, /*28*/
        false, /*29*/
        false, /*30*/
        false  /*31*/
    ],
    "timeZone":"GMT+03:00"
}
```

## Listing All Calendar Names

The following method returns the list of all calendar names that were added to the scheduler.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars/</span>?&lt;argument&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>calendar<br />
Type</span></p></td>
<td><p>optional string</p></td>
<td colspan="2"><p>A type of calendar to return: <span>annual</span>, <span>cron</span>, <span>daily</span>, <span>holiday</span>, <span>monthly</span>, or <span>weekly</span>. You may specify only one <span>calendarType</span> parameter. When <span>calendarType</span> is not specified, all calendars names are returned. If <span>calendarType</span> has an invalid value, an empty collection is returned.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – Body contains a list of calendar names.</p></td>
<td><p>401 Unauthorized</p></td>
</tr>
</tbody>
</table>

The list of calendar names in the result has the following format in XML:

``` xml
<calendarNameList>
  <calendarName>name1</calendarName>
  <calendarName>name2</calendarName>
</calendarNameList>
```

## Viewing an Exclusion Calendar

The following method takes the name of an exclusion calendar and returns the definition of the calendar:

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The body contains the definition of the requested calendar.</p></td>
<td><p>404 Not Found–When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>

The calendar descriptor in a successful response has the following JSON format:

-   Annual calendar:

    ``` json
    {
        "calendarType": "annual",
        "description": "Annual calendar description",
        "timeZone": "GMT+03:00",
        "excludeDays": [
            "2012-03-20",
            "2012-03-21",
            "2012-03-22"
        ]
    }
    ```

-   Cron calendar:

    ``` json
    {
        "calendarType": "cron",
        "description": "Cron calendar description",
        "timeZone": "GMT+03:00",
        "excludeDays": null,
        "cronExpression": "0 30 10-13 ? * WED,FRI"
    }
    ```

-   Daily calendar:

    ``` json
    {
        "calendarType": "daily",
        "description": "Daily calendar description",
        "timeZone": "GMT+03:00",
        "excludeDays": null,
        "rangeStartingCalendar": 1332243817353,
        "rangeEndingCalendar": 1332243877353,
        "invertTimeRange": false
    }
    ```

-   Holiday calendar:

    ``` json
    {
        "calendarType": "holiday",
        "description": "Holiday calendar (observed)",
        "timeZone": "GMT+03:00",
        "excludeDays": [
            "2020-01-01",
            "2020-01-20",
            "2020-02-17",
            "2020-05-25",
            "2020-07-03",
            "2020-09-07",
            "2020-10-12",
            "2020-11-11",
            "2020-11-26",
            "2020-12-25"
        ]
    }
    ```

-   Weekly calendar (day flags are Sunday to Saturday):

    ``` json
    {
        "calendarType": "weekly",
        "description": "Weekly calendar description",
        "excludeDays": null,
        "excludeDaysFlags": [
            true,
            false,
            false,
            false,
            false,
            false,
            false
        ],
        "timeZone":"GMT+03:00"
    }
    ```

-   Monthly calendar (day flags are dates from 1 to 31):

``` json
{
    "calendarType":"monthly",
    "description":"Monthly calendar description",
    "excludeDaysFlags": [
        true,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false
    ],
    "timeZone":"GMT+03:00"
}
```

## Updating an Exclusion Calendar

Use the PUT method to update a calendar that exists, with the option to update all the jobs that use it.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>PUT</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;?&lt;args&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>replace?</span></p></td>
<td><p>true</p></td>
<td colspan="2"><p>Set to true to modify an existing calendar with the given name. When this argument is omitted or false, an error is returned (see below).</p></td>
</tr>
<tr>
<td><p><span>update<br />
Triggers?</span></p></td>
<td><p>true / false</p></td>
<td colspan="2"><p>Whether to update existing triggers that reference this calendar. When triggers are updated, the new calendar is in effect on existing scheduled reports.</p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml<br />
application/json</span></p></td>
<td colspan="2"><p>A well-formed XML or JSON calendar descriptor. See <a href="#creating-an-exclusion-calendar">“Creating an Exclusion Calendar” on page 1</a> for examples of each type of calendar. You can specify any type of exclusion calendar such as weekly, monthly, or cron, regardless of the current type.</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The calendar is updated, and the body of the response contains the new calendar definition, similar to the one that was sent.</p></td>
<td><p>400 Bad Request–When the <code>replace</code> parameter is false or omitted, or the calendar definition is not valid.</p>
<p>404 Not Found–When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>

For example, you can make the following request to replace the calendar named `weeklyCalendar`. Note that the calendar name does not change, and it contains a daily calendar, which is not good naming practice.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Request</p></td>
<td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/
        weeklyCalendar?replace=true&amp;updateTriggers=true
Content-Type=application/json</code></pre></div></td>
</tr>
<tr>
<td><p>Body</p></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;daily&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;test description&quot;</span><span class="fu">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;invertTimeRange&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">,</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;rangeEndingCalendar&quot;</span><span class="fu">:</span><span class="st">&quot;2012-03-20T14:44:37.353+03:00&quot;</span><span class="fu">,</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;rangeStartingCalendar&quot;</span><span class="fu">:</span><span class="st">&quot;2012-03-20T14:43:37.353+03:00&quot;</span><span class="fu">,</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

If the `replace` parameter is false or omitted, the error is as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Response</p></td>
<td><p>400 Bad Request</p></td>
</tr>
<tr>
<td><p>Body</p></td>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;Resource &#39;weeklyCalendar&#39; already exists&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;resource.already.exists&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;weeklyCalendar&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Deleting an Exclusion Calendar

Use the following method to delete a calendar by name.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>DELETE</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/jobs/calendars</span>/&lt;calendarName&gt;/</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The calendar has been deleted.</p></td>
<td><p>404 Not Found–When the specified calendar name does not exist.</p></td>
</tr>
</tbody>
</table>

## Error Messages

When creating or updating a calendar, the error messages can be expected in the following cases.

-   Creating an annual calendar that is missing a mandatory parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/annualCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;annual&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Annual calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.excludeDays&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.excludeDays&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a cron calendar that is missing a mandatory parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/cronCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;cron&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Cron calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.cronExpression&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.cronExpression&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a daily calendar that is missing the mandatory start-range parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/dailyCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;daily&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Daily calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;invertTimeRange&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">,</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;rangeEndingCalendar&quot;</span><span class="fu">:</span><span class="st">&quot;2021-03-20T14:44:37.353+03:00&quot;</span><span class="fu">,</span></span>
    <span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.rangeStartingCalendar&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.rangeStartingCalendar&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a daily calendar that is missing the mandatory end-range parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/dailyCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;daily&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Daily calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;invertTimeRange&quot;</span><span class="fu">:</span><span class="kw">false</span><span class="fu">,</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;rangeStartingCalendar&quot;</span><span class="fu">:</span><span class="st">&quot;2012-03-20T14:43:37.353+03:00&quot;</span><span class="fu">,</span></span>
    <span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.rangeEndingCalendar&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.rangeEndingCalendar&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a holiday calendar that is missing a mandatory parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/holidayCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;holiday&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Holiday calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.excludeDays&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.excludeDays&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a weekly calendar that is missing a mandatory parameter:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Request</p></td>
    <td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/weeklyCalendar
    Content-Type=application/json</code></pre></div></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;weekly&quot;</span><span class="fu">,</span></span>
    <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Weekly calendar description&quot;</span><span class="fu">,</span></span>
    <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
    <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

    Expected Reply:

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <tbody>
    <tr>
    <td><p>Response</p></td>
    <td><p>400 Bad Request</p></td>
    </tr>
    <tr>
    <td><p>Body</p></td>
    <td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
    <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.excludeDaysFlags&#39; not found&quot;</span><span class="fu">,</span></span>
    <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
    <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
    <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
    <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>         <span class="st">&quot;reportJobCalendar.excludeDaysFlags&quot;</span></span>
    <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
    <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
    </tr>
    </tbody>
    </table>

-   Creating a monthly calendar that is missing a mandatory parameter:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Request</p></td>
<td><div class="language-text highlight"><pre><code>PUT http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/rest_v2/jobs/calendars/monthlyCalendar
Content-Type=application/json</code></pre></div></td>
</tr>
<tr>
<td><p>Body</p></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;calendarType&quot;</span><span class="fu">:</span><span class="st">&quot;monthly&quot;</span><span class="fu">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;description&quot;</span><span class="fu">:</span><span class="st">&quot;Monthly calendar description&quot;</span><span class="fu">,</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;timeZone&quot;</span><span class="fu">:</span><span class="st">&quot;GMT+03:00&quot;</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

Expected Reply:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Response</p></td>
<td><p>400 Bad Request</p></td>
</tr>
<tr>
<td><p>Body</p></td>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;message&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory parameter &#39;reportJobCalendar.excludeDaysFlags&#39; not found&quot;</span><span class="fu">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;errorCode&quot;</span><span class="fu">:</span> <span class="st">&quot;mandatory.parameter.error&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;parameters&quot;</span><span class="fu">:</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="ot">[</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>        <span class="st">&quot;reportJobCalendar.excludeDaysFlags&quot;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="ot">]</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
