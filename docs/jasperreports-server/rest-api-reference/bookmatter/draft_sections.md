---
title: Draft Sections
description: "When rendering a report, by default it is scaled to fit in the container you specify. When users resize their window, reports will change so that they fit to the new size of the container. This..."
---

# Draft Sections

...

## Resizing a Report

When rendering a report, by default it is scaled to fit in the container you specify. When users resize their window, reports will change so that they fit to the new size of the container. This section explains several ways to change the size of a rendered report.

To set a different scaling factor when rendering a report, specify its `scale` property:

- `container` – The report is scaled to fully fit within the container, both in width and height. If the container is a different aspect ratio, there will be white space in the dimension where the container is larger. This is the default scaling behavior when the `scale` property is not specified.
- `width` – The report is scaled to fit within the width of the container. If the report is taller than the container, users will need to scroll vertically to see the entire report.
- `height` – The report is scaled to fit within the height of the container. If the report is wider than the container, users will need to scroll horizontally to see the entire report.
- Scale factor – A decimal value greater than 0, with 1 being equivalent to 100%. A value between 0 and 1 reduces the report from its normal size, and a value greater than 1 enlarges it. If either or both dimensions of the scaled report are larger than the container, users will need to scroll to see the entire report.

In every case, the entire report is scaled in both directions by the same amount, you cannot change the aspect ratio of tables and crosstab elements.

For example, to initialize the report to half-size (50%), specify the following scale:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">var</span> report <span class="op">=</span> v<span class="op">.</span><span class="fu">report</span>({</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">resource</span><span class="op">:</span> <span class="st">&quot;/public/Sample&quot;</span><span class="op">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">container</span><span class="op">:</span> <span class="st">&quot;#reportContainer&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">scale</span><span class="op">:</span> <span class="fl">0.5</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>})<span class="op">;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

You can also change the scale after rendering, in this case to more than double size (250%):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>report
    .scale(2.5)
    .run();</code></pre></td>
</tr>
</tbody>
</table>

Alternatively, you can turn off the container resizing and modify the size of the container explicitly:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode javascript"><code class="sourceCode javascript"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">var</span> report <span class="op">=</span> v<span class="op">.</span><span class="fu">report</span>({</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>    <span class="dt">resource</span><span class="op">:</span> <span class="st">&quot;/public/Sample&quot;</span><span class="op">,</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>    <span class="dt">container</span><span class="op">:</span> <span class="st">&quot;#reportContainer&quot;</span><span class="op">,</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>    <span class="dt">scale</span><span class="op">:</span> <span class="st">&quot;container&quot;</span><span class="op">,</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="dt">autoresize</span><span class="op">:</span> <span class="kw">false</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>})<span class="op">;</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="fu">$</span>(<span class="st">&quot;#reportContainer&quot;</span>)<span class="op">.</span><span class="fu">width</span>(<span class="dv">500</span>)<span class="op">.</span><span class="fu">height</span>(<span class="dv">500</span>)<span class="op">;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>report<span class="op">.</span><span class="fu">resize</span>()<span class="op">;</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
