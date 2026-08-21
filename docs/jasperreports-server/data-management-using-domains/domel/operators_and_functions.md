---
title: Operators and Functions
description: "DomEL provides the following operators, listed in order of precedence. Operators higher in this list are evaluated before operators lower in the list:"
---

# Operators and Functions

DomEL provides the following operators, listed in order of precedence. Operators higher in this list are evaluated before operators lower in the list:

<table>
<thead>
<tr>
<th><p>Operator</p></th>
<th><p>Syntax</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>multiply, divide</p></td>
<td><p><code>i * j / k</code></p></td>
<td><p>Arithmetic operators for numeric types only.</p></td>
</tr>
<tr>
<td><p>percent</p></td>
<td><p><code>i % j </code></p></td>
<td><p>Calculates i as a percent of j; numeric types only.</p></td>
</tr>
<tr>
<td><p>add, subtract</p></td>
<td><p><code>i + j - k</code></p></td>
<td><p>Arithmetic operators for numeric types only.</p></td>
</tr>
<tr>
<td><p>equal</p></td>
<td><p><code>i == j</code></p></td>
<td rowspan="2"><p>Comparison operators for string, numeric, and date types.</p></td>
</tr>
<tr>
<td><p>not equal</p></td>
<td><p><code>i != j</code></p></td>
</tr>
<tr>
<td><p>less than</p></td>
<td><p><code>i &lt; j</code></p></td>
<td rowspan="4"><p>Comparison operators for numeric and date types only.</p></td>
</tr>
<tr>
<td><p>less than or equal</p></td>
<td><p><code>i &lt;= j</code></p></td>
</tr>
<tr>
<td><p>greater than</p></td>
<td><p><code>i &gt; j</code></p></td>
</tr>
<tr>
<td><p>greater than or equal</p></td>
<td><p><code>i &gt;= j</code></p></td>
</tr>
<tr>
<td><p>IN <em>set</em></p></td>
<td><p><code>i IN ('apples','oranges')</code></p></td>
<td><p>Sets can be of any type.</p></td>
</tr>
<tr>
<td><p>IN <em>range</em></p></td>
<td><p><code>i IN (j:k)</code></p></td>
<td><p>Ranges must be numeric or date types.</p></td>
</tr>
<tr>
<td><p>NOT</p></td>
<td><p><code>NOT( i )</code></p></td>
<td rowspan="3"><p>Boolean operators. Parentheses are required for <code>NOT</code>.</p></td>
</tr>
<tr>
<td><p>AND</p></td>
<td><p><code>i AND j AND k</code></p></td>
</tr>
<tr>
<td><p>OR</p></td>
<td><p><code>i OR j OR k</code></p></td>
</tr>
<tr>
<td><p>parentheses</p></td>
<td><p><code>()</code></p></td>
<td><p>Used for grouping.</p></td>
</tr>
</tbody>
</table>

DomEL also defines the following operations as functions.

<table>
<thead>
<tr>
<th><p>Function</p></th>
<th><p>Syntax</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>startsWith</p></td>
<td><p><code>startsWith(i, 'prefix')</code></p></td>
<td rowspan="3"><p>Comparison operators for strings.</p></td>
</tr>
<tr>
<td><p>endsWith</p></td>
<td><p><code>endsWith(j, 'suffix')</code></p></td>
</tr>
<tr>
<td><p>contains</p></td>
<td><p><code>contains(k, 'substring')</code></p></td>
</tr>
<tr>
<td><p>concat</p></td>
<td><p><code>concat(i, ' and ', j, ...)</code></p></td>
<td><p>Returns the string of all parameters concatenated.</p></td>
</tr>
</tbody>
</table>

Additional functions are supported in Ad Hoc views.
