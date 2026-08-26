---
title: Working with Dashboards
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# 1.1 Working with Dashboards

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

The resource service also gives access to dashboard resources in commercial editions of JasperReports Server. Dashboards are managed as normal resources whose descriptors can be created, viewed, modified, or deleted with the resource service. However, dashboards can be viewed only through the web interface of JasperReports Server because they do not have any output format that can be generated or transmitted through the REST API.

Therefore, an application using the REST API can only manipulate the definition of the dashboard, that is the selection of reports to display and their layout. In order to work with a dashboard, your application must parse its resource descriptor, make changes, and generate a new, valid descriptor to send back to the server.

The general structure of a dashboard descriptor contains:

-   Typical descriptor properties such as `label`, `description`, and `PROP_PARENT_FOLDER`.

-   The `dashboardState` descriptor containing:

    -   The `ADHOC_FRAMES` property that lists the reports, labels, and buttons, and gives their coordinates in the dashboard.
    -   The `ADHOC_PROPERTIES` property that gives the overall dashboard layout properties.

-   `reference` descriptors for each of the reports included in the `ADHOC_FRAMES` property. These references ensure that the reports can’t be deleted from the repository as long as they are used in this dashboard.

The following example shows the contents of a dashboard’s resource descriptor:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;SampleDashboard&quot;</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a>  <span class="ot">wsType=</span><span class="st">&quot;dashboard&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;/Dashboards/SampleDashboard&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">label</span>&gt;Sample Dashboard&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">description</span>&gt;Created in Dashboard Designer, viewed through REST.&lt;/<span class="kw">description</span>&gt;</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">creationDate</span>&gt;1318380317305&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">value</span>&gt;com.jaspersoft.ji.adhoc.DashboardResource&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;/Dashboards&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_VERSION&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;0&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_HAS_DATA&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;false&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;dashboardState&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">creationDate</span>&gt;1318380317305&lt;/<span class="kw">creationDate</span>&gt;</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_RESOURCE_TYPE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;dashboardState&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_PARENT_FOLDER&quot;</span>&gt;</span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/Dashboards/SampleDashboard&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;ADHOC_PAPER_SIZE&quot;</span>&gt;&lt;<span class="kw">value</span>&gt;content&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;ADHOC_FRAMES&quot;</span>&gt;</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameLeft=0;</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameTop=0;</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameWidth=246;</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameHeight=405;</span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceType=</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>  com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.ReportUnit;</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceName=</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>  Top Fives Report;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameSource=%2Fflow.html
  %3F_flowId%3DviewReportFlow%26viewAsDashboardFrame%3Dtrue%26reportUnit%3D;
frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashResourceIndex=0;
frame_1,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameScrollBars=false;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameLeft=254;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameTop=0;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameWidth=450;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameHeight=418;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceType=
  com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.ReportUnit;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceName=
  Sales By Month Report;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameSource=%2Fflow.html
  %3F_flowId%3DviewReportFlow%26viewAsDashboardFrame%3Dtrue%26reportUnit%3D;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashResourceIndex=1;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameScrollBars=false;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceType=
  com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.ReportUnit;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceName=
  Sales By Month Report;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameSource=%2Fflow.html
  %3F_flowId%3DviewReportFlow%26viewAsDashboardFrame%3Dtrue%26reportUnit%3D;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashResourceIndex=1;
frame_2,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameScrollBars=false;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameLeft=712;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameTop=0;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameWidth=200;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameHeight=350;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceType=
  com.jaspersoft.jasperserver.api.metadata.jasperreports.domain.ReportUnit;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameResourceName=
  Sales Gauges Report;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameSource=%2Fflow.html
  %3F_flowId%3DviewReportFlow%26viewAsDashboardFrame%3Dtrue%26reportUnit%3D;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashResourceIndex=2;
frame_3,com.jaspersoft.ji.adhoc.DashboardContentFrame,dashFrameScrollBars=false;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameLeft=736;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameTop=352;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameWidth=66;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameHeight=16;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashTextFrameLabel=Start Month;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,fontResizes=false;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashTextFrameFontSize=11;
text_2,com.jaspersoft.ji.adhoc.DashboardTextFrame,maxFontSize=11;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameLeft=816;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameTop=352;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameWidth=85;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameHeight=16;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameParamName=
  startMonth;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameParamValue=
  1;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameDefaultParam
  Value=1;
control_2,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameDataType=
  String;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameLeft=744;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameTop=376;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameWidth=59;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashFrameHeight=16;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashTextFrameLabel=End Month;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,fontResizes=false;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,dashTextFrameFontSize=11;
text_3,com.jaspersoft.ji.adhoc.DashboardTextFrame,maxFontSize=11;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameLeft=816;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameTop=376;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameWidth=85;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashFrameHeight=16;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameParamName=
  endMonth;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameParamValue=
  12;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameDefaultParam
  Value=12;
control_3,com.jaspersoft.ji.adhoc.DashboardControlFrame,dashControlFrameDataType=
  String;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameLeft=832;
button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameTop=400;
button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameWidth=72;
button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameHeight=24;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashClickableFrameID=
  submit;
button_1,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashClickableFrameType=
  button;</code></pre></div></td>
</tr>
<tr>
<td><div class="language-text highlight"><pre><code>button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameLeft=744;
button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameTop=400;
button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameWidth=72;
button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashFrameHeight=24;
button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashClickableFrameID=reset;
button_2,com.jaspersoft.ji.adhoc.DashboardClickableFrame,dashClickableFrameType=
  button;
      &lt;/value&gt;
    &lt;/resourceProperty&gt;</code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb13"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;ADHOC_PROPERTIES&quot;</span>&gt;</span>
<span id="cb13-2"><a href="#cb13-2" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;layoutSize=1024x768;</span>
<span id="cb13-3"><a href="#cb13-3" aria-hidden="true" tabindex="-1"></a>        useAbsoluteSizing=true;</span>
<span id="cb13-4"><a href="#cb13-4" aria-hidden="true" tabindex="-1"></a>        paperSize=content;</span>
<span id="cb13-5"><a href="#cb13-5" aria-hidden="true" tabindex="-1"></a>        LayoutLeft=286;</span>
<span id="cb13-6"><a href="#cb13-6" aria-hidden="true" tabindex="-1"></a>        paramValuesChanged=true;</span>
<span id="cb13-7"><a href="#cb13-7" aria-hidden="true" tabindex="-1"></a>        LayoutTop=176;</span>
<span id="cb13-8"><a href="#cb13-8" aria-hidden="true" tabindex="-1"></a>        localDatePattern=MM-dd-yyyy;</span>
<span id="cb13-9"><a href="#cb13-9" aria-hidden="true" tabindex="-1"></a>      &lt;/<span class="kw">value</span>&gt;</span>
<span id="cb13-10"><a href="#cb13-10" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb13-11"><a href="#cb13-11" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
<tr>
<td><div class="sourceCode" id="cb14"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reference&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb14-3"><a href="#cb14-3" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb14-4"><a href="#cb14-4" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/supermart/details/TopFivesReport&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb14-5"><a href="#cb14-5" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb14-6"><a href="#cb14-6" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reference&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb14-7"><a href="#cb14-7" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb14-8"><a href="#cb14-8" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb14-9"><a href="#cb14-9" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/supermart/salesByMonth/SalesByMonthReport&lt;/<span class="kw">value</span>&gt;&lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb14-10"><a href="#cb14-10" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb14-11"><a href="#cb14-11" aria-hidden="true" tabindex="-1"></a>  &lt;<span class="kw">resourceDescriptor</span> <span class="ot">name=</span><span class="st">&quot;&quot;</span> <span class="ot">wsType=</span><span class="st">&quot;reference&quot;</span> <span class="ot">uriString=</span><span class="st">&quot;&quot;</span> <span class="ot">isNew=</span><span class="st">&quot;false&quot;</span>&gt;</span>
<span id="cb14-12"><a href="#cb14-12" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">label</span>&gt;null&lt;/<span class="kw">label</span>&gt;</span>
<span id="cb14-13"><a href="#cb14-13" aria-hidden="true" tabindex="-1"></a>    &lt;<span class="kw">resourceProperty</span> <span class="ot">name=</span><span class="st">&quot;PROP_REFERENCE_URI&quot;</span>&gt;</span>
<span id="cb14-14"><a href="#cb14-14" aria-hidden="true" tabindex="-1"></a>      &lt;<span class="kw">value</span>&gt;/supermart/revenueAndProfit/SalesGaugesReport&lt;/<span class="kw">value</span>&gt;</span>
<span id="cb14-15"><a href="#cb14-15" aria-hidden="true" tabindex="-1"></a>    &lt;/<span class="kw">resourceProperty</span>&gt;</span>
<span id="cb14-16"><a href="#cb14-16" aria-hidden="true" tabindex="-1"></a>  &lt;/<span class="kw">resourceDescriptor</span>&gt;</span>
<span id="cb14-17"><a href="#cb14-17" aria-hidden="true" tabindex="-1"></a>&lt;/<span class="kw">resourceDescriptor</span>&gt;</span></code></pre></div></td>
</tr>
</tbody>
</table>
