---
title: ResourceDescriptor API Constants
description: "The constants that the services require are defined in the following classes:"
---

# Appendix 1 ResourceDescriptor API Constants

The constants that the services require are defined in the following classes:

- `com.jaspersoft.jasperserver.api.metadata.xml.domain.impl.ResourceDescriptor`
- `com.jaspersoft.jasperserver.api.metadata.xml.domain.impl.Argument`

The following values are extracted from `ResourceDescriptor`:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>// Resource wsTypes
TYPE_FOLDER = &quot;folder&quot;;
TYPE_REPORTUNIT = &quot;reportUnit&quot;;
TYPE_DATASOURCE = &quot;datasource&quot;;
TYPE_DATASOURCE_JDBC = &quot;jdbc&quot;;
TYPE_DATASOURCE_JNDI = &quot;jndi&quot;;
TYPE_DATASOURCE_BEAN = &quot;bean&quot;;
TYPE_DATASOURCE_VIRTUAL = &quot;virtual&quot;;
TYPE_DATASOURCE_CUSTOM = &quot;custom&quot;;
TYPE_DATASOURCE_AWS = &quot;aws&quot;; // Amazon Web Services
TYPE_IMAGE = &quot;img&quot;;
TYPE_FONT = &quot;font&quot;;
TYPE_JRXML = &quot;jrxml&quot;;
TYPE_CLASS_JAR = &quot;jar&quot;;
TYPE_RESOURCE_BUNDLE = &quot;prop&quot;;
TYPE_REFERENCE = &quot;reference&quot;;
TYPE_INPUT_CONTROL = &quot;inputControl&quot;;
TYPE_DATA_TYPE = &quot;dataType&quot;;
TYPE_OLAP_MONDRIAN_CONNECTION = &quot;olapMondrianCon&quot;;
TYPE_OLAP_XMLA_CONNECTION = &quot;olapXmlaCon&quot;;
TYPE_MONDRIAN_SCHEMA = &quot;olapMondrianSchema&quot;;
TYPE_ACCESS_GRANT_SCHEMA = &quot;accessGrantSchema&quot;; // Pro-only
TYPE_UNKNOW = &quot;unknow&quot;;
TYPE_LOV = &quot;lov&quot;; // List of values...
TYPE_QUERY = &quot;query&quot;;
TYPE_CONTENT_RESOURCE = &quot;contentResource&quot;;
TYPE_STYLE_TEMPLATE = &quot;jrtx&quot;;
TYPE_XML_FILE = &quot;xml&quot;;</code></pre></td>
</tr>
<tr>
<td><pre class="text"><code>// These constants are copied here from DataType for facility
DT_TYPE_TEXT = 1;
DT_TYPE_NUMBER = 2;
DT_TYPE_DATE = 3;
DT_TYPE_DATE_TIME = 4;
// These constants are copied here from InputControl for facility
IC_TYPE_BOOLEAN = 1;
IC_TYPE_SINGLE_VALUE = 2;
IC_TYPE_SINGLE_SELECT_LIST_OF_VALUES = 3;
IC_TYPE_SINGLE_SELECT_QUERY = 4;
IC_TYPE_MULTI_VALUE = 5;      // This type is deprecated
IC_TYPE_MULTI_SELECT_LIST_OF_VALUES = 6;
IC_TYPE_MULTI_SELECT_QUERY = 7;
IC_TYPE_SINGLE_SELECT_LIST_OF_VALUES_RADIO = 8;
IC_TYPE_SINGLE_SELECT_QUERY_RADIO = 9;
IC_TYPE_MULTI_SELECT_LIST_OF_VALUES_CHECKBOX = 10;
IC_TYPE_MULTI_SELECT_QUERY_CHECKBOX = 11;
...
// ReportUnit resource properties
...RU_CONTROLS_LAYOUT_POPUP_SCREEN = 1;
RU_CONTROLS_LAYOUT_SEPARATE_PAGE = 2;
RU_CONTROLS_LAYOUT_TOP_OF_PAGE = 3;
RU_CONTROLS_LAYOUT_IN_PAGE = 4;
...
// Content resource properties
...
CONTENT_TYPE_PDF = &quot;pdf&quot;;
CONTENT_TYPE_HTML = &quot;html&quot;;
CONTENT_TYPE_XLS = &quot;xls&quot;;
CONTENT_TYPE_RTF = &quot;rtf&quot;;
CONTENT_TYPE_CSV = &quot;csv&quot;;
CONTENT_TYPE_IMAGE = &quot;img&quot;;</code></pre></td>
</tr>
</tbody>
</table>

The constants in the `Argument` class are:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><pre class="text"><code>// Arguments
MODIFY_REPORTUNIT = &quot;MODIFY_REPORTUNIT_URI&quot;;
CREATE_REPORTUNIT = &quot;CREATE_REPORTUNIT_BOOLEAN&quot;;
LIST_DATASOURCES  = &quot;LIST_DATASOURCES&quot;;
IC_GET_QUERY_DATA  = &quot;IC_GET_QUERY_DATA&quot;;
VALUE_TRUE = &quot;true&quot;;
VALUE_FALSE = &quot;false&quot;;
RUN_OUTPUT_FORMAT = &quot;RUN_OUTPUT_FORMAT&quot;;
RUN_OUTPUT_FORMAT_PDF = &quot;PDF&quot;;
RUN_OUTPUT_FORMAT_JRPRINT = &quot;JRPRINT&quot;;
RUN_OUTPUT_FORMAT_HTML = &quot;HTML&quot;;
RUN_OUTPUT_FORMAT_XLS = &quot;XLS&quot;;
RUN_OUTPUT_FORMAT_XML = &quot;XML&quot;;
RUN_OUTPUT_FORMAT_CSV = &quot;CSV&quot;;
RUN_OUTPUT_FORMAT_RTF = &quot;RTF&quot;;
RUN_OUTPUT_IMAGES_URI = &quot;IMAGES_URI&quot;;
RUN_OUTPUT_PAGE = &quot;PAGE&quot;;
RUN_TRANSFORMER_KEY = &quot;TRANSFORMER_KEY&quot;;
RU_REF_URI = &quot;RU_REF_URI&quot;;
PARAMS_ARG = &quot;PARAMS_ARG&quot;;
LIST_RESOURCES = &quot;LIST_RESOURCES&quot;;
RESOURCE_TYPE = &quot;RESOURCE_TYPE&quot;;
REPORT_TYPE = &quot;REPORT_TYPE&quot;;
START_FROM_DIRECTORY = &quot;START_FROM_DIRECTORY&quot;;
NO_RESOURCE_DATA_ATTACHMENT = &quot;NO_ATTACHMENT&quot;;
NO_SUBRESOURCE_DATA_ATTACHMENTS = &quot;NO_SUBRESOURCE_ATTACHMENTS&quot;;
DESTINATION_URI = &quot;DESTINATION_URI&quot;;</code></pre></td>
</tr>
</tbody>
</table>
