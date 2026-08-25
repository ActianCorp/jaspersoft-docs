---
title: The queryExecutor Service
description: "In addition to running reports, JasperReports Server exposes queries that you can run through the restv2/queryExecutor service. The only resource that supports these queries is a domain."
---

# The queryExecutor Service

In addition to running reports, JasperReports Server exposes queries that you can run through the rest_v2/queryExecutor service. The only resource that supports these queries is a domain.

Use the GET method to specify the query string in the request as an argument.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>GET</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/queryExecutor/</span>path/to/Domain/?q=&lt;query&gt;</span></p></td>
</tr>
<tr>
<td><p>Argument</p></td>
<td><p>Type/Value</p></td>
<td colspan="2"><p>Description</p></td>
</tr>
<tr>
<td><p><span>q</span></p></td>
<td><p>Required String</p></td>
<td colspan="2"><p>The query string is a special format that references the fields and measures exposed by the domain. To write this query, you must know the Domain schema that is not available through the REST services. See below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p>
<p><span>Accept-Language: &lt;locale&gt;, &lt;relativeQualityFactor&gt;;</span> for example, <span>en_US, q=0.8;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains the data that is the result of the query. See the format of the data below.</p></td>
<td><p>404 Not Found - When the specified domain does not exist.</p></td>
</tr>
</tbody>
</table>

If the query is too large to fit in the argument in the URL, use the POST method to send it as request content:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><p>Method</p></th>
<th colspan="3"><p>URL</p></th>
</tr>
&#10;<tr>
<td><p>POST</p></td>
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/<span>rest_v2/queryExecutor/</span>path/to/Domain/</span></p></td>
</tr>
<tr>
<td colspan="2"><p>Content-Type</p></td>
<td colspan="2"><p>Content</p></td>
</tr>
<tr>
<td colspan="2"><p><span>application/xml</span></p></td>
<td colspan="2"><p>The query string is a special format that references the fields and measures exposed by the domain. To write this query, you must know the domain schema that is not available through the REST services. See below.</p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>accept: application/xml</span> (default)</p>
<p><span>accept: application/json</span></p>
<p><span>Accept-Language: &lt;locale&gt;, &lt;relativeQualityFactor&gt;;</span> for example, <span>en_US, q=0.8;</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body contains the data that is the result of the query. See the format of the data below.</p></td>
<td><p>404 Not Found - When the specified domain does not exist.</p></td>
</tr>
</tbody>
</table>

The following example shows the format of a query in XML:

``` xml
<query>
  <queryFields>
    <queryField id="expense_join_store.ej_store_store_city"/>
    <queryField id="expense_join_store.ej_store_store_country"/>
    <queryField id="expense_join_store.ej_store_store_name"/>
    <queryField id="expense_join_store.ej_store_store_state"/>
    <queryField id="expense_join_store.ej_store_store_street_address"/>
  </queryFields>
  <queryFilterString>expense_join_store.ej_store_store_country == 'USA'
                     and expense_join_store.ej_store_store_state == 'CA'
  </queryFilterString>
</query>
```

The following sample shows the result of the above query. To optimize the size of the response, rows are presented as sets of values without the column names repeated for each row. The column IDs appear at the top of the result, as shown in the following example. As with the query, the result requires knowledge of the Domain schema to identify the human-readable column names.

``` xml
<queryResult>
  <names>
    <name>expense_join_account.ej_account_account_description</name>
    <name>expense_join_account.ej_expense_fact_account_id</name>
    <name>expense_join_account.ej_account_account_parent</name>
    <name>expense_join_account.ej_account_account_rollup</name>
    <name>expense_join_account.ej_account_account_type</name>
    <name>expense_join_account.ej_account_Custom_Members</name>
    <name>expense_join.ej_expense_fact_amount</name>
    <name>expense_join_store.ej_store_store_type</name>
    <name>expense_join_store.ej_store_store_street_address</name>
    <name>expense_join_store.ej_store_store_city</name>
    <name>expense_join_store.ej_store_store_state</name>
    <name>expense_join_store.ej_store_store_postal_code</name>
    <name>expense_join_store.sample_time</name>
  </names>

  <values>
    <row>
      <value xsi:type="xs:string">Marketing</value>
      <value xsi:type="xs:int">4300</value>
      <value xsi:type="xs:int">4000</value>
      <value xsi:type="xs:string">+</value>
      <value xsi:type="xs:string">Expense</value>
      <value xsi:nil="true"/>
      <value xsi:type="xs:double">1884.0000</value>
      <value xsi:type="xs:dateTime">1997-01-01T04:05:06+02:00</value>
      <value xsi:type="xs:string">HeadQuarters</value>
      <value xsi:type="xs:string">1 Alameda Way</value>
      <value xsi:type="xs:string">Alameda</value>
      <value xsi:type="xs:string">CA</value>
      <value xsi:type="xs:int">94502</value>
      <value xsi:type="xs:string">USA</value>
      <value xsi:type="xs:time">04:05:06+02:00</value>
    </row>
     ...
  </values>
</queryResult>
```

!!! note

    Both date-only and timestamp fields are given in the ISO date-time format such as 1997-01-01T04:05:06+02:00.

    For database columns that store a time and date that includes a time zone, such as "timestamp with time zone" in PostgreSQL, the result is not guaranteed to be in the same time zone as stored in the database. These dates and times are converted to the server's time zone.
