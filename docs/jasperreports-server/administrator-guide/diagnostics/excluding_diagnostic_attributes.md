---
title: Excluding Diagnostic Attributes
description: "The JasperReports Server diagnostic feature exposes a set of managed beans (MBeans), each with a number of JMX attributes. By default, all attributes of all MBeans are available. If you would like to..."
---

# Excluding Diagnostic Attributes

The JasperReports Server diagnostic feature exposes a set of managed beans (MBeans), each with a number of JMX attributes. By default, all attributes of all MBeans are available. If you would like to limit what is exposed, you can exclude any of the attributes or entire beans through the following configuration file:

`.../WEB-INF/applicationContext-diagnostic.xml`

-   To exclude an attribute, locate the MBean where it's defined and uncomment it from the `excludedDiagnosticAttributes` property. For example, if you want to hide sensitive information about your internal database, modify the `diagnosticRepositoryDatabaseInfoCe` MBean as follows:

``` xml
<bean id="diagnosticRepositoryDatabaseInfoCe" class=
      "com.jaspersoft.jasperserver.api.logging.diagnostic.jmx.DiagnosticDynamicMBean">
    <property name="diagnosticServices">
        <set>
            <ref bean="repositoryDatabaseInfo"/>
        </set>
    </property>
    <property name="excludedDiagnosticAttributes">
        <set>
            <value>DatabaseProductName</value>
            <value>DatabaseProductVersion</value>
            <value>DriverName</value>
            <value>SQLKeywords</value>
            <value>URL</value>
            <value>UserName</value>
            <value>JDBCMajorVersion</value>
            <value>JDBCMinorVersion</value>
            <!--
            <value>MaxRowSize</value>
            <value>MaxStatementLength</value>
            <value>MaxConnections</value>
            <value>MaxCharLiteralLength</value>
            <value>MaxColumnsInTable</value>
            <value>MaxColumnsInSelect</value>
            <value>MaxColumnsInGroupBy</value>
            <value>MaxColumnNameLength</value>
            -->
        </set>
    </property>
</bean>
```

-   To exclude an entire bean, comment it out or remove it from the list of beans in the `diagnosticExportingMBeansMap`. For example, instead of excluding selected attributes, you could remove the entire repository database MBean as follows:

``` xml
<util:map id="diagnosticExportingMBeansMap" >
    <entry key="jasperserver:name=Users" value-ref="${bean.diagnosticUsers}"/>
    <entry key="jasperserver:name=Reports" value-ref="${bean.diagnosticReports}"/>
    <entry key="jasperserver:name=Scheduler" value-ref="${bean.diagnosticScheduler}"/>
    <entry key="jasperserver:name=Settings" value-ref="${bean.diagnosticSettings}"/>
    <entry key="jasperserver:name=Repository" value-ref="${bean.diagnosticRepository}"/>
    <entry key="jasperserver:name=About" value-ref="${bean.diagnosticJSAbout}"/>
    <entry key="jasperserver:name=HibernateStatics"
           value-ref="${bean.diagnosticHibernate}"/>
    <entry key="jasperserver:name=EhCache"
            value-ref="${bean.diagnosticEhCache}"/>
    <entry key="jasperserver:name=ExternalInfo"
            value-ref="${bean.diagnosticExternalInfo}"/>
    <!--
    <entry key="jasperserver:name=RepositoryDatabase"
            value-ref="${bean.diagnosticRepositoryDatabaseInfo}"/>
    -->
</util:map>
```
