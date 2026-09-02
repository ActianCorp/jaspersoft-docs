---
title: A Simple Program
description: "In conclusion, the following is an example of a simple program that shows how to produce a PDF file from a Jasper file using a data source named JREmptyDataSource, a utility data source that provides..."
---

# A Simple Program

In conclusion, the following is an example of a simple program that shows how to produce a PDF file from a Jasper file using a data source named `JREmptyDataSource`, a utility data source that provides zero or more records without fields. The file `test.jasper`, referenced in the example, is the compiled version of the code in [A simple JRMXL file example](jrxml_sources_and_jasper_files.md).

**JasperTest.java**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode java"><code class="sourceCode java"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">import</span> <span class="im">net</span><span class="op">.</span><span class="im">sf</span><span class="op">.</span><span class="im">jasperreports</span><span class="op">.</span><span class="im">engine</span><span class="op">.*;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="kw">import</span> <span class="im">net</span><span class="op">.</span><span class="im">sf</span><span class="op">.</span><span class="im">jasperreports</span><span class="op">.</span><span class="im">engine</span><span class="op">.</span><span class="im">export</span><span class="op">.*;</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="kw">import</span> <span class="im">java</span><span class="op">.</span><span class="im">util</span><span class="op">.*;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="kw">public</span> <span class="kw">class</span> JasperTest</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="op">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    <span class="kw">public</span> <span class="dt">static</span> <span class="dt">void</span> <span class="fu">main</span><span class="op">(</span><span class="bu">String</span><span class="op">[]</span> args<span class="op">)</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    <span class="op">{</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>        <span class="bu">String</span> fileName <span class="op">=</span> <span class="st">&quot;/devel/examples/test.jasper&quot;</span><span class="op">;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>        <span class="bu">String</span> outFileName <span class="op">=</span> <span class="st">&quot;/devel/examples/test.pdf&quot;</span><span class="op">;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>        <span class="bu">HashMap</span> hm <span class="op">=</span> <span class="kw">new</span> <span class="bu">HashMap</span><span class="op">();</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>        <span class="cf">try</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>        <span class="op">{</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>        JasperPrint print <span class="op">=</span> JasperFillManager<span class="op">.</span><span class="fu">fillReport</span><span class="op">(</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>        fileName<span class="op">,</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>        hm<span class="op">,</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>        <span class="kw">new</span> <span class="fu">JREmptyDataSource</span><span class="op">());</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>        JRExporter exporter <span class="op">=</span> </span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>        <span class="kw">new</span> net<span class="op">.</span><span class="fu">sf</span><span class="op">.</span><span class="fu">jasperreports</span><span class="op">.</span><span class="fu">engine</span><span class="op">.</span><span class="fu">export</span><span class="op">.</span><span class="fu">JRPdfExporter</span><span class="op">();</span></span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>           exporter.setParameter(
                JRExporterParameter.OUTPUT_FILE_NAME,
                outFileName);
            exporter.setParameter(
            JRExporterParameter.JASPER_PRINT,print);
            exporter.exportReport();
            System.out.println(&quot;Created file: &quot; + outFileName);
        }
        catch (JRException e)
        {
            e.printStackTrace();
            System.exit(1);
        }
        catch (Exception e)
        {
            e.printStackTrace();
            System.exit(1);
        }
    }
}</code></pre></div></td>
</tr>
</tbody>
</table>
