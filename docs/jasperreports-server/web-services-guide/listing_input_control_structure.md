---
title: Listing Input Control Structure
description: The following method returns a description of the structure of the input controls for a given report.
---

# 1.0.1 Listing Input Control Structure

The following method returns a description of the structure of the input controls for a given report.

<table>
<tbody>
<tr>
<td><p>Method</p></td>
<td colspan="3"><p>URL</p></td>
</tr>
<tr>
<td><p>GET</p></td>
<td colspan="3"><p>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/reports</span>/path/to/report<span>/inputControls/</span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p>accept: application/json</p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK – The content is a JSON object that describes the input control structure. See example below.</p></td>
<td><p>404 Not Found – When the specified report URI is not found in the repository.</p></td>
</tr>
</tbody>
</table>

The body of the response contains the structure of the input controls for the report. This structure contains the information needed by your application to display the input controls to your users and allow them to make a selection. In particular, this includes any cascading structure as a set of dependencies between input controls. Each input control also has a type that indicates how the user should be allowed to make a choice:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><ul>
<li>bool</li>
<li>singleSelect</li>
<li>singleSelectRadio</li>
<li>multiSelectCheckbox</li>
<li>multiSelect</li>
</ul></td>
<td><ul>
<li>singleValue</li>
<li>singleValueText</li>
<li>singleValueNumber</li>
<li>singleValueDate</li>
<li>singleValueDatetime</li>
<li>singleValueTime</li>
</ul></td>
</tr>
</tbody>
</table>

The following example shows a response in the JSON format:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">{</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="dt">&quot;inputControl&quot;</span> <span class="fu">:</span> <span class="ot">[</span> <span class="fu">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;id&quot;</span><span class="fu">:</span><span class="st">&quot;Cascading_name_single_select&quot;</span><span class="fu">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;label&quot;</span><span class="fu">:</span><span class="st">&quot;Cascading name single select&quot;</span><span class="fu">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;mandatory&quot;</span><span class="fu">:</span><span class="st">&quot;true&quot;</span><span class="fu">,</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;readOnly&quot;</span><span class="fu">:</span><span class="st">&quot;false&quot;</span><span class="fu">,</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;type&quot;</span><span class="fu">:</span><span class="st">&quot;singleSelect&quot;</span><span class="fu">,</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;uri&quot;</span><span class="fu">:</span><span class="st">&quot;repo:/reports/samples/Cascading_multi_select_report_files/Cascading_name_single_select&quot;</span><span class="fu">,</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;visible&quot;</span><span class="fu">:</span><span class="st">&quot;true&quot;</span><span class="fu">,</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;masterDependencies&quot;</span><span class="fu">:{</span><span class="dt">&quot;controlId&quot;</span><span class="fu">:</span><span class="ot">[</span><span class="st">&quot;Country_multi_select&quot;</span><span class="ot">,</span><span class="st">&quot;Cascading_state_multi_</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="st">                        select&quot;</span><span class="ot">]</span><span class="fu">},</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;slaveDependencies&quot;</span><span class="fu">:</span><span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  <span class="dt">&quot;validationRules&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span> <span class="er">...</span> <span class="fu">}</span><span class="ot">]</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  <span class="st">&quot;dataType&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;type&quot;</span><span class="fu">:</span> <span class="st">&quot;number&quot;</span><span class="fu">,</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;maxValue&quot;</span><span class="fu">:</span> <span class="st">&quot;20&quot;</span><span class="fu">,</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;strictMax&quot;</span><span class="fu">:</span> <span class="kw">true</span><span class="fu">,</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;minValue&quot;</span><span class="fu">:</span> <span class="st">&quot;5&quot;</span><span class="fu">,</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;strictMin&quot;</span><span class="fu">:</span> <span class="kw">true</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>  <span class="fu">}</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>  <span class="st">&quot;state&quot;</span><span class="er">:</span> <span class="fu">{</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;uri&quot;</span><span class="fu">:</span> <span class="st">&quot;/reports/samples/Cascading_multi_select_report_files/</span></span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a><span class="st">            Cascading_name_single_select&quot;</span><span class="fu">,</span></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;id&quot;</span><span class="fu">:</span> <span class="st">&quot;Cascading_name_single_select&quot;</span><span class="fu">,</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="kw">null</span><span class="fu">,</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    <span class="dt">&quot;options&quot;</span><span class="fu">:</span> <span class="ot">[</span><span class="fu">{</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;selected&quot;</span><span class="fu">:</span> <span class="kw">false</span><span class="fu">,</span></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;label&quot;</span><span class="fu">:</span> <span class="st">&quot;A &amp; U Jaramillo Telecommunications, Inc&quot;</span><span class="fu">,</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>      <span class="dt">&quot;value&quot;</span><span class="fu">:</span> <span class="st">&quot;A &amp; U Jaramillo Telecommunications, Inc&quot;</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>      <span class="fu">}</span><span class="ot">,</span>      <span class="er">...</span>      <span class="ot">]</span><span class="fu">}</span>               <span class="fu">}</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>  <span class="er">}</span><span class="ot">,</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>  <span class="er">...</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a><span class="ot">]</span><span class="fu">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

The structure includes a set of validation rules for each input control. These rules indicate what type of validation your client should perform on input control values it receives from your users, and if the validation fails, the message to display. Depending on the type of the input control, the following validations are possible:

-   mandatoryValidationRule – This input is required and your client should ensure the user enters a value.
-   dateTimeFormatValidation – This input must have a data time format and your client should ensure the user enters a valid date and time.

The following sample shows the structure of these two possible validation rules.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>  &quot;validationRules&quot;: [{
    &quot;mandatoryValidationRule&quot; : {
      &quot;errorMessage&quot; : &quot;This field is mandatory so you must enter data.&quot;
    },
    &quot;dateTimeFormatValidationRule&quot; : {
      &quot;errorMessage&quot; : &quot;Specify a valid date value.&quot;,
      &quot;format&quot; : &quot;yyyy-MM-dd&quot;
    }
  }]</code></pre></div></td>
</tr>
</tbody>
</table>
