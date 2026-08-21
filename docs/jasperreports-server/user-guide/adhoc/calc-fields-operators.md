---
title: Operators in Ad Hoc Views
description: "Ad Hoc views support the following operators in calculated fields. Operators are evaluated in the order they are shown in the table:"
---

# Operators in Ad Hoc Views

Ad Hoc views support the following operators in calculated fields. Operators are evaluated in the order they are shown in the table:

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
<td><p>i * j / k</p></td>
<td><p>Arithmetic operators for numeric types only.</p></td>
</tr>
<tr>
<td><p>percent</p></td>
<td><p>i % j</p></td>
<td><p>Calculates i as a percent of j; numeric types only.</p></td>
</tr>
<tr>
<td><p>add, subtract</p></td>
<td><p>i + j - k</p></td>
<td><p>Arithmetic operators for numeric types only.</p></td>
</tr>
<tr>
<td><p>equal</p></td>
<td><p>i == j</p></td>
<td rowspan="2"><p>Comparison operators for string, numeric, and date types.</p></td>
</tr>
<tr>
<td><p>not equal</p></td>
<td><p>i != j</p></td>
</tr>
<tr>
<td><p>less than</p></td>
<td><p>i &lt; j</p></td>
<td rowspan="4"><p>Comparison operators for numeric and date types only.</p></td>
</tr>
<tr>
<td><p>less than or equal</p></td>
<td><p>i &lt;= j</p></td>
</tr>
<tr>
<td><p>greater than</p></td>
<td><p>i &gt; j</p></td>
</tr>
<tr>
<td><p>greater than or equal</p></td>
<td><p>i &gt;= j</p></td>
</tr>
<tr>
<td><p>IN <span>set</span></p></td>
<td><p>i IN <code>('apples','oranges')</code></p></td>
<td><p>Sets can be of any type.</p></td>
</tr>
<tr>
<td><p>IN <span>range</span></p></td>
<td><p>i IN (j:k)</p></td>
<td><p>Ranges must be numeric or date types.</p></td>
</tr>
<tr>
<td><p>NOT</p></td>
<td><p><code>NOT( i )</code></p></td>
<td rowspan="3"><p>Boolean operators. Parentheses are required for <code>NOT</code>.</p></td>
</tr>
<tr>
<td><p>AND</p></td>
<td><p>i AND j AND k</p></td>
</tr>
<tr>
<td><p>OR</p></td>
<td><p>i OR j OR k</p></td>
</tr>
<tr>
<td><p>parentheses</p></td>
<td><p><code>()</code></p></td>
<td><p>Used for grouping.</p></td>
</tr>
</tbody>
</table>

!!! note

    When dates are used in comparisons or IF functions, they must be the same type, (date only, date/time, or time only). Make sure to use the correct modifier (d, ts, t) when using date constants in comparisons.

!!! note

    The following reserved words cannot be used as field names: AND, And, and, IN, In, in, NOT, Not, not, OR, Or, or. Names containing these strings, such as "Not Available", can be used.
