---
title: Working with a Collection of JavaBeans Data Adapter
description: "A collection of JavaBeans data adapters allows you to use JavaBeans as data for a report. In this context, a JavaBean is a Java class that exposes its attributes with a series of get methods, with..."
---

# Working with a Collection of JavaBeans Data Adapter

A collection of JavaBeans data adapters allows you to use JavaBeans as data for a report. In this context, a JavaBean is a Java class that exposes its attributes with a series of `get` methods, with the following syntax:

`public <`returnType`> getXXX()`

where `<``returnType``>` (the return value) is a generic Java class or a primitive type (such as `int`, `double`).

## Implementing the Factory Class for a Collection of JavaBeans

The collection of JavaBeans data adapter uses an external class (named `Factory`) to produce some objects (the JavaBeans) that constitute the data to pass to the report. To use a collection of JavaBeans as a data adapter in Jaspersoft Studio, you must create an instance of the `Factory` class and provide a static method to instantiate different JavaBeans and to return them as a collection (`java.util.Collection`) or an array (`Object[]`). The following example shows how to write an instance of the `Factory` class.

Suppose that you have a collection of JavaBeans, where the data is represented by a set of objects of type `PersonBean`. The following table shows the code for `PersonBean`, which contains two fields: `name` (the person’s name) and `age`:

<table>
<caption><p><code>PersonBean</code> example</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode java"><code class="sourceCode java"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">public</span> <span class="kw">class</span> PersonBean</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="op">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  <span class="kw">private</span> <span class="bu">String</span> name <span class="op">=</span> <span class="st">&quot;&quot;</span><span class="op">;</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="kw">private</span> <span class="dt">int</span> age <span class="op">=</span> <span class="dv">0</span><span class="op">;</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>                            </span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  <span class="kw">public</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="bu">String</span> name<span class="op">,</span> <span class="dt">int</span> age<span class="op">)</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="op">{</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    <span class="kw">this</span><span class="op">.</span><span class="fu">name</span> <span class="op">=</span> name<span class="op">;</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    <span class="kw">this</span><span class="op">.</span><span class="fu">age</span> <span class="op">=</span> age<span class="op">;</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  <span class="op">}</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  <span class="kw">public</span> <span class="dt">int</span> <span class="fu">getAge</span><span class="op">()</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  <span class="op">{</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    <span class="cf">return</span> age<span class="op">;</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>  <span class="op">}</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  <span class="kw">public</span> <span class="bu">String</span> <span class="fu">getName</span><span class="op">()</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>  <span class="op">{</span></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>    <span class="cf">return</span> name<span class="op">;</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>  <span class="op">}</span></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a><span class="op">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

To use this collection of beans, you need to create an instance of the `Factory` class. Your class, named `TestFactory`, must contain the actual data that is used by the report. In this case, it is something similar to this:

<table>
<caption><p><code>PersonBean</code> example - Class result</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode java"><code class="sourceCode java"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="kw">public</span> <span class="kw">class</span> TestFactory</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="op">{</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>                            </span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  <span class="kw">public</span> <span class="dt">static</span> java<span class="op">.</span><span class="fu">util</span><span class="op">.</span><span class="fu">Collection</span> <span class="fu">generateCollection</span><span class="op">()</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>    <span class="op">{</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>    java<span class="op">.</span><span class="fu">util</span><span class="op">.</span><span class="fu">Vector</span> collection <span class="op">=</span> <span class="kw">new</span> java<span class="op">.</span><span class="fu">util</span><span class="op">.</span><span class="fu">Vector</span><span class="op">();</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Ted&quot;</span><span class="op">,</span> <span class="dv">20</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Jack&quot;</span><span class="op">,</span> <span class="dv">34</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Bob&quot;</span><span class="op">,</span> <span class="dv">56</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Alice&quot;</span><span class="op">,</span><span class="dv">12</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Robin&quot;</span><span class="op">,</span><span class="dv">22</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>    collection<span class="op">.</span><span class="fu">add</span><span class="op">(</span><span class="kw">new</span> <span class="fu">PersonBean</span><span class="op">(</span><span class="st">&quot;Peter&quot;</span><span class="op">,</span><span class="dv">28</span><span class="op">)</span> <span class="op">);</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>                            </span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    <span class="cf">return</span> collection<span class="op">;</span></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>  <span class="op">}</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a><span class="op">}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

A data adapter based on this class would represent five JavaBeans of `PersonBean` type.

## Creating a Data Adapter from a Factory Class

Once you have created your `Factory` class instance, you can create a data adapter that uses your collection of JavaBeans.

1.  Create the connection globally or locally:

- To create the connection globally, right-click **Data Adapters** in the Repository Explorer and choose **Create Data Adapter**.
- To create the connection local to a project, click ![jss icon new data adapter](../assets/images/jss-icon-new-data-adapter.png), enter a name and location for the data adapter in the **DataAdapter File** dialog, and then click **Next**.

The **Data Adapter Wizard** appears (see [Data Adapter Wizard](data-adapters-creating.md)).

1.  To create a connection to handle JavaBeans, select **Collection of JavaBeans** in the list of data adapter types.

The fields necessary to create a collection of JavaBeans appear.

|  |
|----|
| ![jss data adapter collection of javabeans](../assets/images/jss-data-adapter-collection-of-javabeans.png) |
| *Figure 1: Collection of JavaBeans Data Adapter* |

1.  Create a name for your adapter.
2.  Enter the name of your Java class in the Factory class. For the example above, you would need to specify the class name for **TestFactory**.
3.  Enter the name of the static method in your Factory class. In the example above, this is `generateCollection`.
4.  By default, the field names in your JavaBeans become the field names in your data adapter. If your JavaBeans definition has field descriptions, and you want to use these as names in Jaspersoft Studio, select **Use field description**.
5.  If necessary, you can add the path to your jar files.

## Registering the Fields

One peculiarity of a collection of JavaBeans data adapters is that the fields are exposed through `get` methods. This means that if the JavaBean has a `getXyz()` method, `xyz` becomes the name of a record field (the JavaBean represents the record).

In this example, the `PersonBean` object shows two fields: `name` and `age`. Register them in the fields list as a `String` and an `Integer`, respectively.

Create a new empty report and add the two fields by right-clicking the **Fields** node in the outline view and selecting **Add field**. The field names and the types of the fields are: name (`java.lang.String`) and age (`java.lang.Integer`).

Drag the fields into the **Detail** band and run the report. (Make sure that the active connection is the TestFactoryAdapter.) To refer to an attribute of an attribute, use periods as a separator. For example, to access the `street` attribute of an `Address` class contained in the `PersonBean`, the syntax would be `address.street`. The real call would be `<someBean>.getAddress().getStreet()`.

|                                                            |
|------------------------------------------------------------|
| ![javabeans layout](../assets/images/javabeans-layout.png) |
| *Figure 2: Layout of a Report Based on JavaBeans*          |

If you selected **Use field description** when you specified the properties of your data adapter, the mapping between JavaBean attribute and field value uses the field description instead of the field name.

Jaspersoft Studio provides a visual tool to map JavaBean attributes to report fields. To use it, open the query window, go to the tab **JavaBean Data Source**, insert the full class name of the bean you want to explore, and click **Read attributes**. The tab displays the attributes of the specified bean class.

- If an attribute is also a Java object, you can double-click the object to display its other attributes.

- To map a field, select an attribute name and click the **Add Selected Field(s)** button.
