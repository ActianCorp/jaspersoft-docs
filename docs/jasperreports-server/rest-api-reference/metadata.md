---
title: Working With Domains
description: "This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit..."
---

# Working With Domains

!!! info "Important"

    This section describes functionality that can be restricted by the software license for JasperReports Server. If you don’t see some of the options described in this section, your license may prohibit you from using them. To find out what you're licensed to use, or to upgrade your license, contact Jaspersoft.

This chapter explains the limited interaction with domains that is available through the REST API. The metadata service retrieves the display layer of a domain containing sets and items and their labels. You can also retrieve the full domain schema and security files through the resources service, but the API provides no functionality to parse these.

This chapter includes the following sections:

-   The metadata Service
-   Fetching a Domain Schema
-   Fetching Domain Bundles and Security Files

## The metadata Service

The rest_v2/domains/metadata service gives access to the sets and items exposed by a domain for use in Ad Hoc reports. Items are database fields exposed by the Domain, after all joins, filters, and calculated fields have been applied to the database tables selected in the Domain. Sets are groups of items, arranged by the domain creator for use by report creators.

!!! note

    A limitation of the metadata service only allows it to operate on domains with a single data island. A data island is a group of fields that are all related by joins between the database tables in the domain. Fields that belong to tables that are not joined in the domain belong to separate data islands.

If your domain contains localization bundles you can specify a locale and an optional alternate locale and preference (called q-value, a decimal between 0 and 1).

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
<td colspan="3"><p><span>http://&lt;host&gt;:&lt;port&gt;/jasperserver[-pro]/<span>rest_v2/domains</span>/path/to/Domain/<span>metadata</span></span></p></td>
</tr>
<tr>
<td colspan="4"><p>Options</p></td>
</tr>
<tr>
<td colspan="4"><p><span>Accept-Language: &lt;locale&gt;[, &lt;alt-locale&gt;;q=0.8]</span></p>
<p><span>Accept: application/xml (default)</span></p>
<p><span>Accept: application/json</span></p></td>
</tr>
<tr>
<td colspan="3"><p>Return Value on Success</p></td>
<td><p>Typical Return Values on Failure</p></td>
</tr>
<tr>
<td colspan="3"><p>200 OK - The body is XML containing the list of <span>resourceDescriptors</span>.</p></td>
<td><p>404 Not Found - The specified domain URI is not found in the repository. This service also returns an XML <code>errorDescriptor</code> giving a human-readable error message.</p></td>
</tr>
</tbody>
</table>

The response of the metadata service is an XML or JSON structure that describes the sets and items available in the selected domain. This metadata includes the localized labels for the sets and items, as well as the datatypes of the items. The `resourceId` of the sets and items are internal to the domain and not meaningful or otherwise useable.

For more information about domains, refer to the JasperReports Server User Guide.

The following example shows the JSON response for a domain with:

-   A set named expense containing:

    -   An item named Exp Date of type Date
    -   An item named Amount of type BigDecimal

-   A set named store containing:

    -   An item named Store Type of type String
    -   ...

``` json
{
    "rootLevel": {
        "id":"root",
        "subLevels":[
            {
                "id":"expense_join",
                "label":"expense",
                "properties": {
                        "resourceId": "expense_join"
                },
                "items":[
                    {
                        "id":"ej_expense_fact_exp_date",
                        "label":"Exp Date",
                        "properties": {
                                "JavaType": "java.sql.Date",
                                "resourceId": "expense_join.e.exp_date"
                        }
                    },
                    {
                        "id":"ej_expense_fact_amount",
                        "label":"Amount",
                        "properties": {
                                "JavaType": "java.math.BigDecimal",
                                "resourceId": "expense_join.e.amount"
                        }
                    }
                ]
            },
            {
                "id":"expense_join_store",
                "label":"store",
                "properties": {
                        "resourceId":"expense_join"
                },
                "items":[
                    {
                        "id":"ej_store_store_type",
                        "label":"Store Type",
                        "properties": {
                                "JavaType": "java.lang.String",
                                "resourceId": "expense_join.s.store_type"
                        }
                    },
                    ...
                ]
            }
        ]
    }
}
```

The following example shows the same domain as returned by the metadata service in XML format:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<domainMetadata>
    <rootLevel>
        <id>root</id>
        <subLevels>
            <subLevel>
                <id>expense_join</id>
                <label>expense</label>
                <properties>
                    <entry>
                        <key>resourceId</key>
                        <value>expense_join</value>
                    </entry>
                </properties>
                <items>
                    <item>
                        <id>ej_expense_fact_exp_date</id>
                        <label>Exp Date</label>
                        <properties>
                            <entry>
                                <key>JavaType</key>
                                <value>java.sql.Date</value>
                            </entry>
                            <entry>
                                <key>resourceId</key>
                                <value>expense_join.e.exp_date</value>
                            </entry>
                        </properties>
                    </item>
                    <item>
                        <id>ej_expense_fact_amount</id>
                        <label>Amount</label>
                        <properties>
                            <entry>
                                <key>JavaType</key>
                                <value>java.math.BigDecimal</value>
                            </entry>
                            <entry>
                                <key>resourceId</key>
                                <value>expense_join.e.amount</value>
                            </entry>
                        </properties>
                    </item>
                </items>
            </subLevel>
            <subLevel>
                <id>expense_join_store</id>
                <label>store</label>
                <properties>
                    <entry>
                        <key>resourceId</key>
                        <value>expense_join</value>
                    </entry>
                </properties>
                <items>
                    <item>
                        <id>ej_store_store_type</id>
                        <label>Store Type</label>
                        <properties>
                            <entry>
                                <key>JavaType</key>
                                <value>java.lang.String</value>
                            </entry>
                            <entry>
                                <key>resourceId</key>
                                <value>expense_join.s.store_type</value>
                            </entry>
                        </properties>
                    </item>
                    ...
                </items>
            </subLevel>
        </subLevels>
    </rootLevel>
</domainMetadata>
```

!!! note

    If the Domain metadata service encounters one or more issues, the response includes either a list or an object, depending on the number of errors returned. If a single error is returned, the response includes an object. If multiple errors are returned, it includes a list.

## Fetching a Domain Schema

The metadata service returns only the displaying information about a domain, not its internal definition. The fields joins, filters, and calculated fields that define the internal structure of a domain make up the domain design. The XML representation of a domain design is called the domain schema.

Currently, there is no REST service to interact with domain schemas, but you can use the resources service to retrieve the raw schema. First, retrieve the resource descriptor for the domain. For example, to view the descriptor for the Supermart Domain, use the following request (when logged in as `jasperadmin`):

GET http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/resources/Domains/supermartDomain

This descriptor contains the Domain schema as an internal resource:

``` xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<semanticLayerDataSource>
    <creationDate>2013-10-10T15:30:31</creationDate>
    <description>Comprehensive example of Domain (pre-joined table sets for complex reporting, custom query based dataset, column and row security, I18n bundles)</description>
    <label>Supermart Domain</label>
    <permissionMask>1</permissionMask>
    <updateDate>2013-10-10T15:30:31</updateDate>
    <uri>/organizations/organization_1/Domains/supermartDomain</uri>
    <version>1</version>
    <dataSourceReference>
        <uri>/organizations/organization_1/analysis/datasources/FoodmartDataSourceJNDI</uri>
    </dataSourceReference>
    <bundles>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain.properties</uri></fileReference>
            <locale></locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_en_US.properties</uri></fileReference>
            <locale>en_US</locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_de.properties</uri></fileReference>
            <locale>de</locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_fr.properties</uri></fileReference>
            <locale>fr</locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_es.properties</uri></fileReference>
            <locale>es</locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_ja.properties</uri></fileReference>
            <locale>ja</locale>
        </bundle>
        <bundle>
            <fileReference><uri>/organizations/organization_1/Domains/supermartDomain_files/supermart_domain_zh_CN.properties</uri></fileReference>
            <locale>zh_CN</locale>
        </bundle>
    </bundles>
    <schemaFileReference>
        <uri>/organizations/organization_1/Domains/supermartDomain_files/supermartDomain_schema</uri>
    </schemaFileReference>
    <securityFileReference>
        <uri>/organizations/organization_1/Domains/supermartDomain_files/supermartDomain_domain_security</uri>
    </securityFileReference>
</semanticLayerDataSource>
```

Use the following request to access the Domain schema file inside the Domain resource:

GET http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermartDomain_schema

The Domain schema is an XML file with a structure explained in the JasperReports Server User Guide. If you wish to modify the schema programmatically, you must write your own parser to access its fields and definitions. You can then replace the schema file in the domain with one of the file updating methods described in [1.1, “Uploading File Resources,” on page 1](file_resources.md).

## Fetching Domain Bundles and Security Files

Once you have the descriptor of a domain resource as shown in the previous section, you can access the other files that help define a domain. For example, you can access the language bundles of the Supermart Domain with the following request:

GET http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermart_domain\_&lt;locale&gt;.properties

Language bundles are Java properties files that follow the language bundle naming convention, and that contain the names of the sets and fields in the language of the locale in the filename.

You can also retrieve the localized set and item names by specifying Accept-Language when using the metadata service. However, by accessing the language bundles through the Domain descriptor, you read the default bundle to see the pattern of keys and values, and then create a bundle for a new locale.

Domains may also contain a security file that is also stored as an internal resource of the Domain descriptor. Use the following example to request the security file of the Supermart Domain in the sample data:

GET http://&lt;host&gt;:&lt;port&gt;/jasperserver-pro/rest_v2/resources/Domains/supermartDomain_files/supermart_domain_security

A security file defines a complex set of access permissions to the data in the rows and columns returned by the Domain, based on the username, roles, or profile attributes of the user running a Domain-based report. As with the Domain schema file, you must write your own parser to interpret this file and modify it.

You can then upload an updated language bundle or security file for the domain with one of the methods described in [1.1, “Uploading File Resources,” on page 1](file_resources.md).

For more information about language bundles and security files in Domains, see the JasperReports Server User Guide.
